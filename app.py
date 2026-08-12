"""
Flask Web Application
Main web interface for plagiarism detection system
"""

from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Import custom modules
from config import *
from text_extraction import extract_text, remove_references_section
from text_preprocessing import preprocess_text
from similarity_detection import compare_documents, identify_plagiarized_sections
from file_storage import (
    store_submission, get_all_stored_documents, update_submission_similarity,
    get_submission_by_id, load_index, delete_submission, get_statistics
)
from report_generation import generate_report

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload document page"""
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if not allowed_file(file.filename):
            flash('Invalid file type. Only PDF and DOCX files are allowed.', 'error')
            return redirect(request.url)
        
        # Get student information
        student_name = request.form.get('student_name', '').strip()
        student_id = request.form.get('student_id', '').strip()
        
        if not student_name or not student_id:
            flash('Please provide both student name and ID', 'error')
            return redirect(request.url)
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        temp_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(temp_path)
        
        try:
            # Store submission
            submission_record = store_submission(temp_path, student_name, student_id, filename)
            
            # Remove temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            flash('File uploaded successfully!', 'success')
            return redirect(url_for('check_plagiarism', submission_id=submission_record['id']))
            
        except Exception as e:
            flash(f'Error processing file: {str(e)}', 'error')
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return redirect(request.url)
    
    return render_template('upload.html')


@app.route('/check/<submission_id>')
def check_plagiarism(submission_id):
    """Check plagiarism for a submission"""
    # Get submission record
    submission = get_submission_by_id(submission_id)
    
    if not submission:
        flash('Submission not found', 'error')
        return redirect(url_for('index'))
    
    try:
        # Extract text from submission
        original_text = extract_text(submission['stored_path'])
        text_without_refs = remove_references_section(original_text)
        
        # Get all stored documents (excluding this one)
        stored_docs = get_all_stored_documents(exclude_id=submission_id)
        
        if not stored_docs:
            flash('No documents available for comparison. This is the first submission.', 'info')
            # Update submission with 0% similarity
            update_submission_similarity(submission_id, 0.0)
            return redirect(url_for('view_submissions'))
        
        # Compare documents
        comparison_result = compare_documents(text_without_refs, stored_docs, threshold=0.3)
        
        # Identify plagiarized sections
        plagiarized_sections = identify_plagiarized_sections(
            original_text,
            comparison_result['matches']
        )
        
        # Update submission similarity
        update_submission_similarity(submission_id, comparison_result['overall_similarity'])
        
        # Generate report
        metadata = {
            'student_name': submission['student_name'],
            'student_id': submission['student_id'],
            'filename': submission['filename'],
            'submission_date': submission['submission_date'],
            'submission_time': submission['submission_time']
        }
        
        report_path = generate_report(
            metadata,
            original_text,
            plagiarized_sections,
            comparison_result['source_contributions'],
            comparison_result['overall_similarity']
        )
        
        # Store report path in session or pass to template
        flash('Plagiarism check completed!', 'success')
        return redirect(url_for('view_report', 
                               submission_id=submission_id,
                               report_file=os.path.basename(report_path)))
        
    except Exception as e:
        flash(f'Error checking plagiarism: {str(e)}', 'error')
        return redirect(url_for('view_submissions'))


@app.route('/report/<submission_id>/<report_file>')
def view_report(submission_id, report_file):
    """View plagiarism report"""
    submission = get_submission_by_id(submission_id)
    
    if not submission:
        flash('Submission not found', 'error')
        return redirect(url_for('index'))
    
    report_path = os.path.join(REPORTS_FOLDER, report_file)
    
    if not os.path.exists(report_path):
        flash('Report not found', 'error')
        return redirect(url_for('view_submissions'))
    
    # Read report content
    with open(report_path, 'r', encoding='utf-8') as f:
        report_content = f.read()
    
    return render_template('report.html', 
                         report_content=report_content,
                         submission=submission,
                         report_file=report_file)


@app.route('/download_report/<report_file>')
def download_report(report_file):
    """Download report file"""
    report_path = os.path.join(REPORTS_FOLDER, report_file)
    
    if not os.path.exists(report_path):
        flash('Report not found', 'error')
        return redirect(url_for('index'))
    
    return send_file(report_path, as_attachment=True)


@app.route('/submissions')
def view_submissions():
    """View all submissions"""
    submissions = load_index()
    # Sort by submission datetime (newest first)
    submissions.sort(key=lambda x: x.get('submission_datetime', ''), reverse=True)
    
    return render_template('submissions.html', submissions=submissions)


@app.route('/admin')
def admin_dashboard():
    """Admin dashboard"""
    submissions = load_index()
    statistics = get_statistics()
    
    # Sort submissions by similarity (highest first)
    submissions_sorted = sorted(submissions, 
                               key=lambda x: x.get('overall_similarity', 0), 
                               reverse=True)
    
    return render_template('admin.html', 
                         submissions=submissions_sorted,
                         statistics=statistics)


@app.route('/delete/<submission_id>', methods=['POST'])
def delete_submission_route(submission_id):
    """Delete a submission"""
    success = delete_submission(submission_id)
    
    if success:
        flash('Submission deleted successfully', 'success')
    else:
        flash('Error deleting submission', 'error')
    
    return redirect(url_for('admin_dashboard'))


@app.route('/api/statistics')
def api_statistics():
    """API endpoint for statistics"""
    stats = get_statistics()
    return jsonify(stats)


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


if __name__ == '__main__':
    # Create necessary directories
    for directory in [UPLOAD_FOLDER, STORAGE_FOLDER, REPORTS_FOLDER]:
        os.makedirs(directory, exist_ok=True)
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

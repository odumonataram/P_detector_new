"""
File Storage Manager Module
Handles file storage and indexing
"""

import os
import json
import shutil
from datetime import datetime
from config import STORAGE_FOLDER, INDEX_FILE
from text_extraction import extract_text, remove_references_section


def initialize_index():
    """
    Initialize the submissions index file if it doesn't exist
    """
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'w') as f:
            json.dump([], f)


def load_index():
    """
    Load the submissions index
    
    Returns:
        List of submission records
    """
    initialize_index()
    try:
        with open(INDEX_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading index: {e}")
        return []


def save_index(index_data):
    """
    Save the submissions index
    
    Args:
        index_data: List of submission records
    """
    try:
        with open(INDEX_FILE, 'w') as f:
            json.dump(index_data, f, indent=4)
    except Exception as e:
        print(f"Error saving index: {e}")


def store_submission(file_path, student_name, student_id, filename):
    """
    Store a submitted file and add to index
    
    Args:
        file_path: Path to uploaded file
        student_name: Name of student
        student_id: Student ID
        filename: Original filename
        
    Returns:
        Submission record dictionary
    """
    # Create timestamp-based filename to avoid collisions
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_extension = os.path.splitext(filename)[1]
    stored_filename = f"{student_id}_{timestamp}{file_extension}"
    stored_path = os.path.join(STORAGE_FOLDER, stored_filename)
    
    # Copy file to storage
    shutil.copy2(file_path, stored_path)
    
    # Extract text from file
    text = extract_text(stored_path)
    text_without_refs = remove_references_section(text)
    
    # Create submission record
    submission_record = {
        'id': timestamp + student_id,  # Unique ID
        'filename': filename,
        'stored_filename': stored_filename,
        'stored_path': stored_path,
        'student_name': student_name,
        'student_id': student_id,
        'submission_date': datetime.now().strftime('%Y-%m-%d'),
        'submission_time': datetime.now().strftime('%H:%M:%S'),
        'submission_datetime': datetime.now().isoformat(),
        'text_length': len(text),
        'similarity_checked': False,
        'overall_similarity': 0.0
    }
    
    # Add to index
    index = load_index()
    index.append(submission_record)
    save_index(index)
    
    return submission_record


def get_all_stored_documents(exclude_id=None):
    """
    Get all stored documents for comparison
    
    Args:
        exclude_id: ID of submission to exclude (the one being checked)
        
    Returns:
        Dictionary of {filename: text}
    """
    documents = {}
    index = load_index()
    
    for record in index:
        # Skip the document being checked
        if exclude_id and record['id'] == exclude_id:
            continue
        
        # Extract text from stored file
        text = extract_text(record['stored_path'])
        text_without_refs = remove_references_section(text)
        
        if text_without_refs:
            documents[record['filename']] = text_without_refs
    
    return documents


def update_submission_similarity(submission_id, overall_similarity):
    """
    Update the similarity score for a submission
    
    Args:
        submission_id: ID of submission
        overall_similarity: Overall similarity percentage
    """
    index = load_index()
    
    for record in index:
        if record['id'] == submission_id:
            record['similarity_checked'] = True
            record['overall_similarity'] = overall_similarity
            break
    
    save_index(index)


def get_submission_by_id(submission_id):
    """
    Get submission record by ID
    
    Args:
        submission_id: ID of submission
        
    Returns:
        Submission record or None
    """
    index = load_index()
    
    for record in index:
        if record['id'] == submission_id:
            return record
    
    return None


def delete_submission(submission_id):
    """
    Delete a submission from storage and index
    
    Args:
        submission_id: ID of submission to delete
        
    Returns:
        True if successful, False otherwise
    """
    index = load_index()
    
    for i, record in enumerate(index):
        if record['id'] == submission_id:
            # Delete file
            try:
                if os.path.exists(record['stored_path']):
                    os.remove(record['stored_path'])
            except Exception as e:
                print(f"Error deleting file: {e}")
            
            # Remove from index
            index.pop(i)
            save_index(index)
            return True
    
    return False


def get_statistics():
    """
    Get system statistics
    
    Returns:
        Dictionary of statistics
    """
    index = load_index()
    
    if not index:
        return {
            'total_submissions': 0,
            'average_similarity': 0.0,
            'high_similarity_count': 0,
            'submissions_by_date': {},
            'top_students': []
        }
    
    # Calculate statistics
    total = len(index)
    checked = [r for r in index if r['similarity_checked']]
    
    if checked:
        avg_similarity = sum(r['overall_similarity'] for r in checked) / len(checked)
        high_similarity = len([r for r in checked if r['overall_similarity'] > 50])
    else:
        avg_similarity = 0.0
        high_similarity = 0
    
    # Submissions by date
    submissions_by_date = {}
    for record in index:
        date = record['submission_date']
        submissions_by_date[date] = submissions_by_date.get(date, 0) + 1
    
    # Top students by submission count
    students = {}
    for record in index:
        student = record['student_name']
        students[student] = students.get(student, 0) + 1
    
    top_students = sorted(students.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return {
        'total_submissions': total,
        'average_similarity': round(avg_similarity, 2),
        'high_similarity_count': high_similarity,
        'submissions_by_date': submissions_by_date,
        'top_students': top_students
    }

# Plagiarism Detection System

A comprehensive, web-based plagiarism detection system with a Turnitin-like interface. Built with Python and Flask, this system provides professional plagiarism checking with detailed reports, visualizations, and an admin dashboard.

## 🌟 Features

### 1. File Upload Module
- Upload Word (.docx) and PDF (.pdf) files
- Automatic text extraction from uploaded files
- Local storage organization by student and date
- CSV/JSON index for submission tracking
- Metadata collection: filename, student ID/name, submission date & time

### 2. Text Preprocessing Module
- Convert text to lowercase
- Remove punctuation and special characters
- Remove stopwords (English)
- Sentence tokenization
- Automatic exclusion of References/Bibliography sections

### 3. Similarity Detection Module
- TF-IDF vectorization with cosine similarity
- Sentence-level comparison
- Document-level similarity scoring
- Source attribution for matched content
- Configurable similarity thresholds

### 4. Report Generation Module (Turnitin-Like)
- Full document display with inline highlights
- Color-coded similarity levels:
  - **Green (0-20%)**: Low similarity
  - **Yellow (21-50%)**: Moderate similarity
  - **Orange (51-80%)**: High similarity
  - **Red (81-100%)**: Very high similarity
- Source file names and similarity percentages inline
- Comprehensive metadata display:
  - Submitter name and student ID
  - Submission date and time
  - Overall similarity percentage
- Interactive visualizations:
  - Pie chart: Similarity distribution by source
  - Bar chart: Top contributing sources
  - Heatmap: Plagiarism intensity across document
- Downloadable HTML reports

### 5. Web Interface Module
- Modern, responsive Turnitin-like GUI
- Document upload interface
- Overall similarity percentage display
- Full document view with highlighted sections
- Interactive charts and heatmaps
- One-click report downloads

### 6. Admin Dashboard
- Complete submission overview table
- Student name/ID, document name, date/time
- Overall similarity percentage for each submission
- Advanced filtering:
  - By student name
  - By submission date
  - By similarity threshold
- System statistics:
  - Total number of submissions
  - Average similarity per student
  - High similarity count (>50%)
  - Submissions over time chart
  - Most active students
- Delete old submissions
- Monitor system usage and trends

## 🛠️ Technology Stack

- **Backend Framework**: Flask (Python)
- **Text Extraction**: python-docx, pdfplumber, PyPDF2
- **Text Processing**: NLTK, spaCy
- **Machine Learning**: scikit-learn (TF-IDF, cosine similarity)
- **Visualization**: Matplotlib, Seaborn
- **Storage**: JSON-based local file system
- **Frontend**: HTML5, CSS3, JavaScript

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone or download the project**:
   ```bash
   cd plagiarism_detector
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**:
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## 🎯 Running the System

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **The system is now ready to use!**

## 📖 Usage Guide

### For Students/Lecturers

1. **Upload a Document**:
   - Click "Upload" in the navigation menu
   - Enter student name and ID
   - Select a PDF or DOCX file
   - Click "Upload and Check Plagiarism"

2. **View Results**:
   - System automatically processes the document
   - Redirects to report page with results
   - View highlighted plagiarized sections
   - Check overall similarity percentage
   - Explore charts and visualizations

3. **Download Report**:
   - Click "Download Report" button
   - Save HTML report for records

### For Administrators

1. **Access Admin Dashboard**:
   - Click "Admin" in the navigation menu
   - View system statistics
   - Monitor all submissions

2. **View Statistics**:
   - Total submissions
   - Average similarity percentage
   - High similarity count
   - Submissions over time chart
   - Most active students

3. **Manage Submissions**:
   - View all submissions sorted by similarity
   - Delete old or test submissions
   - Filter by student or date

4. **Monitor Trends**:
   - Track submission patterns
   - Identify high-risk submissions
   - Analyze student behavior

## 📁 Project Structure

```
plagiarism_detector/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── text_extraction.py          # PDF/DOCX text extraction
├── text_preprocessing.py       # Text preprocessing functions
├── similarity_detection.py     # Plagiarism detection algorithms
├── file_storage.py            # File storage and indexing
├── report_generation.py       # Report generation with charts
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Home page
│   ├── upload.html           # Upload page
│   ├── submissions.html      # Submissions list
│   ├── admin.html            # Admin dashboard
│   ├── report.html           # Report viewer
│   └── about.html            # About page
│
├── static/                    # Static files
│   ├── css/
│   │   └── style.css         # Main stylesheet
│   └── js/
│
├── uploads/                   # Temporary upload folder
├── storage/                   # Stored documents
│   └── submissions_index.json # Submission index
└── reports/                   # Generated reports
```

## 🎨 Color-Coded Similarity Levels

The system uses color coding to visually represent similarity levels:

| Color | Range | Meaning |
|-------|-------|---------|
| 🟢 Green | 0-20% | Low similarity - Acceptable |
| 🟡 Yellow | 21-50% | Moderate similarity - Review recommended |
| 🟠 Orange | 51-80% | High similarity - Investigation needed |
| 🔴 Red | 81-100% | Very high similarity - Likely plagiarism |

## 📊 Report Contents

Each plagiarism report includes:

1. **Metadata Section**:
   - Student name and ID
   - Document name
   - Submission date and time
   - Overall similarity percentage
   - Number of matches found

2. **Visualizations**:
   - Pie chart showing similarity distribution by source
   - Bar chart of top contributing sources
   - Heatmap showing plagiarism intensity across document

3. **Document Content**:
   - Full text with highlighted plagiarized sections
   - Color-coded highlights based on similarity
   - Inline similarity percentages
   - Source attribution for each match

## ⚙️ Configuration

Key settings can be modified in `config.py`:

```python
# File size limit (default: 16MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Similarity thresholds for color coding
THRESHOLDS = {
    'green': (0, 20),
    'yellow': (21, 50),
    'orange': (51, 80),
    'red': (81, 100)
}

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
```

## 🔒 Data Storage

- **Storage Type**: Local file system (no database required)
- **Index Format**: JSON
- **Document Storage**: Organized by student ID and timestamp
- **Reports**: HTML format with embedded images

### Storage Locations:

- **Uploaded Files**: `storage/` directory
- **Reports**: `reports/` directory
- **Index**: `storage/submissions_index.json`

## 🧪 Testing

To test the system:

1. **Upload test documents**:
   - Create or use sample academic papers
   - Upload with different student IDs

2. **Test plagiarism detection**:
   - Upload similar content
   - Upload duplicate content
   - Upload original content

3. **Verify reports**:
   - Check highlighting accuracy
   - Verify charts are generated
   - Test download functionality

4. **Test admin features**:
   - View statistics
   - Delete submissions
   - Monitor trends

## 🐛 Troubleshooting

### Common Issues:

1. **"No module named 'nltk'"**:
   ```bash
   pip install nltk
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

2. **"Error extracting text from PDF"**:
   - Ensure PDF is not password-protected
   - Check if PDF contains extractable text (not scanned images)

3. **"File too large"**:
   - Increase `MAX_CONTENT_LENGTH` in `config.py`
   - Or compress/split the document

4. **Charts not displaying**:
   - Ensure matplotlib backend is set correctly
   - Check if matplotlib is installed: `pip install matplotlib`

## 📝 Important Notes

1. **References Exclusion**: The system automatically excludes References and Bibliography sections from plagiarism checking.

2. **First Submission**: The first uploaded document will always show 0% similarity as there are no prior documents to compare against.

3. **Storage Management**: Regularly review and delete old submissions to manage storage space.

4. **Similarity Scores**: Scores are algorithmic and should be reviewed by instructors for context.

5. **Local Only**: This system does not check against external sources or the internet.

## 🔜 Future Enhancements

Potential improvements for future versions:

- Support for more file formats (TXT, RTF, HTML)
- Integration with external plagiarism databases
- Advanced NLP techniques (Word2Vec, BERT)
- User authentication and authorization
- Database integration (PostgreSQL, MongoDB)
- API for programmatic access
- Batch upload support
- Email notifications
- Export to PDF format
- Multi-language support

## 📄 License

This project is provided as-is for educational and institutional use.

## 🤝 Support

For issues, questions, or contributions, please refer to the documentation or contact the system administrator.

## 📚 References

- TF-IDF: Term Frequency-Inverse Document Frequency
- Cosine Similarity: Measure of similarity between vectors
- NLTK: Natural Language Toolkit
- Flask: Python web framework
- scikit-learn: Machine learning library

---

**Version**: 1.0.0  
**Last Updated**: January 2026  
**Status**: Production Ready ✅

"""
Configuration file for Plagiarism Detection System
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Storage directories
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
STORAGE_FOLDER = os.path.join(BASE_DIR, 'storage')
REPORTS_FOLDER = os.path.join(BASE_DIR, 'reports')

# Index file for submissions
INDEX_FILE = os.path.join(STORAGE_FOLDER, 'submissions_index.json')

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Similarity thresholds (for color coding)
THRESHOLDS = {
    'green': (0, 20),
    'yellow': (21, 50),
    'orange': (51, 80),
    'red': (81, 100)
}

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-this')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Create directories if they don't exist
for directory in [UPLOAD_FOLDER, STORAGE_FOLDER, REPORTS_FOLDER]:
    os.makedirs(directory, exist_ok=True)

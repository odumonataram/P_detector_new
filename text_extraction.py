"""
Text Extraction Module
Extracts text from PDF and DOCX files
"""

import pdfplumber
from docx import Document
import re


def extract_text_from_pdf(file_path):
    """
    Extract text from PDF file
    
    Args:
        file_path: Path to PDF file
        
    Returns:
        Extracted text as string
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return ""


def extract_text_from_docx(file_path):
    """
    Extract text from DOCX file
    
    Args:
        file_path: Path to DOCX file
        
    Returns:
        Extracted text as string
    """
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting DOCX text: {e}")
        return ""


def extract_text(file_path):
    """
    Extract text from file based on extension
    
    Args:
        file_path: Path to file
        
    Returns:
        Extracted text as string
    """
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return ""


def remove_references_section(text):
    """
    Remove References/Bibliography section from text
    
    Args:
        text: Input text
        
    Returns:
        Text without references section
    """
    # Common patterns for references section
    patterns = [
        r'(?i)\n\s*references\s*\n.*',
        r'(?i)\n\s*bibliography\s*\n.*',
        r'(?i)\n\s*works cited\s*\n.*',
        r'(?i)\n\s*literature cited\s*\n.*'
    ]
    
    for pattern in patterns:
        text = re.split(pattern, text)[0]
    
    return text

"""
Text Preprocessing Module
Handles text preprocessing for plagiarism detection
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


def preprocess_text(text, remove_stopwords=True):
    """
    Preprocess text for plagiarism detection
    
    Steps:
    1. Convert to lowercase
    2. Remove special characters and punctuation
    3. Remove stopwords (optional)
    4. Tokenize
    
    Args:
        text: Input text string
        remove_stopwords: Whether to remove stopwords
        
    Returns:
        Preprocessed text as string
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove stopwords if requested
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        text = ' '.join([word for word in words if word not in stop_words])
    
    return text


def tokenize_sentences(text):
    """
    Tokenize text into sentences
    
    Args:
        text: Input text string
        
    Returns:
        List of sentences
    """
    try:
        sentences = sent_tokenize(text)
        # Filter out very short sentences (likely not meaningful)
        sentences = [s for s in sentences if len(s.split()) > 3]
        return sentences
    except Exception as e:
        print(f"Error tokenizing sentences: {e}")
        return []


def create_ngrams(text, n=3):
    """
    Create n-grams from text
    
    Args:
        text: Input text string
        n: Size of n-grams
        
    Returns:
        List of n-grams
    """
    words = word_tokenize(text.lower())
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams


def split_into_paragraphs(text):
    """
    Split text into paragraphs
    
    Args:
        text: Input text string
        
    Returns:
        List of paragraphs
    """
    # Split by double newlines or multiple spaces
    paragraphs = re.split(r'\n\s*\n', text)
    # Filter out empty paragraphs
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return paragraphs

"""
Similarity Detection Module
Compares documents and detects plagiarism using TF-IDF and cosine similarity
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from text_preprocessing import preprocess_text, tokenize_sentences
import re


def calculate_cosine_similarity(text1, text2):
    """
    Calculate cosine similarity between two texts using TF-IDF
    
    Args:
        text1: First text
        text2: Second text
        
    Returns:
        Similarity score (0-1)
    """
    try:
        # Preprocess texts
        preprocessed1 = preprocess_text(text1, remove_stopwords=False)
        preprocessed2 = preprocess_text(text2, remove_stopwords=False)
        
        if not preprocessed1 or not preprocessed2:
            return 0.0
        
        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([preprocessed1, preprocessed2])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        return float(similarity)
    except Exception as e:
        print(f"Error calculating similarity: {e}")
        return 0.0


def find_matching_sentences(new_text, stored_text, threshold=0.5):
    """
    Find matching sentences between two texts
    
    Args:
        new_text: New document text
        stored_text: Stored document text
        threshold: Minimum similarity threshold
        
    Returns:
        List of matches with sentence pairs and similarity scores
    """
    matches = []
    
    # Tokenize into sentences
    new_sentences = tokenize_sentences(new_text)
    stored_sentences = tokenize_sentences(stored_text)
    
    if not new_sentences or not stored_sentences:
        return matches
    
    # Compare each sentence in new text with sentences in stored text
    for i, new_sent in enumerate(new_sentences):
        for j, stored_sent in enumerate(stored_sentences):
            similarity = calculate_cosine_similarity(new_sent, stored_sent)
            
            if similarity >= threshold:
                matches.append({
                    'new_sentence': new_sent,
                    'new_sentence_index': i,
                    'matched_sentence': stored_sent,
                    'matched_sentence_index': j,
                    'similarity': similarity * 100  # Convert to percentage
                })
    
    return matches


def compare_documents(new_doc_text, stored_docs, threshold=0.5):
    """
    Compare new document against all stored documents
    
    Args:
        new_doc_text: Text of new document
        stored_docs: Dictionary of stored documents {filename: text}
        threshold: Minimum similarity threshold
        
    Returns:
        Dictionary containing:
        - overall_similarity: Overall similarity percentage
        - matches: List of matches per source document
        - source_contributions: Similarity contribution per source
    """
    all_matches = []
    source_contributions = {}
    
    # Compare against each stored document
    for filename, stored_text in stored_docs.items():
        # Find matching sentences
        matches = find_matching_sentences(new_doc_text, stored_text, threshold)
        
        if matches:
            # Calculate overall similarity for this source
            doc_similarity = calculate_cosine_similarity(new_doc_text, stored_text) * 100
            
            source_contributions[filename] = doc_similarity
            
            for match in matches:
                match['source_file'] = filename
                all_matches.append(match)
    
    # Calculate overall similarity (average of top sources)
    if source_contributions:
        overall_similarity = max(source_contributions.values())
    else:
        overall_similarity = 0.0
    
    return {
        'overall_similarity': overall_similarity,
        'matches': all_matches,
        'source_contributions': source_contributions
    }


def get_sentence_positions(text, sentence):
    """
    Find the position of a sentence in the original text
    
    Args:
        text: Original text
        sentence: Sentence to find
        
    Returns:
        Tuple of (start_pos, end_pos)
    """
    # Try to find exact match first
    start = text.find(sentence)
    if start != -1:
        return (start, start + len(sentence))
    
    # If not found, try fuzzy matching
    # Look for the first few words of the sentence
    words = sentence.split()[:5]
    search_pattern = ' '.join(words)
    
    start = text.lower().find(search_pattern.lower())
    if start != -1:
        # Estimate end position
        end = start + len(sentence)
        return (start, min(end, len(text)))
    
    return (-1, -1)


def identify_plagiarized_sections(original_text, matches):
    """
    Identify plagiarized sections in the original text with their positions
    
    Args:
        original_text: Original document text
        matches: List of match dictionaries from compare_documents
        
    Returns:
        List of plagiarized sections with positions and metadata
    """
    sections = []
    
    for match in matches:
        sentence = match['new_sentence']
        start_pos, end_pos = get_sentence_positions(original_text, sentence)
        
        if start_pos != -1:
            sections.append({
                'text': sentence,
                'start': start_pos,
                'end': end_pos,
                'similarity': match['similarity'],
                'source': match['source_file'],
                'matched_text': match['matched_sentence']
            })
    
    # Sort by position
    sections.sort(key=lambda x: x['start'])
    
    # Merge overlapping sections
    merged_sections = []
    for section in sections:
        if not merged_sections:
            merged_sections.append(section)
        else:
            last = merged_sections[-1]
            # If sections overlap or are very close
            if section['start'] <= last['end'] + 50:
                # Merge sections
                if section['similarity'] > last['similarity']:
                    last['end'] = max(last['end'], section['end'])
                    last['similarity'] = section['similarity']
                    last['source'] = section['source']
                    last['matched_text'] = section['matched_text']
            else:
                merged_sections.append(section)
    
    return merged_sections

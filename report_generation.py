"""
Report Generation Module
Generates plagiarism reports in various formats (HTML, PDF, DOCX)
"""

import os
from datetime import datetime
from docx import Document
from docx.shared import RGBColor, Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from config import REPORTS_FOLDER, THRESHOLDS


def get_similarity_color(similarity):
    """
    Get color based on similarity percentage
    
    Args:
        similarity: Similarity percentage (0-100)
        
    Returns:
        Tuple of (color_name, rgb_tuple)
    """
    if similarity <= THRESHOLDS['green'][1]:
        return ('green', (0, 255, 0))
    elif similarity <= THRESHOLDS['yellow'][1]:
        return ('yellow', (255, 255, 0))
    elif similarity <= THRESHOLDS['orange'][1]:
        return ('orange', (255, 165, 0))
    else:
        return ('red', (255, 0, 0))


def get_similarity_color_hex(similarity):
    """
    Get hex color based on similarity percentage
    
    Args:
        similarity: Similarity percentage (0-100)
        
    Returns:
        Hex color string
    """
    if similarity <= THRESHOLDS['green'][1]:
        return '#90EE90'  # Light green
    elif similarity <= THRESHOLDS['yellow'][1]:
        return '#FFFF99'  # Light yellow
    elif similarity <= THRESHOLDS['orange'][1]:
        return '#FFB366'  # Light orange
    else:
        return '#FF6B6B'  # Light red


def create_pie_chart(source_contributions):
    """
    Create pie chart of similarity per source
    
    Args:
        source_contributions: Dictionary of {source: similarity}
        
    Returns:
        Base64 encoded image
    """
    if not source_contributions:
        return None
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sources = list(source_contributions.keys())[:10]  # Top 10 sources
    similarities = [source_contributions[s] for s in sources]
    
    # Shorten long filenames
    labels = [s[:20] + '...' if len(s) > 20 else s for s in sources]
    
    colors = sns.color_palette('Set3', len(sources))
    ax.pie(similarities, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title('Similarity Distribution by Source', fontsize=14, fontweight='bold')
    
    # Save to base64
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64


def create_bar_chart(source_contributions):
    """
    Create bar chart of top contributing sources
    
    Args:
        source_contributions: Dictionary of {source: similarity}
        
    Returns:
        Base64 encoded image
    """
    if not source_contributions:
        return None
    
    # Sort by similarity and take top 10
    sorted_sources = sorted(source_contributions.items(), key=lambda x: x[1], reverse=True)[:10]
    sources = [s[0] for s in sorted_sources]
    similarities = [s[1] for s in sorted_sources]
    
    # Shorten long filenames
    labels = [s[:30] + '...' if len(s) > 30 else s for s in sources]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(range(len(labels)), similarities, color=sns.color_palette('viridis', len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel('Similarity (%)', fontsize=12)
    ax.set_title('Top Contributing Sources', fontsize=14, fontweight='bold')
    ax.invert_yaxis()
    
    # Add value labels on bars
    for i, (bar, val) in enumerate(zip(bars, similarities)):
        ax.text(val + 1, i, f'{val:.1f}%', va='center', fontsize=10)
    
    # Save to base64
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64


def create_heatmap(plagiarized_sections, original_text):
    """
    Create heatmap showing plagiarism intensity across document
    
    Args:
        plagiarized_sections: List of plagiarized sections
        original_text: Original document text
        
    Returns:
        Base64 encoded image
    """
    if not plagiarized_sections or not original_text:
        return None
    
    # Divide document into chunks
    chunk_size = max(len(original_text) // 20, 100)  # 20 chunks
    num_chunks = (len(original_text) + chunk_size - 1) // chunk_size
    
    # Calculate similarity for each chunk
    chunk_similarities = [0] * num_chunks
    
    for section in plagiarized_sections:
        start_chunk = section['start'] // chunk_size
        end_chunk = min(section['end'] // chunk_size, num_chunks - 1)
        
        for i in range(start_chunk, end_chunk + 1):
            chunk_similarities[i] = max(chunk_similarities[i], section['similarity'])
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 2))
    
    data = [chunk_similarities]
    im = ax.imshow(data, cmap='RdYlGn_r', aspect='auto', vmin=0, vmax=100)
    
    ax.set_yticks([])

    tick_positions = list(range(0, num_chunks, max(num_chunks // 10, 1)))
    ax.set_xticks(tick_positions)

    tick_labels = [f'{int((pos / max(num_chunks - 1, 1)) * 100)}%' for pos in tick_positions]
    ax.set_xticklabels(tick_labels)

    ax.set_xlabel('Document Position', fontsize=12)
    ax.set_title('Plagiarism Heatmap Across Document', fontsize=14, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, orientation='horizontal', pad=0.1)
    cbar.set_label('Similarity (%)', fontsize=10)
    
    # Save to base64
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64


def generate_html_report(metadata, original_text, plagiarized_sections, 
                         source_contributions, overall_similarity):
    """
    Generate HTML report with highlighted plagiarized sections
    
    Args:
        metadata: Dictionary with student info
        original_text: Original document text
        plagiarized_sections: List of plagiarized sections
        source_contributions: Dictionary of source similarities
        overall_similarity: Overall similarity percentage
        
    Returns:
        HTML string
    """
    # Create charts
    pie_chart = create_pie_chart(source_contributions)
    bar_chart = create_bar_chart(source_contributions)
    heatmap = create_heatmap(plagiarized_sections, original_text)
    
    # Build highlighted text
    highlighted_html = ""
    last_pos = 0
    
    for section in plagiarized_sections:
        # Add text before this section
        if section['start'] > last_pos:
            highlighted_html += original_text[last_pos:section['start']]
        
        # Add highlighted section
        color = get_similarity_color_hex(section['similarity'])
        tooltip = f"Source: {section['source']}<br>Similarity: {section['similarity']:.1f}%<br>Matched: {section['matched_text'][:100]}..."
        
        highlighted_html += f'''<span class="highlight" style="background-color: {color};" 
                                  data-toggle="tooltip" 
                                  title="{tooltip}"
                                  data-similarity="{section['similarity']:.1f}"
                                  data-source="{section['source']}">
                                  {original_text[section['start']:section['end']]}
                                  <sup class="similarity-badge">{section['similarity']:.0f}%</sup>
                                </span>'''
        
        last_pos = section['end']
    
    # Add remaining text
    if last_pos < len(original_text):
        highlighted_html += original_text[last_pos:]
    
    # Get color for overall similarity
    overall_color = get_similarity_color_hex(overall_similarity)
    
    # Build HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Plagiarism Report - {metadata['student_name']}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 1200px;
                margin: 20px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .header {{
                background-color: #2c3e50;
                color: white;
                padding: 30px;
                border-radius: 10px;
                margin-bottom: 30px;
            }}
            .header h1 {{
                margin: 0;
                font-size: 32px;
            }}
            .metadata {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                background-color: white;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .metadata-item {{
                padding: 10px;
            }}
            .metadata-label {{
                font-weight: bold;
                color: #555;
                font-size: 14px;
            }}
            .metadata-value {{
                font-size: 16px;
                color: #222;
                margin-top: 5px;
            }}
            .similarity-box {{
                text-align: center;
                background-color: {overall_color};
                padding: 30px;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.2);
            }}
            .similarity-box h2 {{
                margin: 0;
                font-size: 48px;
                color: #333;
            }}
            .similarity-box p {{
                margin: 10px 0 0 0;
                font-size: 18px;
                color: #555;
            }}
            .charts {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin-bottom: 30px;
            }}
            .chart-container {{
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                text-align: center;
            }}
            .chart-container img {{
                max-width: 100%;
                height: auto;
            }}
            .heatmap-container {{
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }}
            .heatmap-container img {{
                width: 100%;
                height: auto;
            }}
            .document-container {{
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                line-height: 1.8;
            }}
            .document-title {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            .highlight {{
                position: relative;
                padding: 2px 4px;
                border-radius: 3px;
                cursor: help;
                transition: all 0.3s ease;
            }}
            .highlight:hover {{
                opacity: 0.8;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
            }}
            .similarity-badge {{
                font-size: 10px;
                font-weight: bold;
                color: #333;
                margin-left: 2px;
                padding: 1px 3px;
                background-color: rgba(255,255,255,0.7);
                border-radius: 3px;
            }}
            .legend {{
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .legend h3 {{
                margin-top: 0;
                color: #2c3e50;
            }}
            .legend-item {{
                display: inline-block;
                margin-right: 30px;
                margin-bottom: 10px;
            }}
            .legend-color {{
                display: inline-block;
                width: 30px;
                height: 20px;
                border-radius: 3px;
                margin-right: 10px;
                vertical-align: middle;
            }}
            @media print {{
                body {{
                    background-color: white;
                }}
                .chart-container, .metadata, .document-container {{
                    box-shadow: none;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📄 Plagiarism Detection Report</h1>
        </div>
        
        <div class="similarity-box">
            <h2>{overall_similarity:.1f}%</h2>
            <p>Overall Similarity Score</p>
        </div>
        
        <div class="metadata">
            <div class="metadata-item">
                <div class="metadata-label">Student Name</div>
                <div class="metadata-value">{metadata['student_name']}</div>
            </div>
            <div class="metadata-item">
                <div class="metadata-label">Student ID</div>
                <div class="metadata-value">{metadata['student_id']}</div>
            </div>
            <div class="metadata-item">
                <div class="metadata-label">Document Name</div>
                <div class="metadata-value">{metadata['filename']}</div>
            </div>
            <div class="metadata-item">
                <div class="metadata-label">Submission Date & Time</div>
                <div class="metadata-value">{metadata['submission_date']} {metadata['submission_time']}</div>
            </div>
            <div class="metadata-item">
                <div class="metadata-label">Report Generated</div>
                <div class="metadata-value">{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
            </div>
            <div class="metadata-item">
                <div class="metadata-label">Total Matches Found</div>
                <div class="metadata-value">{len(plagiarized_sections)}</div>
            </div>
        </div>
        
        <div class="legend">
            <h3>Similarity Color Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #90EE90;"></span>
                <span>0-20% (Low)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFFF99;"></span>
                <span>21-50% (Moderate)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFB366;"></span>
                <span>51-80% (High)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF6B6B;"></span>
                <span>81-100% (Very High)</span>
            </div>
        </div>
    """
    
    # Add charts if available
    if pie_chart or bar_chart:
        html += '<div class="charts">'
        if pie_chart:
            html += f'''
            <div class="chart-container">
                <img src="data:image/png;base64,{pie_chart}" alt="Similarity Distribution">
            </div>
            '''
        if bar_chart:
            html += f'''
            <div class="chart-container">
                <img src="data:image/png;base64,{bar_chart}" alt="Top Sources">
            </div>
            '''
        html += '</div>'
    
    # Add heatmap if available
    if heatmap:
        html += f'''
        <div class="heatmap-container">
            <img src="data:image/png;base64,{heatmap}" alt="Plagiarism Heatmap">
        </div>
        '''
    
    # Add document with highlights
    html += f'''
        <div class="document-container">
            <div class="document-title">Document Content (Highlighted)</div>
            <div style="white-space: pre-wrap;">{highlighted_html}</div>
        </div>
    </body>
    </html>
    '''
    
    return html


def save_html_report(html_content, filename):
    """
    Save HTML report to file
    
    Args:
        html_content: HTML string
        filename: Filename for report
        
    Returns:
        Path to saved report
    """
    report_path = os.path.join(REPORTS_FOLDER, filename)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return report_path


def generate_report(metadata, original_text, plagiarized_sections, 
                   source_contributions, overall_similarity):
    """
    Generate complete plagiarism report
    
    Args:
        metadata: Student and submission information
        original_text: Original document text
        plagiarized_sections: List of plagiarized sections
        source_contributions: Dictionary of source similarities
        overall_similarity: Overall similarity percentage
        
    Returns:
        Path to HTML report
    """
    # Generate HTML report
    html_content = generate_html_report(
        metadata, original_text, plagiarized_sections,
        source_contributions, overall_similarity
    )
    
    # Save HTML report
    report_filename = f"report_{metadata['student_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    report_path = save_html_report(html_content, report_filename)
    
    return report_path

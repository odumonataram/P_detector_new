# Plagiarism Detection System - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [User Interface Guide](#user-interface-guide)
5. [Workflow Examples](#workflow-examples)
6. [Admin Guide](#admin-guide)
7. [Understanding Reports](#understanding-reports)
8. [Best Practices](#best-practices)
9. [FAQs](#faqs)

---

## Introduction

The Plagiarism Detection System is a comprehensive tool designed to identify potential plagiarism in academic documents. It provides:

- Automated plagiarism checking
- Detailed visual reports
- Administrative oversight
- Statistical analysis

### Key Benefits:
- **For Students**: Verify originality before submission
- **For Lecturers**: Quickly check multiple submissions
- **For Administrators**: Monitor academic integrity across courses

---

## System Requirements

### Minimum Requirements:
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 1GB free space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest version)

### Software Dependencies:
- Flask (web framework)
- python-docx (Word processing)
- pdfplumber (PDF processing)
- NLTK (text processing)
- scikit-learn (similarity algorithms)
- matplotlib, seaborn (visualizations)

---

## Installation Guide

### Step-by-Step Installation:

#### 1. Install Python
- Download from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Verify installation:
  ```bash
  python --version
  ```

#### 2. Extract Project Files
- Extract the plagiarism_detector folder to a location of your choice
- Example: `C:\plagiarism_detector` or `~/plagiarism_detector`

#### 3. Open Terminal/Command Prompt
- **Windows**: Press Win+R, type `cmd`, press Enter
- **macOS/Linux**: Open Terminal application

#### 4. Navigate to Project Directory
```bash
cd path/to/plagiarism_detector
```

#### 5. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 6. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 7. Download NLTK Data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

#### 8. Verify Installation
```bash
python app.py
```

If successful, you should see:
```
* Running on http://127.0.0.1:5000
```

---

## User Interface Guide

### Main Navigation

#### 1. Home Page (`/`)
- **Purpose**: Introduction and overview
- **Features**:
  - System features overview
  - Quick access buttons
  - How it works guide

#### 2. Upload Page (`/upload`)
- **Purpose**: Submit documents for checking
- **Required Information**:
  - Student Name (full name)
  - Student ID (unique identifier)
  - Document File (PDF or DOCX, max 16MB)

**Step-by-Step Upload Process:**

1. Click "Upload" in navigation menu
2. Enter student name in first field
3. Enter student ID in second field
4. Click file upload area or drag-and-drop document
5. Verify file name appears
6. Click "Upload and Check Plagiarism"
7. Wait for processing (30 seconds - 2 minutes)
8. Review results on report page

#### 3. Submissions Page (`/submissions`)
- **Purpose**: View all submitted documents
- **Information Displayed**:
  - Student name and ID
  - Document name
  - Submission date and time
  - Similarity percentage (if checked)
  - Check status
- **Actions Available**:
  - Check plagiarism (for unchecked submissions)
  - View report (for checked submissions)

#### 4. Admin Dashboard (`/admin`)
- **Purpose**: System administration and monitoring
- **Features**:
  - System statistics
  - Submission trends chart
  - Top active students
  - Complete submission list
  - Delete submissions

#### 5. About Page (`/about`)
- **Purpose**: System information and documentation
- **Contents**:
  - System overview
  - Feature descriptions
  - Technology information
  - Color legend
  - Important notes

---

## Workflow Examples

### Example 1: Student Self-Check

**Scenario**: A student wants to check their essay before submission.

**Steps**:
1. Navigate to Upload page
2. Enter your name: "Jane Smith"
3. Enter your ID: "S2024001"
4. Upload your essay: "essay_climate_change.docx"
5. Click "Upload and Check Plagiarism"
6. Wait for processing
7. Review the report:
   - Check overall similarity percentage
   - Review highlighted sections
   - Identify sources of matches
8. Download report for records
9. Revise document if needed
10. Re-submit for verification

### Example 2: Lecturer Batch Checking

**Scenario**: A lecturer has 30 student submissions to check.

**Steps**:
1. Prepare a spreadsheet with student names and IDs
2. For each submission:
   - Go to Upload page
   - Enter student information from spreadsheet
   - Upload student's document
   - Wait for processing
3. After all uploads:
   - Go to Submissions page
   - Review similarity scores
   - Flag high-similarity submissions (>50%)
4. Go to Admin dashboard:
   - Check average similarity
   - Identify patterns
   - Download reports for flagged submissions
5. Review flagged cases individually

### Example 3: Administrator Monitoring

**Scenario**: An administrator wants to monitor academic integrity.

**Steps**:
1. Access Admin dashboard daily
2. Review statistics:
   - Total submissions today
   - Average similarity percentage
   - High-risk submissions
3. Check submissions over time chart:
   - Identify submission patterns
   - Spot unusual activity
4. Review top active students:
   - Verify submission frequency is normal
5. Investigate high-similarity submissions:
   - View reports
   - Compare matched sources
6. Generate monthly summary:
   - Export statistics
   - Prepare report for management

---

## Admin Guide

### Accessing Admin Features

The Admin dashboard provides comprehensive oversight capabilities.

### Statistics Panel

**Total Submissions**
- Count of all documents uploaded
- Use to track system usage

**Average Similarity**
- Mean similarity across all checked documents
- Benchmark for normal similarity levels

**High Similarity Count**
- Number of submissions over 50% similarity
- Indicator of potential integrity issues

**Active Students**
- Number of unique students with submissions
- Measure of system adoption

### Submissions Over Time Chart

**Purpose**: Visualize submission patterns

**How to Read**:
- X-axis: Dates
- Y-axis: Number of submissions
- Line shows trend over time

**Use Cases**:
- Identify peak submission periods
- Plan system resources
- Detect unusual activity spikes

### Most Active Students

**Purpose**: Identify students with multiple submissions

**Information Shown**:
- Student name
- Number of submissions

**Actions**:
- Verify submissions are legitimate
- Contact students with excessive submissions
- Ensure compliance with submission policies

### Managing Submissions

#### Deleting Submissions

**When to Delete**:
- Test submissions
- Duplicate submissions
- Withdrawn submissions
- Data cleanup

**How to Delete**:
1. Find submission in admin table
2. Click "Delete" button
3. Confirm deletion
4. Submission and associated files are removed

**Note**: Deletion is permanent and cannot be undone.

#### Filtering and Sorting

**By Similarity**:
- Submissions sorted highest to lowest
- Quickly identify high-risk cases

**By Date**:
- View recent submissions
- Track temporal patterns

**By Student**:
- Review individual student history
- Check for repeat offenders

---

## Understanding Reports

### Report Structure

A complete plagiarism report contains four main sections:

#### 1. Header and Metadata

**Overall Similarity Box**:
- Large percentage display
- Color-coded background
- Most important metric

**Metadata Table**:
- Student name and ID
- Document name
- Submission date and time
- Report generation date
- Total matches found

#### 2. Visual Analytics

**Pie Chart - Similarity Distribution**:
- Shows percentage from each source
- Helps identify primary sources of similarity
- Maximum 10 sources displayed

**Bar Chart - Top Contributing Sources**:
- Ranks sources by similarity percentage
- Displays source names and percentages
- Maximum 10 sources displayed

**Heatmap - Document Sections**:
- Visualizes plagiarism across document
- Color intensity indicates similarity level
- Helps identify problem sections

#### 3. Color Legend

Explains the color coding system:
- Green (0-20%): Low, acceptable
- Yellow (21-50%): Moderate, review
- Orange (51-80%): High, investigate
- Red (81-100%): Very high, likely plagiarism

#### 4. Highlighted Document

**Full Document Display**:
- Complete original text
- Maintains original formatting
- Preserves paragraph structure

**Highlighted Sections**:
- Color-coded based on similarity
- Hover shows details (in web view)
- Similarity badge shows percentage
- Source name indicated

### Interpreting Results

#### Low Similarity (0-20% - Green)
**Interpretation**: Acceptable level of similarity
**Likely Causes**:
- Common phrases
- Standard terminology
- Proper citations
- Normal paraphrasing
**Action**: No action needed

#### Moderate Similarity (21-50% - Yellow)
**Interpretation**: May need review
**Likely Causes**:
- Extensive paraphrasing
- Multiple short matches
- Shared research topics
- Common methodologies
**Action**: Review highlighted sections

#### High Similarity (51-80% - Orange)
**Interpretation**: Significant concern
**Likely Causes**:
- Large copied sections
- Improper paraphrasing
- Missing citations
- Copied structure
**Action**: Investigate thoroughly

#### Very High Similarity (81-100% - Red)
**Interpretation**: Likely plagiarism
**Likely Causes**:
- Direct copying
- Minimal changes
- Duplicate submission
- Text replacement
**Action**: Immediate investigation required

---

## Best Practices

### For Students

1. **Check Early**: Run checks during writing process
2. **Revise and Recheck**: After making changes, verify
3. **Understand Results**: Learn from highlighted sections
4. **Proper Citation**: Always cite sources correctly
5. **Original Writing**: Develop your own voice
6. **Paraphrase Correctly**: Don't just change a few words
7. **Keep Records**: Save reports for reference

### For Lecturers

1. **Establish Baseline**: Check several known-original works
2. **Context Matters**: High similarity doesn't always mean plagiarism
3. **Review Manually**: Use reports as screening tool
4. **Consistent Policy**: Apply same standards to all students
5. **Educate Students**: Teach proper citation and paraphrasing
6. **Document Process**: Keep records of checks and outcomes
7. **Privacy**: Handle student data confidentially

### For Administrators

1. **Regular Monitoring**: Check dashboard weekly
2. **Trend Analysis**: Look for patterns over time
3. **System Maintenance**: Periodically clean old submissions
4. **Backup Data**: Regularly backup submissions_index.json
5. **Security**: Limit admin access appropriately
6. **Capacity Planning**: Monitor storage usage
7. **User Training**: Provide guidance to users

---

## FAQs

### General Questions

**Q: How accurate is the plagiarism detection?**
A: The system uses TF-IDF and cosine similarity, which are industry-standard algorithms. Accuracy depends on the database of stored documents. It's a screening tool that should be combined with human review.

**Q: Does it check against the internet?**
A: No, the system only compares against previously uploaded documents in the local database.

**Q: What file formats are supported?**
A: PDF (.pdf) and Microsoft Word (.docx) files are supported.

**Q: What's the maximum file size?**
A: 16MB by default. This can be changed in config.py if needed.

**Q: Can I delete a submission?**
A: Yes, administrators can delete submissions from the Admin dashboard.

### Technical Questions

**Q: Where are files stored?**
A: Files are stored locally in the `storage/` directory with a JSON index.

**Q: Can I run this on a server?**
A: Yes, but you'll need to configure Flask for production use (see Flask documentation).

**Q: Does it support multiple languages?**
A: Currently optimized for English. Other languages may work but with reduced accuracy.

**Q: Can I customize the similarity thresholds?**
A: Yes, edit the THRESHOLDS dictionary in config.py.

**Q: How long does checking take?**
A: Typically 30 seconds to 2 minutes, depending on document size and number of stored documents.

### Usage Questions

**Q: Why is my first submission showing 0% similarity?**
A: The first document has nothing to compare against. Subsequent submissions will be compared to all previous ones.

**Q: Can the same student upload multiple times?**
A: Yes, each submission is stored separately with timestamp.

**Q: Are References sections checked?**
A: No, the system automatically excludes References and Bibliography sections.

**Q: Can I see which specific document was matched?**
A: Yes, the report shows the source document name for each match.

**Q: How do I interpret a 35% similarity?**
A: 35% falls in the yellow (moderate) range. Review the highlighted sections to determine if it's proper citation, common knowledge, or potential plagiarism.

### Troubleshooting

**Q: The upload isn't working. What should I check?**
A: 
1. Verify file is PDF or DOCX
2. Check file size is under 16MB
3. Ensure file isn't password-protected
4. Try a different browser

**Q: Charts aren't displaying in reports. Why?**
A: Ensure matplotlib and seaborn are installed: `pip install matplotlib seaborn`

**Q: I get an NLTK error. How do I fix it?**
A: Run: `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`

**Q: The system is running slow. What can I do?**
A:
1. Delete old submissions to reduce database size
2. Ensure adequate RAM is available
3. Close unnecessary applications

---

## Appendix

### Color Code Reference Card

| Color | Range | RGB | Hex | Action |
|-------|-------|-----|-----|--------|
| Green | 0-20% | (144, 238, 144) | #90EE90 | Accept |
| Yellow | 21-50% | (255, 255, 153) | #FFFF99 | Review |
| Orange | 51-80% | (255, 179, 102) | #FFB366 | Investigate |
| Red | 81-100% | (255, 107, 107) | #FF6B6B | Flag |

### Keyboard Shortcuts (Web Interface)

- **Ctrl/Cmd + U**: Go to Upload page
- **Ctrl/Cmd + S**: Go to Submissions page
- **Ctrl/Cmd + A**: Go to Admin dashboard
- **Ctrl/Cmd + H**: Go to Home page

### Support Resources

- **README.md**: Complete technical documentation
- **QUICK_START.md**: Fast setup guide
- **This Manual**: Comprehensive user guide
- **Code Comments**: Detailed inline documentation

---

**Document Version**: 1.0  
**Last Updated**: January 2026  
**For**: Plagiarism Detection System v1.0

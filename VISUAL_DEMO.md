# Plagiarism Detection System - Visual Demo Guide

## System Screenshots and Examples

This document provides a visual walkthrough of the Plagiarism Detection System interface and features.

---

## 🏠 Home Page

**URL**: `http://localhost:5000`

### Features Displayed:

```
╔════════════════════════════════════════════════════════════╗
║        📚 PLAGIARISM DETECTION SYSTEM                      ║
║    Professional plagiarism checking with comprehensive     ║
║                    reporting                               ║
╚════════════════════════════════════════════════════════════╝

┌──────────────┬──────────────┬──────────────┬──────────────┐
│  📄          │   🔍         │   📊         │   ⚙️         │
│  Upload      │   Detect     │   Detailed   │   Admin      │
│  Documents   │   Plagiarism │   Reports    │   Dashboard  │
│              │              │              │              │
│ Support for  │ Advanced TF- │ Charts and   │ Monitor and  │
│ PDF & DOCX   │ IDF detection│ highlights   │ manage       │
└──────────────┴──────────────┴──────────────┴──────────────┘

        [Upload Document]  [View Submissions]

HOW IT WORKS:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  1  │ →  │  2  │ →  │  3  │ →  │  4  │
│Upload│    │Analyze│   │Report│   │Review│
└─────┘    └─────┘    └─────┘    └─────┘
```

---

## 📤 Upload Page

**URL**: `http://localhost:5000/upload`

### Upload Form:

```
╔════════════════════════════════════════════════════════════╗
║     Upload Document for Plagiarism Check                  ║
║     Submit PDF or DOCX files for analysis                 ║
╚════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────┐
│ Student Name *                                           │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Enter student name                                 │   │
│ └────────────────────────────────────────────────────┘   │
│                                                          │
│ Student ID *                                             │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Enter student ID                                   │   │
│ └────────────────────────────────────────────────────┘   │
│                                                          │
│ Document File *                                          │
│ ┌────────────────────────────────────────────────────┐   │
│ │              📁                                    │   │
│ │   Click to select file or drag and drop           │   │
│ │   Accepted formats: PDF, DOCX (Max 16MB)          │   │
│ └────────────────────────────────────────────────────┘   │
│                                                          │
│ [Upload and Check Plagiarism]  [Cancel]                 │
└──────────────────────────────────────────────────────────┘

📝 IMPORTANT NOTES:
• Only PDF and DOCX files accepted
• Maximum file size: 16MB
• Files stored securely
• References automatically excluded
```

---

## 📊 Submissions Page

**URL**: `http://localhost:5000/submissions`

### Submissions Table:

```
╔════════════════════════════════════════════════════════════╗
║                    All Submissions                         ║
║            View and manage submitted documents             ║
╚════════════════════════════════════════════════════════════╝

┌─────────────┬────────┬──────────────┬──────────┬──────────┬────────────┬────────┬────────┐
│ Student     │ Student│ Document     │ Submission│ Sub Time │ Similarity │ Status │ Actions│
│ Name        │ ID     │ Name         │ Date      │          │            │        │        │
├─────────────┼────────┼──────────────┼──────────┼──────────┼────────────┼────────┼────────┤
│ John Smith  │ S001   │ essay_1.docx │ 2026-01-15│ 10:30:45 │   🔴 85.3% │ ✓ Check│ [View] │
├─────────────┼────────┼──────────────┼──────────┼──────────┼────────────┼────────┼────────┤
│ Jane Doe    │ S002   │ paper_2.docx │ 2026-01-15│ 11:15:22 │   🟡 35.7% │ ✓ Check│ [View] │
├─────────────┼────────┼──────────────┼──────────┼──────────┼────────────┼────────┼────────┤
│ Bob Wilson  │ S003   │ report.pdf   │ 2026-01-16│ 09:20:11 │   🟢 12.5% │ ✓ Check│ [View] │
├─────────────┼────────┼──────────────┼──────────┼──────────┼────────────┼────────┼────────┤
│ Alice Brown │ S004   │ thesis.docx  │ 2026-01-16│ 14:45:30 │   ⏳ ---   │⏳ Pend │ [Check]│
└─────────────┴────────┴──────────────┴──────────┴──────────┴────────────┴────────┴────────┘

Color Legend:
🟢 Green (0-20%)   🟡 Yellow (21-50%)   🟠 Orange (51-80%)   🔴 Red (81-100%)
```

---

## 🎯 Admin Dashboard

**URL**: `http://localhost:5000/admin`

### Statistics Cards:

```
╔════════════════════════════════════════════════════════════╗
║                   Admin Dashboard                          ║
║          Monitor system usage and manage submissions       ║
╚════════════════════════════════════════════════════════════╝

┌──────────────┬──────────────┬──────────────┬──────────────┐
│   📊 42      │   📈 28.5%   │   ⚠️ 8       │   👥 35      │
│   Total      │   Average    │   High Sim   │   Active     │
│ Submissions  │  Similarity  │   (>50%)     │  Students    │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

### Submissions Over Time Chart:

```
Submissions Over Time
┌─────────────────────────────────────────────────────────┐
│   10│                                          ●         │
│     │                                    ●               │
│    8│                              ●                     │
│     │                        ●                           │
│    6│                  ●                                 │
│     │            ●                                       │
│    4│      ●                                             │
│     │ ●                                                  │
│    2│                                                    │
│     └────────────────────────────────────────────────── │
│     Jan-10  Jan-11  Jan-12  Jan-13  Jan-14  Jan-15      │
└─────────────────────────────────────────────────────────┘
```

### Most Active Students:

```
┌──────────────────────────────────────┐
│ Most Active Students                 │
├──────────────────────────────────────┤
│ John Smith        │ 5 submissions    │
│ Jane Doe          │ 4 submissions    │
│ Bob Wilson        │ 3 submissions    │
│ Alice Brown       │ 3 submissions    │
│ Charlie Davis     │ 2 submissions    │
└──────────────────────────────────────┘
```

---

## 📄 Plagiarism Report

**URL**: `http://localhost:5000/report/<id>/<file>`

### Report Header:

```
╔════════════════════════════════════════════════════════════╗
║            📄 Plagiarism Detection Report                  ║
╚════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────┐
│                        85.3%                             │
│                Overall Similarity Score                   │
└──────────────────────────────────────────────────────────┘
                    (Red background)

┌─────────────────────┬─────────────────────────────────────┐
│ Student Name        │ John Smith                          │
│ Student ID          │ S001                                │
│ Document Name       │ essay_climate_change.docx           │
│ Submission Date     │ 2026-01-15 10:30:45                 │
│ Report Generated    │ 2026-01-15 10:31:20                 │
│ Total Matches Found │ 23                                  │
└─────────────────────┴─────────────────────────────────────┘

Color Legend:
🟢 0-20% (Low)  🟡 21-50% (Moderate)  🟠 51-80% (High)  🔴 81-100% (Very High)
```

### Charts Section:

```
┌────────────────────────────┬────────────────────────────┐
│  Similarity Distribution   │  Top Contributing Sources  │
│                            │                            │
│      (Pie Chart)           │      (Bar Chart)           │
│                            │                            │
│   ┌────────────────┐       │  Source 1 ▓▓▓▓▓▓▓ 45.2%   │
│   │     35%        │       │  Source 2 ▓▓▓▓▓ 28.1%     │
│   │                │       │  Source 3 ▓▓▓ 12.0%       │
│   │   65%          │       │                            │
│   └────────────────┘       │                            │
└────────────────────────────┴────────────────────────────┘
```

### Heatmap:

```
┌──────────────────────────────────────────────────────────┐
│         Plagiarism Heatmap Across Document               │
├──────────────────────────────────────────────────────────┤
│ ▓▓▓░░░░░░░▓▓▓▓▓▓░░░░░░░░░░▓▓▓▓▓░░░░░░░░░░░░░░░░        │
│ 0%   10%   20%   30%   40%   50%   60%   70%   80%  90% │
└──────────────────────────────────────────────────────────┘
Legend: ░ Low   ▒ Medium   ▓ High   █ Very High
```

### Highlighted Document:

```
┌──────────────────────────────────────────────────────────┐
│              Document Content (Highlighted)              │
├──────────────────────────────────────────────────────────┤
│                                                          │
│ Climate change represents one of the most significant   │
│ threats to global biodiversity. 🔴[Rising temperatures  │
│ and changing precipitation patterns are altering        │
│ ecosystems worldwide. Species are being forced to       │
│ adapt, migrate, or face extinction.]🔴 85%              │
│ Source: essay_environment.docx                          │
│                                                          │
│ The scientific community has reached consensus on       │
│ these issues. 🟡[Ocean acidification threatens marine   │
│ life significantly.]🟡 42% Source: ocean_study.pdf      │
│                                                          │
│ Conservation efforts must adapt to changing conditions. │
│ 🟢[New strategies are being developed.]🟢 15%           │
│ Source: conservation_report.docx                        │
│                                                          │
└──────────────────────────────────────────────────────────┘

[📥 Download Report]  [← Back to Submissions]
```

---

## 📱 Example Report Analysis

### Sample Scenario: High Similarity Case

**Student**: John Smith (S001)  
**Document**: essay_climate_change.docx  
**Overall Similarity**: 85.3%

#### Breakdown:

```
Source Distribution:
┌──────────────────────────────────────────┐
│ essay_environment.docx    │ 45.2%  ▓▓▓▓▓│
│ climate_paper.pdf         │ 28.1%  ▓▓▓▓ │
│ biodiversity_study.docx   │ 12.0%  ▓▓   │
└──────────────────────────────────────────┘

Matched Sections:
• Paragraph 1: 95% match with essay_environment.docx
• Paragraph 2: 88% match with climate_paper.pdf
• Paragraph 3: 72% match with essay_environment.docx
• Introduction: 45% match with biodiversity_study.docx

Conclusion: High plagiarism risk - requires investigation
```

### Sample Scenario: Low Similarity Case

**Student**: Bob Wilson (S003)  
**Document**: report.pdf  
**Overall Similarity**: 12.5%

#### Breakdown:

```
Source Distribution:
┌──────────────────────────────────────────┐
│ standard_template.docx    │ 8.0%   ▓    │
│ methodology_guide.pdf     │ 4.5%   ▓    │
└──────────────────────────────────────────┘

Matched Sections:
• Methodology section: 18% (standard procedures)
• References format: 12% (citation style)
• Common terminology: 8%

Conclusion: Acceptable similarity - likely common academic language
```

---

## 🎨 Color Coding Examples

### Visual Representation:

```
Similarity Level Examples:

🟢 GREEN (0-20% - Acceptable):
"The research methodology employed quantitative analysis."
└─ 15% match - Common academic language

🟡 YELLOW (21-50% - Review):
"The study examined the effects of climate change on biodiversity 
in coastal regions through a comprehensive literature review."
└─ 35% match - Moderate paraphrasing needed

🟠 ORANGE (51-80% - High Risk):
"Climate change represents one of the most significant environmental 
challenges of our time, threatening ecosystems and species diversity 
on a global scale through rising temperatures and altered precipitation."
└─ 68% match - Substantial similarity detected

🔴 RED (81-100% - Very High Risk):
"Rising temperatures and changing precipitation patterns are altering 
ecosystems worldwide. Species are being forced to adapt, migrate, or 
face extinction. The rapid pace of change exceeds the adaptive capacity 
of many organisms."
└─ 95% match - Direct copying detected
```

---

## 📈 Admin Analytics Examples

### Monthly Statistics Report:

```
═══════════════════════════════════════════════════════════
                MONTHLY STATISTICS REPORT
                     January 2026
═══════════════════════════════════════════════════════════

📊 OVERVIEW
├─ Total Submissions: 127
├─ Average Similarity: 28.5%
├─ High Risk Cases (>50%): 18 (14.2%)
└─ Unique Students: 85

📈 TRENDS
Submissions by Week:
Week 1: ▓▓▓▓▓▓▓▓▓▓ 25
Week 2: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 35
Week 3: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 42
Week 4: ▓▓▓▓▓▓▓▓▓ 25

⚠️ HIGH RISK CASES
1. S001 - John Smith    - 85.3%
2. S045 - Sarah Jones   - 78.2%
3. S089 - Mike Brown    - 72.5%
...

👥 TOP SUBMITTERS
1. Jane Doe (S002)      - 7 submissions
2. Bob Wilson (S003)    - 5 submissions
3. Alice Brown (S004)   - 5 submissions
...
═══════════════════════════════════════════════════════════
```

---

## 🔍 Investigation Workflow

### Step-by-Step Investigation Process:

```
┌──────────────────────────────────────────────────────────┐
│ HIGH SIMILARITY DETECTED: 85.3%                          │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 1: Review Overall Percentage                       │
│ • 85.3% = Very High (Red Zone)                          │
│ • Requires immediate attention                          │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 2: Check Source Distribution                       │
│ • Primary source: essay_environment.docx (45.2%)        │
│ • Multiple sources or single source?                    │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 3: Examine Highlighted Sections                    │
│ • Paragraph 1: 95% match - Direct copying              │
│ • Paragraph 2: 88% match - Minimal changes             │
│ • Review context and citations                          │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 4: Compare with Source Documents                   │
│ • View source: essay_environment.docx                   │
│ • Verify matches are accurate                           │
│ • Check for proper citations                            │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 5: Make Decision                                   │
│ Options:                                                │
│ ✓ Academic integrity violation                          │
│ ✓ Request revision                                      │
│ ✓ Educational discussion                                │
│ ✗ False positive (if applicable)                        │
└──────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ STEP 6: Document and Follow Up                          │
│ • Download report for records                           │
│ • Contact student                                       │
│ • Follow institutional procedures                       │
└──────────────────────────────────────────────────────────┘
```

---

## 📋 Quick Reference Guide

### Common Tasks:

```
┌─────────────────────────────────────────────────────────┐
│ TASK                    │ STEPS                         │
├─────────────────────────┼───────────────────────────────┤
│ Upload document         │ Upload → Fill form → Submit   │
│ View report             │ Submissions → Click View      │
│ Download report         │ Report page → Download button │
│ Check statistics        │ Admin → View dashboard        │
│ Delete submission       │ Admin → Find → Delete         │
│ Find high similarity    │ Admin → Sort by similarity    │
│ View student history    │ Submissions → Filter by ID    │
│ Generate monthly report │ Admin → Export statistics     │
└─────────────────────────┴───────────────────────────────┘
```

### Keyboard Shortcuts:

```
┌─────────────────────────────────────────────────────────┐
│ ACTION                  │ SHORTCUT                      │
├─────────────────────────┼───────────────────────────────┤
│ Go to Home              │ Ctrl/Cmd + H                  │
│ Go to Upload            │ Ctrl/Cmd + U                  │
│ Go to Submissions       │ Ctrl/Cmd + S                  │
│ Go to Admin             │ Ctrl/Cmd + A                  │
│ Download current report │ Ctrl/Cmd + D                  │
└─────────────────────────┴───────────────────────────────┘
```

---

**This visual guide demonstrates the complete user interface and workflow of the Plagiarism Detection System.**

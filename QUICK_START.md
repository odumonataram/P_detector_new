# Quick Start Guide - Plagiarism Detection System

## ⚡ Quick Setup (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download NLTK Data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Step 3: Create Sample Documents (Optional)
```bash
python create_samples.py
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
```
http://localhost:5000
```

## 🎯 First-Time Usage

### Test the System:

1. **Go to Upload Page**
   - Click "Upload" in navigation
   - Enter: Student Name = "John Doe"
   - Enter: Student ID = "S001"
   - Select a PDF or DOCX file
   - Click "Upload and Check Plagiarism"

2. **View Results**
   - System will process and redirect to report
   - Check overall similarity percentage
   - View highlighted sections
   - Download report as HTML

3. **Try Admin Dashboard**
   - Click "Admin" in navigation
   - View statistics
   - Monitor submissions

## 📝 Testing Plagiarism Detection

To see the system in action:

1. **Upload First Document** (Original)
   - Upload any document as "Student 1"
   - Result: 0% similarity (no prior documents)

2. **Upload Similar Document** (Test)
   - Upload a document with similar content as "Student 2"
   - Result: Will show similarity percentage and highlights

3. **Upload Different Document** (Control)
   - Upload completely different content as "Student 3"
   - Result: Low or 0% similarity

## 🎨 Understanding the Report

### Color Codes:
- 🟢 **Green (0-20%)**: Good - Acceptable similarity
- 🟡 **Yellow (21-50%)**: Caution - Review recommended
- 🟠 **Orange (51-80%)**: Warning - Investigation needed
- 🔴 **Red (81-100%)**: Alert - Likely plagiarism

### Report Sections:
1. **Overall Similarity Box**: Shows total similarity percentage
2. **Metadata**: Student info and submission details
3. **Charts**: Visual representation of sources
4. **Highlighted Document**: Full text with color-coded matches

## 🔧 Troubleshooting

**Problem**: "ModuleNotFoundError"
**Solution**: `pip install -r requirements.txt`

**Problem**: "NLTK data not found"
**Solution**: `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`

**Problem**: "Port 5000 already in use"
**Solution**: Change port in app.py: `app.run(port=5001)`

**Problem**: "File not uploading"
**Solution**: Check file size (<16MB) and format (PDF/DOCX)

## 📱 Using Sample Documents

If you created sample documents:

1. Navigate to `sample_documents/` folder
2. Upload `sample_doc1_original.docx` first
3. Then upload `sample_doc2_partial.docx`
4. Observe plagiarism detection results!

## 🚀 Production Tips

- Set `debug=False` in app.py for production
- Change `SECRET_KEY` in config.py
- Regularly backup `storage/submissions_index.json`
- Monitor `storage/` folder size
- Review and delete old submissions periodically

## 📞 Need Help?

- Check README.md for detailed documentation
- Review code comments for technical details
- Test with sample documents first
- Verify all dependencies are installed

---

**Ready to start? Just run:** `python app.py` 🎉

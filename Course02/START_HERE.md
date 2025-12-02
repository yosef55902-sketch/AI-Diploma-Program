# 🎓 START HERE - Welcome Students! | ابدأ من هنا - مرحباً بالطلاب!

## 👋 Welcome to Python for AI Course | مرحباً بك في دورة بايثون للذكاء الاصطناعي

**If you're a new student, READ THIS FIRST!**  
**إذا كنت طالباً جديداً، اقرأ هذا أولاً!**

This file tells you exactly what to do on **Day 1** and how to navigate this course.  
هذا الملف يخبرك بالضبط ماذا تفعل في **اليوم الأول** وكيف تتنقل في هذه الدورة.

---

## ✅ Day 1 Checklist | قائمة اليوم الأول

Follow these steps in order. Don't skip any!  
اتبع هذه الخطوات بالترتيب. لا تتخطى أي خطوة!

### Step 1: Check Prerequisites | الخطوة 1: تحقق من المتطلبات الأساسية

**Before starting this course, you should have completed:**

- [ ] **Python Essentials - Part 1 (Basics)**: Variables, data types, lists, dictionaries, loops
- [ ] **Python Essentials - Part 2 (Intermediate)**: Functions, classes, modules, file handling

**Links:**
- [Python Essentials - Part 1](https://edube.org/study/pe1)
- [Python Essentials - Part 2](https://edube.org/study/pe2)

**If you haven't completed these courses:**  
⚠️ You will struggle with this course. Complete them first!

---

### Step 2: Check Python Version | الخطوة 2: تحقق من إصدار بايثون

Open your terminal/command prompt and type:

```bash
python --version
```

**You need:** Python 3.9 or higher (3.10 or 3.11 recommended)

**If you don't have Python or have an old version:**  
Install Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/)

---

### Step 3: Install Libraries | الخطوة 3: تثبيت المكتبات

**Follow the installation guide:** Open `DOCS/INSTALLATION_GUIDE.md` and follow the instructions.

**Quick method (if you're comfortable with terminal):**

```bash
# 1. Create virtual environment (recommended)
python -m venv venv

# 2. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install all libraries
pip install -r ../requirements.txt

# 5. Verify installation
pip check
```

**If you see errors:** Read `DOCS/INSTALLATION_GUIDE.md` for troubleshooting.

---

### Step 4: Read the Course Overview | الخطوة 4: اقرأ نظرة عامة على الدورة

**Open and read:** `README.md`

This file explains:
- What this course covers
- The learning path
- What each notebook teaches
- How notebooks connect to each other

**Don't skip this!** It's only 5-10 minutes to read and will save you hours of confusion later.

---

### Step 5: Start with Notebook 00 | الخطوة 5: ابدأ بالدفتر 00

**Open:** `NOTEBOOKS/00_Python_Libraries_for_AI.ipynb`

**Why this notebook FIRST?**
- All other notebooks use Python libraries (NumPy, Matplotlib, etc.)
- You need to learn these libraries BEFORE learning AI concepts
- This notebook teaches you the tools you'll use in all other notebooks

**Don't jump ahead to Notebook 01!** You'll be confused without the library knowledge.

---

## 📚 Learning Sequence | تسلسل التعلم

**Follow this exact order:**

```
1. ✅ Complete Prerequisites (Python PE1 & PE2)
   ↓
2. ✅ Install Libraries (Step 3 above)
   ↓
3. 📓 Notebook 00: Python Libraries for AI
   ↓
4. 📓 Notebook 01: Introduction & Search Algorithms
   ↓
5. 📓 Notebook 02: Knowledge Representation
   ↓
6. 📓 Notebook 03: Learning under Uncertainty
   ↓
7. 📓 Notebook 04: Optimization Techniques
   ↓
8. 📓 Notebook 05: AI-based Learning Models
```

**Important:** Each notebook builds on the previous one. Don't skip notebooks!

---

## 📋 Progress Tracker | متتبع التقدم

Use this checklist to track your progress:

### Setup & Preparation
- [ ] Completed Python PE1 & PE2 prerequisites
- [ ] Python 3.9+ installed and verified
- [ ] Libraries installed successfully (`pip check` shows no errors)
- [ ] Read README.md
- [ ] Read this START_HERE.md file

### Notebooks
- [ ] **Notebook 00**: Python Libraries for AI
- [ ] **Notebook 01**: Introduction & Search Algorithms
- [ ] **Notebook 02**: Knowledge Representation
- [ ] **Notebook 03**: Learning under Uncertainty
- [ ] **Notebook 04**: Optimization Techniques
- [ ] **Notebook 05**: AI-based Learning Models

---

## 🆘 Need Help? | تحتاج مساعدة؟

### Common Issues:

**Problem:** "No module named 'numpy'"  
**Solution:** You haven't installed libraries. Go back to Step 3.

**Problem:** "Python version too old"  
**Solution:** Install Python 3.10 or 3.11 from python.org

**Problem:** "I don't understand the notebook"  
**Solution:** 
1. Check if you completed prerequisites (Step 1)
2. Make sure you're doing notebooks in order (00 → 01 → 02...)
3. Read the prerequisites section at the top of each notebook

**Problem:** "Libraries conflict with each other"  
**Solution:** Use virtual environment (see `DOCS/INSTALLATION_GUIDE.md`)

---

## 📖 File Guide | دليل الملفات

**What each file is for:**

| File | Purpose | When to Use |
|------|---------|-------------|
| `START_HERE.md` | **This file** - First thing to read | **Day 1, before anything else** |
| `README.md` | Course overview and structure | After reading START_HERE |
| `DOCS/INSTALLATION_GUIDE.md` | Detailed installation instructions | When installing libraries |
| `../requirements.txt` | List of libraries to install | During installation (Step 3) |
| `NOTEBOOKS/00_Python_Libraries_for_AI.ipynb` | Learn Python libraries | **First notebook to open** |
| `NOTEBOOKS/01_Introduction_Search_Algorithms.ipynb` | Search algorithms | After completing Notebook 00 |
| `NOTEBOOKS/02_Knowledge_Representation.ipynb` | Knowledge systems | After completing Notebook 01 |
| `NOTEBOOKS/03_Learning_Under_Uncertainty.ipynb` | Probability & uncertainty | After completing Notebook 02 |
| `NOTEBOOKS/04_Optimization_Techniques.ipynb` | Optimization methods | After completing Notebook 03 |
| `NOTEBOOKS/05_AI_Learning_Models.ipynb` | Machine learning models | After completing Notebook 04 |

---

## 🎯 Quick Start Summary | ملخص البدء السريع

**For students who want the shortest path:**

1. ✅ Check prerequisites (Python PE1 & PE2 completed)
2. ✅ Install Python 3.10+ if needed
3. ✅ Install libraries: `pip install -r ../requirements.txt`
4. ✅ Read `README.md` (5 minutes)
5. ✅ Open `00_Python_Libraries_for_AI.ipynb` and start learning!

**That's it!** Everything else is in the notebooks.

---

## 💡 Tips for Success | نصائح للنجاح

1. **Don't rush:** Each notebook builds on the previous one
2. **Practice:** Try modifying the code examples
3. **Ask questions:** If something is unclear, ask your instructor
4. **Take notes:** Write down concepts you find difficult
5. **Review:** Before starting a new notebook, review the previous one

---

## ✅ Ready to Start? | جاهز للبدء؟

If you've completed all steps above, you're ready!

**Next action:** Open `NOTEBOOKS/00_Python_Libraries_for_AI.ipynb` and begin your AI journey!

**Good luck!** 🚀  
**حظاً موفقاً!** 🚀

---

**Last Updated:** 2025  
**Course:** Python for AI - 112 AIAT  
**Language Support:** Arabic & English


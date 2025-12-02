# 🎓 START HERE - Welcome Students! | ابدأ من هنا - مرحباً بالطلاب!

## 👋 Welcome to Ethics of Artificial Intelligence Course | مرحباً بك في دورة أخلاقيات الذكاء الاصطناعي

**If you're a new student, READ THIS FIRST!**  
**إذا كنت طالباً جديداً، اقرأ هذا أولاً!**

This file tells you exactly what to do on **Day 1** and how to navigate this course.  
هذا الملف يخبرك بالضبط ماذا تفعل في **اليوم الأول** وكيف تتنقل في هذه الدورة.

---

## ✅ Day 1 Checklist | قائمة اليوم الأول

Follow these steps in order. Don't skip any!  
اتبع هذه الخطوات بالترتيب. لا تتخطى أي خطوة!

### Step 1: Check Prerequisites | الخطوة 1: تحقق من المتطلبات الأساسية

**Before starting this course, you should have:**

- [ ] **Python 3.8 or higher** installed on your computer
- [ ] **Basic Python programming knowledge**: Variables, data types, functions, classes
- [ ] **Understanding of AI/ML concepts** (helpful but not required)
- [ ] **Interest in ethical considerations** of technology

**Check Python version:**
```bash
python --version
```

**You need:** Python 3.8 or higher (3.10 or 3.11 recommended)

**If you don't have Python or have an old version:**  
Install Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/)

---

### Step 2: Install Libraries | الخطوة 2: تثبيت المكتبات

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

### Step 3: Read the Course Overview | الخطوة 3: اقرأ نظرة عامة على الدورة

**Open and read:** `README.md`

This file explains:
- What this course covers
- The learning path through 5 units
- What each unit teaches
- How units connect to each other

**Don't skip this!** It's only 5-10 minutes to read and will save you hours of confusion later.

---

### Step 4: Start with Unit 1 | الخطوة 4: ابدأ بالوحدة 1

**Open:** `unit1-ethics-foundations/README.md`

**Why this unit FIRST?**
- Establishes foundational ethical principles
- Introduces key ethical frameworks
- Provides context for all other units
- You need to understand ethics foundations BEFORE analyzing specific AI ethics issues

**Then start with:** `unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb`

**Don't jump ahead to other units!** Each unit builds on the previous one.

---

## 📚 Learning Sequence | تسلسل التعلم

**Follow this exact order:**

```
1. ✅ Check Prerequisites (Python 3.8+)
   ↓
2. ✅ Install Libraries (Step 2 above)
   ↓
3. 📓 Unit 1: Foundations of AI Ethics
   ↓
4. 📓 Unit 2: Bias, Justice, and Discrimination
   ↓
5. 📓 Unit 3: Privacy and Security
   ↓
6. 📓 Unit 4: Transparency and Accountability
   ↓
7. 📓 Unit 5: Governance and Regulations
```

**Important:** Each unit builds on the previous one. Don't skip units!

---

## 📋 Progress Tracker | متتبع التقدم

Use this checklist to track your progress:

### Setup & Preparation
- [ ] Python 3.8+ installed and verified
- [ ] Libraries installed successfully (`pip check` shows no errors)
- [ ] Read README.md
- [ ] Read this START_HERE.md file

### Units
- [ ] **Unit 1**: Foundations of AI Ethics
- [ ] **Unit 2**: Bias, Justice, and Discrimination
- [ ] **Unit 3**: Privacy and Security
- [ ] **Unit 4**: Transparency and Accountability
- [ ] **Unit 5**: Governance and Regulations

**For detailed progress tracking, use:** `STUDENT_PROGRESS_CHECKLIST.md`

---

## 🆘 Need Help? | تحتاج مساعدة?

### Common Issues:

**Problem:** "No module named 'pandas'" or "No module named 'fairlearn'"  
**Solution:** You haven't installed libraries. Go back to Step 2.

**Problem:** "Python version too old"  
**Solution:** Install Python 3.10 or 3.11 from python.org

**Problem:** "I don't understand the notebook"  
**Solution:** 
1. Check if you have Python basics knowledge
2. Make sure you're doing units in order (1 → 2 → 3...)
3. Read the README.md in each unit folder

**Problem:** "Libraries conflict with each other"  
**Solution:** Use virtual environment (see Step 2)

---

## 📖 File Guide | دليل الملفات

**What each file/folder is for:**

| File/Folder | Purpose | When to Use |
|-------------|---------|-------------|
| `START_HERE.md` | **This file** - First thing to read | **Day 1, before anything else** |
| `README.md` | Course overview and structure | After reading START_HERE |
| `STUDENT_PROGRESS_CHECKLIST.md` | Track your progress | Throughout the course |
| `../requirements.txt` | List of libraries to install | During installation (Step 2) |
| `unit1-ethics-foundations/README.md` | Unit 1 overview | Before starting Unit 1 |
| `unit2-bias-justice/` | Unit 2 materials | After completing Unit 1 |
| `unit3-privacy-security/` | Unit 3 materials | After completing Unit 2 |
| `unit4-transparency-accountability/` | Unit 4 materials | After completing Unit 3 |
| `unit5-governance-regulations/` | Unit 5 materials | After completing Unit 4 |
| `DOCS/` | Documentation and guides | When you need help |

---

## 🎯 Quick Start Summary | ملخص البدء السريع

**For students who want the shortest path:**

1. ✅ Check Python version (3.8+)
2. ✅ Install Python 3.10+ if needed
3. ✅ Install libraries: `pip install -r ../requirements.txt`
4. ✅ Read `README.md` (5 minutes)
5. ✅ Open `unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb` and start learning!

**That's it!** Everything else is in the unit folders.

---

## 💡 Tips for Success | نصائح للنجاح

1. **Don't rush:** Each unit builds on the previous one
2. **Think critically:** Ethics requires careful consideration
3. **Read case studies:** Real-world examples help understanding
4. **Practice:** Complete all exercises in each unit
5. **Discuss:** Ethics benefits from discussion and different perspectives

---

## ✅ Ready to Start? | جاهز للبدء؟

If you've completed all steps above, you're ready!

**Next action:** Open `unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb` and begin your AI ethics journey!

**Good luck!** 🚀  
**حظاً موفقاً!** 🚀

---

**Last Updated:** 2025  
**Course:** AIAT 116 - Ethics of Artificial Intelligence  
**Language Support:** Arabic & English


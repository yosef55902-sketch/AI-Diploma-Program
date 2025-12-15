# Frequently Asked Questions (FAQ) | الأسئلة الشائعة

Common questions and answers for students and instructors.

---

## General Questions | الأسئلة العامة

### Q1: What is this course about?
**A:** This course teaches Python programming with a focus on AI applications. You'll learn how to use Python libraries to implement AI concepts like search algorithms, knowledge representation, machine learning, and more.

---

### Q2: Do I need prior programming experience?
**A:** Yes, you should complete Python Essentials Part 1 and Part 2 before starting this course. You need to understand:
- Variables, data types, lists, dictionaries
- Functions, classes, modules
- Basic Python syntax

---

### Q3: What Python version do I need?
**A:** Python 3.9 or higher (3.10 or 3.11 recommended). Check your version:
```bash
python --version
```

---

### Q4: How long does the course take?
**A:** The course is designed for 12 weeks with 6-8 hours per week. See `COURSE_SCHEDULE.md` for detailed timeline.

---

## Installation & Setup | التثبيت والإعداد

### Q5: How do I install the required libraries?
**A:** Follow `DOCS/INSTALLATION_GUIDE.md`. Quick method:
```bash
pip install -r ../../requirements.txt
```

---

### Q6: Should I use a virtual environment?
**A:** Yes, it's highly recommended! Virtual environments prevent conflicts with other Python projects. See `INSTALLATION_GUIDE.md` for instructions.

---

### Q7: I'm getting "No module named 'numpy'" error. What should I do?
**A:** 
1. Make sure you installed libraries: `pip install -r ../../requirements.txt`
2. Check if you're in the correct virtual environment
3. Verify installation: `python TESTING/verify_installation.py`

---

### Q8: Libraries are conflicting. How do I fix this?
**A:** 
1. Use a virtual environment (see DOCS/INSTALLATION_GUIDE.md)
2. Use the exact versions in `requirements.txt`
3. Run `pip check` to identify conflicts
4. Reinstall: `pip install --upgrade --force-reinstall -r requirements.txt`

---

### Q9: How do I verify my installation?
**A:** Run the verification script:
```bash
python TESTING/verify_installation.py
```
Or check manually:
```bash
pip check
```
Or manually check:
```bash
pip check
```

---

## Course Content | محتوى الدورة

### Q10: Which notebook should I start with?
**A:** Always start with `NOTEBOOKS/00_Python_Libraries_for_AI.ipynb`. It teaches the libraries you'll need for all other notebooks. Don't skip it!

---

### Q11: Can I skip notebooks?
**A:** No! Each notebook builds on the previous one. Skipping will cause confusion later. Follow the sequence: 00 → 01 → 02 → 03 → 04 → 05

---

### Q12: How long does each notebook take?
**A:** Typically 2-3 hours of study time, plus 1-2 hours for practice exercises. Don't rush - understanding is more important than speed.

---

### Q13: What if I don't understand a concept?
**A:** 
1. Review the prerequisites section in the notebook
2. Go back to previous notebooks if needed
3. Check `ADDITIONAL_RESOURCES.md` for videos/explanations
4. Ask your instructor during office hours
5. Practice with exercises in `PRACTICE_PROBLEMS.md`

---

### Q14: Are there solutions to exercises?
**A:** Solutions structure is in `SOLUTIONS/` folder. Try exercises yourself first, then check solutions. Remember: understanding is more important than copying!

---

## Assessment & Grading | التقييم والدرجات

### Q15: How is the course graded?
**A:** 
- Quizzes (60%): 6 quizzes, 5-15% each
- Project (30%): One project from Weeks 7-8
- Participation (10%): Class participation, questions, helping others

---

### Q16: When are quizzes?
**A:** After completing each notebook (see `COURSE_SCHEDULE.md`):
- Week 1: Quiz 00
- Week 2: Quiz 01
- Week 3: Quiz 02
- Week 4: Quiz 03
- Week 5: Quiz 04
- Week 6: Quiz 05

---

### Q17: What if I fail a quiz?
**A:** 
1. Review the notebook again
2. Practice with exercises
3. Ask instructor for help
4. Some courses allow retakes - check with your instructor

---

### Q18: How do I choose a project?
**A:** 
1. Review all 3 project descriptions in `PROJECTS/` folder
2. Consider your interests and skill level
3. Check prerequisites for each project
4. Discuss with instructor if unsure

---

### Q19: Can I work on projects in groups?
**A:** Check with your instructor. Some courses allow group work, others require individual projects.

---

## Technical Questions | الأسئلة التقنية

### Q20: My code doesn't work. What should I do?
**A:** 
1. Read the error message carefully
2. Check for typos (common mistake!)
3. Verify you imported required libraries
4. Check indentation (Python is sensitive to this)
5. Use print statements to debug
6. Ask instructor or classmates for help

---

### Q21: Jupyter Notebook won't start. What's wrong?
**A:** 
1. Make sure Jupyter is installed: `pip install jupyter`
2. Start from terminal: `jupyter notebook`
3. Check if port is already in use
4. Try: `jupyter notebook --port 8889`

---

### Q22: How do I save my work?
**A:** 
- Jupyter Notebooks auto-save, but you can also:
  - File → Save and Checkpoint
  - Use Git for version control (recommended)
  - Export as PDF or HTML for backup

---

### Q23: Can I use Google Colab instead of local Jupyter?
**A:** Yes! Google Colab works well. Just make sure to:
- Install libraries in each session
- Save your work regularly
- Download notebooks for backup

---

## Resources & Help | الموارد والمساعدة

### Q24: Where can I get more help?
**A:** 
- Check `DOCS/ADDITIONAL_RESOURCES.md` for videos, tutorials
- Ask instructor during office hours
- Post questions in course forum (if available)
- Check Stack Overflow for coding questions
- Review official documentation

---

### Q25: What if I'm falling behind?
**A:** 
1. Don't panic - many students face this
2. Identify specific gaps
3. Create a catch-up plan
4. Ask instructor for help
5. Consider extending deadlines (check with instructor)

---

### Q26: Are there practice problems?
**A:** Yes! Check `DOCS/PRACTICE_PROBLEMS.md` for 18+ additional problems organized by topic and difficulty level.

---

## Projects | المشاريع

### Q27: When do projects start?
**A:** Projects start in Week 7. You'll have 2 weeks (Weeks 7-8) to complete your project.

---

### Q28: Can I use project templates?
**A:** Yes! Templates are in `PROJECTS/Project_Templates/`. They provide starter code and structure. Fill in the TODO sections.

---

### Q29: How is the project graded?
**A:** See `ASSESSMENTS/Project_Rubric.md`. Projects are evaluated on:
- Functionality (40%)
- Code Quality (20%)
- Documentation (15%)
- Testing (10%)
- Creativity (15%)

---

### Q30: What if I can't finish my project on time?
**A:** 
1. Contact instructor immediately
2. Explain the situation
3. Some instructors allow extensions with valid reasons
4. Partial credit may be available for completed parts

---

## Course Completion | إتمام الدورة

### Q31: What do I get after completing the course?
**A:** 
- Certificate of completion (if provided by institution)
- Portfolio of projects
- Knowledge and skills in Python for AI
- Foundation for advanced AI topics

---

### Q32: What can I do after this course?
**A:** 
- Take advanced AI/ML courses
- Work on personal AI projects
- Apply for AI-related jobs
- Continue learning (deep learning, NLP, computer vision)

---

## For Instructors | للمدرسين

### Q33: How do I use the assessment materials?
**A:** 
- Quizzes: Administer after each notebook, use answer keys provided
- Projects: Use `ASSESSMENTS/Project_Rubric.md` for evaluation
- See `INSTRUCTOR_GUIDE.md` for detailed guidance

---

### Q34: Can I modify the course content?
**A:** Yes, you can customize:
- Schedule (see `COURSE_SCHEDULE.md` for options)
- Assessment weights
- Project requirements
- Additional topics

---

### Q35: How do I handle students with different skill levels?
**A:** 
- Provide additional resources for struggling students
- Offer advanced challenges for strong students
- Use office hours for individual help
- Consider grouping students by level

---

## Still Have Questions? | لا تزال لديك أسئلة؟

**Contact:**
- Your course instructor
- Course forum (if available)
- Check `ADDITIONAL_RESOURCES.md` for more help

**Remember:** No question is too basic. Asking questions helps you learn!

---

**Last Updated**: 2025  
**For**: Python for AI Course - 112 AIAT


# Installation Guide | دليل التثبيت

## ⚠️ IMPORTANT: Avoid Library Conflicts | مهم: تجنب تعارض المكتبات

This guide ensures you install all libraries **without conflicts** that could cause errors.

---

## ✅ Recommended: Use Virtual Environment | بيئة افتراضية (موصى بها)

**WHY?** Virtual environments prevent conflicts with other Python projects on your computer.

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Libraries

```bash
pip install --upgrade pip
pip install -r ../../requirements.txt
```

### Step 3: Verify Installation

**Quick check:**
```bash
pip check
```
If you see "No broken requirements found", you're good! ✅

**Detailed check (recommended):**
```bash
python TESTING/verify_installation.py
```
This tests all libraries work together and reports any issues.

---

## 🔄 Alternative: Install Without Virtual Environment

**WARNING**: Only if you don't have other Python projects.

```bash
pip install --upgrade pip
pip install -r ../../requirements.txt
pip check  # Verify no conflicts
python TESTING/verify_installation.py  # Test all libraries
```

---

## 📋 Manual Installation (If Needed)

If `../../requirements.txt` causes issues, install in this order:

```bash
# 1. Core libraries first
pip install numpy>=1.24.0
pip install scipy>=1.10.0

# 2. Visualization
pip install matplotlib>=3.7.0
pip install seaborn>=0.12.0

# 3. Machine Learning
pip install scikit-learn>=1.3.0

# 4. Graph operations
pip install networkx>=3.0

# 5. Data manipulation
pip install pandas>=2.0.0

# 6. Jupyter support
pip install jupyter notebook ipykernel
```

---

## ⚠️ Known Compatibility Notes | ملاحظات التوافق

### ✅ Compatible Versions:
- **Python 3.9, 3.10, 3.11**: All supported
- **NumPy 1.24+**: Works with all other libraries
- **SciPy 1.10+**: Requires NumPy 1.21+
- **Matplotlib 3.7+**: Compatible with NumPy 1.24+
- **Scikit-learn 1.3+**: Requires NumPy 1.17+, SciPy 1.3+
- **NetworkX 3.0+**: Compatible with all versions

### ❌ Potential Conflicts:
1. **NumPy < 1.21**: Won't work with SciPy 1.10+
2. **Old scikit-learn**: May conflict with new NumPy
3. **Python < 3.9**: Some libraries don't support older Python

### ✅ Solution:
Use versions in `../../requirements.txt` - they're all tested together!

---

## 🐛 Troubleshooting | حل المشاكل

### Problem 1: "No module named 'numpy'"
**Solution**: Install NumPy first:
```bash
pip install numpy
```

### Problem 2: "Cannot import name 'X' from 'scipy'"
**Solution**: Upgrade SciPy:
```bash
pip install --upgrade scipy
```

### Problem 3: "ImportError: cannot import name 'X' from 'sklearn'"
**Solution**: Upgrade scikit-learn:
```bash
pip install --upgrade scikit-learn
```

### Problem 4: Multiple version conflicts
**Solution**: Use virtual environment (see above) or:
```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### Problem 5: NetworkX not found
**Solution**: 
```bash
pip install networkx matplotlib
```

---

## ✅ Verify Installation | التحقق من التثبيت

### Method 1: Using pip check (Quick Check)

```bash
pip check
```

If you see "No broken requirements found", you're good! ✅

---

### Method 2: Using verify_installation.py (Detailed Check)

Run the verification script:

```bash
python TESTING/verify_installation.py
```

**OR** on some systems:

```bash
python3 TESTING/verify_installation.py
```

This script will:
- ✅ Check all libraries are installed
- ✅ Verify versions are compatible
- ✅ Test imports to ensure no conflicts
- ✅ Report any missing libraries

---

### Method 3: Manual Python Code (Alternative)

Run this Python code to verify all libraries work:

```python
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sklearn
import networkx as nx
import pandas as pd
import seaborn as sns

print("✅ All libraries imported successfully!")
print(f"NumPy version: {np.__version__}")
print(f"SciPy version: {scipy.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")
print(f"NetworkX version: {nx.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Seaborn version: {sns.__version__}")
```

---

## 📚 Installation Order Matters | ترتيب التثبيت مهم

**Correct order** (prevents conflicts):
1. NumPy (base for everything)
2. SciPy (depends on NumPy)
3. Matplotlib (works with NumPy)
4. Scikit-learn (depends on NumPy + SciPy)
5. NetworkX, Pandas, Seaborn (independent)

**Why?** Some libraries depend on others - install dependencies first!

---

## 🎯 Quick Start | البدء السريع

**Easiest method (recommended):**

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows

# 2. Install everything
pip install --upgrade pip
pip install -r ../../requirements.txt

# 3. Verify installation
pip check  # Quick check for conflicts
python TESTING/verify_installation.py  # Detailed verification

# 4. Start Jupyter
jupyter notebook
```

**What these commands do:**
- `pip install -r ../../requirements.txt`: Installs all libraries with compatible versions
- `pip check`: Quick check for conflicts between libraries
- `python TESTING/verify_installation.py`: Detailed check - tests all libraries work together

---

## 💡 Tips | نصائح

1. **Always use virtual environment** for Python projects
2. **Use `pip check`** after installation to find conflicts
3. **Keep pip updated**: `pip install --upgrade pip`
4. **If conflicts occur**: Use virtual environment and reinstall
5. **Don't mix installations**: Either use ../../requirements.txt OR manual, not both

---

## 📞 Need Help? | تحتاج مساعدة؟

If you encounter issues:
1. Check Python version: `python --version` (should be 3.9+)
2. Run `pip check` to see conflicts
3. Try virtual environment (see above)
4. Check error messages - they often tell you what's missing

---

**Last Updated**: 2025
**Tested on**: Python 3.9, 3.10, 3.11 | Windows, macOS, Linux


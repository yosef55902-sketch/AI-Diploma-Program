# Complete Project Guide: 02 Classification System
## دليل المشروع الكامل

---

## 🎯 Real-World Application | التطبيق في الحياة الواقعية

---

## 🚀 Quick Start (For Experienced Students)
## البدء السريع (للطلاب ذوي الخبرة)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation | التنفيذ خطوة بخطوة

---

## 📚 Complete Tutorial (For Beginners)
## دليل كامل للمبتدئين

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Classification (Day 1)

**What is Classification?**
Predicting which category something belongs to:
- Email → Spam or Not Spam?
- Image → Cat, Dog, or Bird?
- Customer → Will Buy or Won't Buy?

**Example:**
```
Email features:
- Has "FREE" in subject → Likely spam
- From known sender → Likely not spam
- Has links → Could be spam
- Short message → Could be spam

Classification: Spam (95% confidence)
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
classification_project/
├── data/
│   └── emails.csv
├── src/
│   ├── data_loader.py
│   ├── classifier.py
│   └── evaluator.py
├── models/
├── results/
├── main.py
└── README.md
```

**Install:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### Step 3: Load and Explore Data (Day 2)

**File: `src/data_loader.py`**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def load_data(self, filepath):
        """Load classification dataset"""
        df = pd.read_csv(filepath)
        print(f"✅ Loaded {len(df)} samples")
        return df
    
    def prepare_data(self, df, target_column):
        """Prepare features and target"""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"✅ Train: {len(X_train)}, Test: {len(X_test)}")
        return X_train, X_test, y_train, y_test
```

---

### Step 4: Implement Classifiers (Day 3)

**File: `src/classifier.py`**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class ClassifierSystem:
    """Multiple classification algorithms"""
    
    def __init__(self):
        self.models = {}
    
    def train_all(self, X_train, y_train):
        """Train all classifiers"""
        
        # 1. Logistic Regression
        lr = LogisticRegression(random_state=42, max_iter=1000)
        lr.fit(X_train, y_train)
        self.models['Logistic Regression'] = lr
        
        # 2. Decision Tree
        dt = DecisionTreeClassifier(random_state=42)
        dt.fit(X_train, y_train)
        self.models['Decision Tree'] = dt
        
        # 3. SVM
        svm = SVC(random_state=42, probability=True)
        svm.fit(X_train, y_train)
        self.models['SVM'] = svm
        
        # 4. Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        self.models['Random Forest'] = rf
        
        print("✅ Trained all models")
        return self.models
```

---

### Step 5: Evaluate Models (Day 4)

**File: `src/evaluator.py`**

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    """Evaluate classification models"""
    
    def evaluate_all(self, models, X_test, y_test):
        """Evaluate all models"""
        results = {}
        
        for name, model in models.items():
            y_pred = model.predict(X_test)
            
            results[name] = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, average='weighted'),
                'recall': recall_score(y_test, y_pred, average='weighted'),
                'f1': f1_score(y_test, y_pred, average='weighted')
            }
            
            print(f"\n{name}:")
            print(f"  Accuracy: {results[name]['accuracy']:.4f}")
            print(f"  Precision: {results[name]['precision']:.4f}")
            print(f"  Recall: {results[name]['recall']:.4f}")
            print(f"  F1-Score: {results[name]['f1']:.4f}")
        
        return results
    
    def plot_confusion_matrix(self, model, X_test, y_test, name):
        """Plot confusion matrix"""
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix - {name}')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig(f'results/confusion_matrix_{name}.png')
        plt.close()
```

---

### Step 6: Compare Models (Day 5)

**File: `main.py`**

```python
from src.data_loader import DataLoader
from src.classifier import ClassifierSystem
from src.evaluator import ModelEvaluator

def main():
    # Load data
    loader = DataLoader()
    df = loader.load_data('data/emails.csv')
    
    # Prepare data
    X_train, X_test, y_train, y_test = loader.prepare_data(df, 'label')
    
    # Train models
    classifier = ClassifierSystem()
    models = classifier.train_all(X_train, y_train)
    
    # Evaluate
    evaluator = ModelEvaluator()
    results = evaluator.evaluate_all(models, X_test, y_test)
    
    # Find best model
    best_model = max(results, key=lambda x: results[x]['f1'])
    print(f"\n✅ Best model: {best_model}")
    
    # Plot confusion matrices
    for name, model in models.items():
        evaluator.plot_confusion_matrix(model, X_test, y_test, name)

if __name__ == "__main__":
    main()
```

---

---

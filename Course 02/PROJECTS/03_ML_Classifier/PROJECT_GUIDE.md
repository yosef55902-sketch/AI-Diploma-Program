# Complete Project Guide: 03 Ml Classifier
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
- Customer → Will Cancel or Stay?
- Email → Spam or Not Spam?
- Image → Cat or Dog?
- Transaction → Fraud or Legitimate?

**Example:**
```
Customer Features:
- Subscription length: 6 months
- Usage frequency: Low
- Payment issues: Yes
- Support tickets: 3

Prediction: Will Cancel (85% confidence)
Action: Send retention offer
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
ml_classifier/
├── data/
│   └── customer_data.csv
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── classifier.py
│   └── evaluator.py
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
import matplotlib.pyplot as plt
import seaborn as sns

class DataLoader:
    def load_data(self, filepath):
        """Load classification dataset"""
        df = pd.read_csv(filepath)
        print(f"✅ Loaded {len(df)} samples, {len(df.columns)} features")
        return df
    
    def explore_data(self, df):
        """Explore the dataset"""
        print("\n" + "=" * 50)
        print("Data Overview")
        print("=" * 50)
        
        # Basic info
        print(f"\nShape: {df.shape}")
        print(f"\nFirst 5 rows:")
        print(df.head())
        
        # Check for missing values
        print(f"\nMissing values:")
        print(df.isnull().sum())
        
        # Check target distribution
        if 'churn' in df.columns:
            print(f"\nChurn distribution:")
            print(df['churn'].value_counts())
            print(f"\nChurn rate: {df['churn'].mean():.2%}")
        
        return df
```

---

### Step 4: Preprocess Data (Day 3)

**File: `src/preprocessor.py`**

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoders = {}
    
    def prepare_data(self, df, target_column):
        """Prepare data for ML"""
        # Separate features and target
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Handle categorical variables
        categorical_cols = X.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            self.encoders[col] = le
        
        # Handle missing values
        X = X.fillna(X.mean())
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        print(f"✅ Prepared data: Train {len(X_train)}, Test {len(X_test)}")
        return X_train_scaled, X_test_scaled, y_train, y_test
```

---

### Step 5: Implement Classifiers (Day 4)

**File: `src/classifier.py`**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class MLClassifier:
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
        dt = DecisionTreeClassifier(random_state=42, max_depth=5)
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
        
        print("✅ Trained all classifiers")
        return self.models
    
    def get_models(self):
        """Get all trained models"""
        return self.models
```

---

### Step 6: Evaluate Models (Day 5)

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
                'precision': precision_score(y_test, y_pred),
                'recall': recall_score(y_test, y_pred),
                'f1': f1_score(y_test, y_pred)
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
        plt.tight_layout()
        plt.savefig(f'results/confusion_matrix_{name.replace(" ", "_")}.png')
        plt.close()
    
    def plot_feature_importance(self, model, feature_names, name):
        """Plot feature importance (for tree-based models)"""
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            indices = importances.argsort()[::-1]
            
            plt.figure(figsize=(10, 6))
            plt.bar(range(len(importances)), importances[indices])
            plt.xticks(range(len(importances)), 
                      [feature_names[i] for i in indices], rotation=45)
            plt.title(f'Feature Importance - {name}')
            plt.tight_layout()
            plt.savefig(f'results/feature_importance_{name.replace(" ", "_")}.png')
            plt.close()
```

---

### Step 7: Create Main Program (Day 6)

**File: `main.py`**

```python
from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.classifier import MLClassifier
from src.evaluator import ModelEvaluator

def main():
    print("=" * 60)
    print("Customer Churn Prediction System")
    print("=" * 60)
    
    # Load data
    loader = DataLoader()
    df = loader.load_data('data/customer_data.csv')
    loader.explore_data(df)
    
    # Preprocess
    preprocessor = Preprocessor()
    X_train, X_test, y_train, y_test = preprocessor.prepare_data(
        df, target_column='churn'
    )
    
    # Train models
    classifier = MLClassifier()
    models = classifier.train_all(X_train, y_train)
    
    # Evaluate
    evaluator = ModelEvaluator()
    results = evaluator.evaluate_all(models, X_test, y_test)
    
    # Find best model
    best_model = max(results, key=lambda x: results[x]['f1'])
    print(f"\n✅ Best model: {best_model}")
    
    # Create visualizations
    for name, model in models.items():
        evaluator.plot_confusion_matrix(model, X_test, y_test, name)
    
    # Feature importance (for tree models)
    feature_names = df.drop(columns=['churn']).columns
    for name, model in models.items():
        if hasattr(model, 'feature_importances_'):
            evaluator.plot_feature_importance(model, feature_names, name)
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

---

---

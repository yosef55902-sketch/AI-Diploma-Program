# Implementation Guide | دليل التنفيذ
## Project 03: Machine Learning Classifier

---

## Step-by-Step Implementation | التنفيذ خطوة بخطوة

### Step 1: Choose Dataset
Options:
- Iris dataset (built-in) - **Recommended for beginners**
- Wine quality dataset
- Customer churn dataset
- Your own dataset

**Loading Iris:**
```python
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
```

---

### Step 2: Data Preprocessing
- Load data with Pandas
- Explore data (head, info, describe)
- Handle missing values
- Encode categorical variables
- Normalize/scale features (if needed)

**Key Steps:**
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.info()  # Check for missing values
df.describe()  # Summary statistics
```

---

### Step 3: Split Data
- Use train_test_split from Scikit-learn
- Typical split: 80% train, 20% test
- Consider stratification for imbalanced data

**Example:**
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

---

### Step 4: Train Models
- Create model instances
- Fit models on training data
- Store trained models

**Example:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'KNN': KNeighborsClassifier(n_neighbors=3)
}

for name, model in models.items():
    model.fit(X_train, y_train)
```

---

### Step 5: Evaluate Models
- Make predictions on test set
- Calculate metrics (accuracy, precision, recall, F1)
- Create confusion matrices
- Visualize results

**Metrics:**
```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))
```

---

### Step 6: Compare & Report
- Compare all models
- Visualize comparison
- Write report with recommendations

**Visualization:**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Compare accuracies
accuracies = [acc1, acc2, acc3]
plt.bar(['LR', 'DT', 'KNN'], accuracies)
plt.title('Model Comparison')
plt.show()
```

---

## Code Structure | هيكل الكود

### Recommended File Organization:

```python
# data_loader.py
def load_data(filename):
    # Load and return data
def preprocess_data(df):
    # Preprocess and return X, y

# models.py
def create_models():
    # Create and return model dictionary

# trainer.py
def train_models(models, X_train, y_train):
    # Train all models

# evaluator.py
def evaluate_model(model, X_test, y_test):
    # Evaluate and return metrics

# visualizer.py
def plot_confusion_matrix(y_test, y_pred, model_name):
    # Plot confusion matrix
def compare_models(results):
    # Compare all models

# main.py
def main():
    # Main pipeline
```

---

## Testing | الاختبار

### Test Cases:
1. **Iris Dataset:** Should achieve >90% accuracy
2. **Custom Dataset:** Test with your own data
3. **Missing Values:** Test data preprocessing
4. **Different Splits:** Test with 70/30, 80/20, 90/10

---

## Troubleshooting | حل المشاكل

### Common Issues:

**Problem:** Low accuracy  
**Solution:** Check data preprocessing, try feature scaling

**Problem:** Overfitting  
**Solution:** Use train/validation/test split, tune hyperparameters

**Problem:** Memory errors  
**Solution:** Use smaller dataset, optimize code

---

**See Template folder for starter code!**


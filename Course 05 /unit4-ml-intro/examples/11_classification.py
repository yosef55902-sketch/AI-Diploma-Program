"""
Unit 4 - Example 11: Classification Basics | أساسيات التصنيف

This example teaches classification - predicting categories/classes.
Learn how to predict discrete categories instead of continuous values.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 10: Linear Regression - Understand regression first
- ✅ Understanding of train/test split and model training

If you haven't completed these, you might struggle with:
- Understanding classification vs regression
- Knowing which algorithm to use
- Understanding classification metrics

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SECOND example in Unit 4 - Machine Learning!

Why this example SECOND?
- Before classification, understand regression (different prediction type)
- Classification predicts categories, regression predicts numbers
- Both are supervised learning but solve different problems

Builds on: 
- Example 10: Linear Regression (same ML workflow, different task)

Leads to: 
- Example 12: Model Evaluation (evaluate classification models)
- Example 13: CPU vs GPU ML (compare GPU acceleration)
- Real-world classification problems (spam detection, image recognition)

## The Story: Sorting vs Measuring | القصة: التصنيف مقابل القياس

Imagine you're organizing mail. Regression is like weighing each letter (continuous value), 
but classification is like sorting into bins (categories: spam/not spam, urgent/normal). 
After learning classification, you can sort items into categories!

Same with ML: Regression predicts numbers (price, temperature), but classification predicts 
categories (spam/not spam, disease/no disease). After learning classification, you can 
predict categories!

## Why Classification Matters | لماذا يهم التصنيف

Classification is essential because:
- Categories: Many real problems are about categories (not numbers)
- Applications: Spam detection, image recognition, medical diagnosis
- Different Metrics: Accuracy, precision, recall (not MSE/R²)
- Algorithms: Logistic regression, decision trees, random forests

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Understand classification vs regression (categories vs numbers)
2. Train classification models (logistic regression, decision trees)
3. Evaluate classification performance (accuracy, precision, recall)
4. Understand confusion matrices
5. Choose the right classification algorithm for your problem
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
f1_score, confusion_matrix, roc_curve, roc_auc_score)
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("=" * 70)
print("Example 11: Classification Basics | أساسيات التصنيف")
print("=" * 70)
print("\n📚 Prerequisites: Example 10 completed, understand regression first")
print("🔗 This is the SECOND example in Unit 4 - predicting categories")
print("🎯 Goal: Master classification - predicting categories/classes\n")
# ============================================================================
# 1. CREATE CLASSIFICATION DATA
# ============================================================================
print("\n1. Creating Classification Data")
print("-" * 70)
np.random.seed(42)
n_samples = 500
X1 = np.random.normal(2, 1.5, n_samples)
X2 = np.random.normal(3, 1.5, n_samples)
X = np.column_stack([X1, X2])
y = ((X1 - 2)**2 + (X2 - 3)**2 < 4).astype(int) + np.random.binomial(1, 0.1, n_samples)
y = np.clip(y, 0, 1)
df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])
df['target'] = y
print(f"Data shape: {df.shape}")
print(f"Target distribution:\n{df['target'].value_counts()}")
# ============================================================================
# 2. LOGISTIC REGRESSION
# ============================================================================
print("\n\n2. Logistic Regression")
print("-" * 70)
X_data = df[['feature_1', 'feature_2']]
y_data = df['target']
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42, stratify=y_data)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
logistic_model = LogisticRegression(random_state=42, max_iter=1000)
logistic_model.fit(X_train_scaled, y_train)
y_test_pred_lr = logistic_model.predict(X_test_scaled)
y_test_proba_lr = logistic_model.predict_proba(X_test_scaled)[:, 1]
accuracy_lr = accuracy_score(y_test, y_test_pred_lr)
print(f"\nLogistic Regression Accuracy: {accuracy_lr:.4f}")
# ============================================================================
# 3. DECISION TREE
# ============================================================================
print("\n\n3. Decision Tree")
print("-" * 70)
tree_model = DecisionTreeClassifier(random_state=42, max_depth=5)
tree_model.fit(X_train, y_train)
y_test_pred_dt = tree_model.predict(X_test)
y_test_proba_dt = tree_model.predict_proba(X_test)[:, 1]
accuracy_dt = accuracy_score(y_test, y_test_pred_dt)
print(f"\nDecision Tree Accuracy: {accuracy_dt:.4f}")
# ============================================================================
# 4. CONFUSION MATRICES
# ============================================================================
print("\n\n4. Confusion Matrices")
print("-" * 70)
cm_lr = confusion_matrix(y_test, y_test_pred_lr)
cm_dt = confusion_matrix(y_test, y_test_pred_dt)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Confusion Matrices')
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', ax=axes[0],
xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
axes[0].set_title('Logistic Regression')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens', ax=axes[1],
xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
axes[1].set_title('Decision Tree')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')
plt.tight_layout()
plt.savefig('11_confusion_matrices.png', dpi=300, bbox_inches='tight')
print("✓ Confusion matrices saved")
plt.close()
# ============================================================================
# 5. ROC CURVES
# ============================================================================
print("\n\n5. ROC Curves")
print("-" * 70)
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_test_proba_lr)
auc_lr = roc_auc_score(y_test, y_test_proba_lr)
fpr_dt, tpr_dt, _ = roc_curve(y_test, y_test_proba_dt)
auc_dt = roc_auc_score(y_test, y_test_proba_dt)
plt.figure(figsize=(10, 6))
plt.plot(fpr_lr, tpr_lr, linewidth=2, label=f'Logistic Regression (AUC = {auc_lr:.4f})')
plt.plot(fpr_dt, tpr_dt, linewidth=2, label=f'Decision Tree (AUC = {auc_dt:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves Comparison')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('11_roc_curves.png', dpi=300, bbox_inches='tight')
print("✓ ROC curves saved")
plt.close()
# ============================================================================
# 6. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Logistic Regression for classification")
print("2. Decision Tree classifier")
print("3. Confusion matrix analysis")
print("4. ROC curves and AUC")
print("\nNext Steps: Continue to Example 12 for Model Evaluation")
print(" :    12  ")
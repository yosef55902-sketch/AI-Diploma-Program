"""
Unit 4 - Example 12: Model Evaluation | تقييم النموذج

This example teaches how to properly evaluate machine learning models.
Learn cross-validation, performance metrics, and how to avoid overfitting.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 10: Linear Regression - Train your first model
- ✅ Example 11: Classification - Understand different model types
- ✅ Understanding of train/test split

If you haven't completed these, you might struggle with:
- Understanding evaluation metrics
- Knowing how to validate models properly
- Understanding overfitting and underfitting

## 🔗 Where This Example Fits | مكان هذا المثال

This is the THIRD example in Unit 4 - Machine Learning!

Why this example THIRD?
- Before evaluating models, you need to train them first
- After learning regression and classification, learn how to evaluate both
- Evaluation is critical - know if your model is actually good!

Builds on: 
- Example 10: Linear Regression (evaluate regression models)
- Example 11: Classification (evaluate classification models)

Leads to: 
- Example 13: CPU vs GPU ML (compare model performance)
- Production models (evaluation ensures models work in production)
- Model improvement (evaluation shows what to fix)

## The Story: Testing Your Work | القصة: اختبار عملك

Imagine you built a bridge. Before using it, you test it thoroughly - check if it 
holds weight, survives storms, lasts long. After testing, you know if it's safe!

Same with ML: Before deploying models, we evaluate them - check accuracy, test on 
new data, validate performance. After evaluation, we know if models work well!

## Why Model Evaluation Matters | لماذا يهم تقييم النموذج

Model evaluation is critical because:
- Trust: Know if your model actually works
- Overfitting: Detect if model memorized training data
- Comparison: Compare different models fairly
- Production: Ensure models work on new, unseen data
- Improvement: Know what to fix to improve performance

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Use cross-validation for robust evaluation
2. Understand evaluation metrics (regression and classification)
3. Detect overfitting and underfitting
4. Compare models fairly using proper evaluation
5. Validate models on unseen data
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import (train_test_split, cross_val_score,
KFold, learning_curve)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (mean_squared_error, r2_score, accuracy_score,
classification_report, confusion_matrix)
from sklearn.preprocessing import StandardScaler
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("=" * 70)
print("Example 12: Model Evaluation | تقييم النموذج")
print("=" * 70)
print("\n📚 Prerequisites: Examples 10 & 11 completed, understand ML models")
print("🔗 This is the THIRD example in Unit 4 - evaluating model performance")
print("🎯 Goal: Master model evaluation - know if your model actually works\n")
# ============================================================================
# 1. CROSS-VALIDATION
# ============================================================================
print("\n1. Cross Validation")
print("-" * 70)
np.random.seed(42)
n_samples = 300
X = np.random.randn(n_samples, 4)
y = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + np.random.randn(n_samples) * 0.1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
# K-Fold Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='r2')
print(f"\n5-Fold Cross-Validation R² Scores:")
print(f" R²    :")
for i, score in enumerate(cv_scores, 1):
    print(f"  Fold {i}: {score:.4f}")
print(f"\nMean CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
print(f"  CV: {cv_scores.mean():.4f}")
# ============================================================================
# 2. LEARNING CURVES
# ============================================================================
print("\n\n2. Learning Curves")
print("-" * 70)
train_sizes, train_scores, val_scores = learning_curve(
model, X_train, y_train, cv=5, n_jobs=-1,
train_sizes=np.linspace(0.1, 1.0, 10), scoring='r2')
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
val_std = np.std(val_scores, axis=1)
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', color='#FF6B6B', label='Training Score')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color='#FF6B6B')
plt.plot(train_sizes, val_mean, 'o-', color='#4ECDC4', label='Validation Score')
plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1, color='#4ECDC4')
plt.xlabel('Training Set Size')
plt.ylabel('R² Score', fontsize=12)
plt.title('Learning Curves')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('12_learning_curves.png', dpi=300, bbox_inches='tight')
print("✓ Learning curves saved")
plt.close()
# ============================================================================
# 3. MULTIPLE METRICS EVALUATION
# ============================================================================
print("\n\n3. Multiple Metrics Evaluation")
print("-" * 70)
# Classification metrics
np.random.seed(42)
X_clf = np.random.randn(200, 3)
y_clf = (X_clf[:, 0] + X_clf[:, 1] > 0).astype(int)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf)
scaler = StandardScaler()
X_train_clf_scaled = scaler.fit_transform(X_train_clf)
X_test_clf_scaled = scaler.transform(X_test_clf)
clf_model = LogisticRegression(random_state=42)
clf_model.fit(X_train_clf_scaled, y_train_clf)
y_pred_clf = clf_model.predict(X_test_clf_scaled)
from sklearn.metrics import precision_score, recall_score, f1_score
accuracy = accuracy_score(y_test_clf, y_pred_clf)
precision = precision_score(y_test_clf, y_pred_clf)
recall = recall_score(y_test_clf, y_pred_clf)
f1 = f1_score(y_test_clf, y_pred_clf)
print("\nClassification Metrics:")
print(f"  Accuracy:  {accuracy:.4f}")
print(f"  Precision: {precision:.4f}")
print(f"  Recall:    {recall:.4f}")
print(f"  F1 Score:  {f1:.4f}")
# ============================================================================
# 4. MODEL COMPARISON
# ============================================================================
print("\n\n4. Model Comparison")
print("-" * 70)
models = {
'Logistic Regression': LogisticRegression(random_state=42),
'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5)
}
results = {}
for name, model in models.items():
    model.fit(X_train_clf_scaled, y_train_clf)
y_pred = model.predict(X_test_clf_scaled)
results[name] = {
'Accuracy': accuracy_score(y_test_clf, y_pred),
'Precision': precision_score(y_test_clf, y_pred),
'Recall': recall_score(y_test_clf, y_pred),
'F1': f1_score(y_test_clf, y_pred)
}
comparison_df = pd.DataFrame(results).T
print("\nModel Comparison:")
print(comparison_df.round(4))
# Visualize comparison
fig, ax = plt.subplots(figsize=(10, 6))
comparison_df.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
ax.set_title('Model Comparison',
             fontsize=14, weight='bold')
ax.set_ylabel('Score', fontsize=12)
ax.set_xlabel('Model')
ax.legend(loc='best')
ax.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('12_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Model comparison saved")
plt.close()
# ============================================================================
# 5. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Cross-validation techniques")
print("2. Learning curves")
print("3. Multiple evaluation metrics")
print("4. Model comparison")
print("\nNext Steps: Continue to Example 13 for CPU vs GPU ML")
print(" :    13  CPU  GPU  ML")
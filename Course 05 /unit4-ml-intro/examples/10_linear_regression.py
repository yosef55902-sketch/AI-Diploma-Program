"""
Unit 4 - Example 10: Linear Regression | الانحدار الخطي

This example teaches linear regression - the foundation of machine learning.
Learn how to predict continuous values and understand the first ML algorithm.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 3: Data Visualization - Visualize model results
- ✅ Understanding of data cleaning and preprocessing
- ✅ Basic statistics knowledge (mean, correlation)

If you haven't completed these, you might struggle with:
- Understanding train/test split
- Interpreting model performance metrics
- Understanding how predictions work

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIRST example in Unit 4 - Introduction to Machine Learning!

Why this example FIRST in Unit 4?
- Before complex ML algorithms, learn the simplest one (linear regression)
- Before classification, understand regression (predicting numbers)
- Before advanced models, master the foundation

Builds on: 
- Unit 2: Data Cleaning (need clean data for modeling)
- Unit 3: Data Visualization (visualize model results)

Leads to: 
- Example 11: Classification (different type of prediction - categories)
- Example 12: Model Evaluation (evaluate model performance)
- All ML work (regression is the foundation)

## The Story: Predicting the Future | القصة: التنبؤ بالمستقبل

Imagine you're buying a house. You know size, and want to predict price. Linear 
regression finds the best line through data points - after learning the relationship, 
you can predict price for any size!

Same with ML: Linear regression finds the best line through data - after training 
on examples, you can predict new values (like house prices, sales, temperatures)!

## Why Linear Regression Matters | لماذا يهم الانحدار الخطي

Linear regression is essential because:
- Foundation: Simplest ML algorithm - understand this first
- Widely Used: Most common ML technique in industry
- Interpretable: Easy to understand and explain
- Fast: Very fast to train and predict
- Baseline: Good starting point before trying complex models

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Understand what linear regression does (finds best line)
2. Train a linear regression model (fit to data)
3. Make predictions (predict new values)
4. Evaluate model performance (MSE, MAE, R²)
5. Visualize regression results (plot predictions vs actual)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("=" * 70)
print("Example 10: Linear Regression | الانحدار الخطي")
print("=" * 70)
print("\n📚 Prerequisites: Unit 3 completed, clean data ready for modeling")
print("🔗 This is the FIRST example in Unit 4 - foundation of machine learning")
print("🎯 Goal: Master linear regression - the simplest ML algorithm\n")
# ============================================================================
# 1. SIMPLE LINEAR REGRESSION
# ============================================================================
print("\n1. Simple Linear Regression")
print("-" * 70)
np.random.seed(42)
house_size = np.linspace(1000, 4000, 100)
house_price = 50 * house_size + 100000 + np.random.normal(0, 30000, 100)
df_simple = pd.DataFrame({'size': house_size, 'price': house_price})
print("\nSample Data:")
print(df_simple.head())
X = df_simple[['size']]
y = df_simple['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_simple = LinearRegression()
model_simple.fit(X_train, y_train)
y_train_pred = model_simple.predict(X_train)
y_test_pred = model_simple.predict(X_test)
print("\nModel Parameters:")
print(f"Intercept: {model_simple.intercept_:.2f}")
print(f"Coefficient: {model_simple.coef_[0]:.4f}")
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
print(f"\nTraining R²: {train_r2:.4f}")
print(f"Test R²: {test_r2:.4f}")
# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].scatter(X_train, y_train, alpha=0.6, label='Training Data')
axes[0].plot(X_train, y_train_pred, 'r-', linewidth=2, label='Regression Line')
axes[0].set_xlabel('House Size (sq ft)')
axes[0].set_ylabel('Price ($)')
axes[0].set_title('Simple Linear Regression Training')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[1].scatter(X_test, y_test, alpha=0.6, color='green', label='Test Data')
axes[1].plot(X_test, y_test_pred, 'r-', linewidth=2, label='Regression Line')
axes[1].set_xlabel('House Size (sq ft)')
axes[1].set_ylabel('Price ($)')
axes[1].set_title('Simple Linear Regression Test')
axes[1].legend()
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('10_linear_regression.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved")
plt.close()
# ============================================================================
# 2. MULTIPLE LINEAR REGRESSION
# ============================================================================
print("\n\n2. Multiple Linear Regression")
print("-" * 70)
np.random.seed(42)
n_samples = 200
data_multiple = {
'size': np.random.uniform(1000, 4000, n_samples),
'bedrooms': np.random.randint(2, 6, n_samples),
'age': np.random.uniform(0, 30, n_samples),
'location_score': np.random.uniform(1, 10, n_samples)
}
df_multiple = pd.DataFrame(data_multiple)
price = (50 * df_multiple['size'] + 30000 * df_multiple['bedrooms'] -
5000 * df_multiple['age'] + 15000 * df_multiple['location_score'] +
50000 + np.random.normal(0, 40000, n_samples))
df_multiple['price'] = price
X_multiple = df_multiple[['size', 'bedrooms', 'age', 'location_score']]
y_multiple = df_multiple['price']
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
X_multiple, y_multiple, test_size=0.2, random_state=42)
model_multiple = LinearRegression()
model_multiple.fit(X_train_m, y_train_m)
y_train_pred_m = model_multiple.predict(X_train_m)
y_test_pred_m = model_multiple.predict(X_test_m)
print("\nCoefficients")
for feature, coef in zip(X_multiple.columns, model_multiple.coef_):
    print(f"  {feature}: {coef:.4f}")
test_r2_m = r2_score(y_test_m, y_test_pred_m)
print(f"\nTest R² Score: {test_r2_m:.4f}")
# Visualize
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_test_m, y_test_pred_m, alpha=0.6, color='green')
ax.plot([y_test_m.min(), y_test_m.max()],
                 [y_test_m.min(), y_test_m.max()], 'r--', linewidth=2)
ax.set_xlabel('Actual Price ($)')
ax.set_ylabel('Predicted Price ($)')
ax.set_title(f'Multiple Regression: Predicted vs Actual (R² = {test_r2_m:.4f})')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('10_multiple_regression.png', dpi=300, bbox_inches='tight')
print("✓ Multiple regression plot saved")
plt.close()
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nNext Steps: Continue to Example 11 for Classification")
print(" :    11 ")
"""
Unit 4 - Exercise 1: Machine Learning Practice
تمرين 1: ممارسة تعلم الآلة

Instructions:
1. Build a regression model
2. Build a classification model
3. Evaluate model performance
4. Compare different models
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Generate sample data for regression
np.random.seed(42)
n_samples = 200
X_reg = np.random.randn(n_samples, 3)
y_reg = 2.5 * X_reg[:, 0] + 1.5 * X_reg[:, 1] - 0.5 * X_reg[:, 2] + np.random.randn(n_samples) * 0.5

# Generate sample data for classification
X_clf = np.random.randn(n_samples, 2)
y_clf = (X_clf[:, 0] + X_clf[:, 1] > 0).astype(int)

# TODO: Write your code here

# Task 1: Regression Model
print("=" * 60)
print("Task 1: Linear Regression")
print("=" * 60)
# Your code here...
# - Split data into train/test sets
# - Train a linear regression model
# - Make predictions
# - Calculate MSE and R² score
# - Visualize predictions vs actual

# Task 2: Classification Model
print("\n" + "=" * 60)
print("Task 2: Classification")
print("=" * 60)
# Your code here...
# - Split data into train/test sets
# - Train a logistic regression model
# - Train a decision tree classifier
# - Evaluate both models
# - Create confusion matrices

# Task 3: Model Comparison
print("\n" + "=" * 60)
print("Task 3: Model Comparison")
print("=" * 60)
# Your code here...
# - Compare accuracy of both classification models
# - Print classification reports
# - Visualize decision boundaries (optional)

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)


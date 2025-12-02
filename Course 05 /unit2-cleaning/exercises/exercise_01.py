"""
Unit 2 - Exercise 1: Data Cleaning Practice
تمرين 1: ممارسة تنظيف البيانات

Instructions:
1. Load the sample dataset (provided below)
2. Identify and handle missing values
3. Detect and remove duplicates
4. Identify and handle outliers
5. Transform and normalize data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Sample dataset with issues
np.random.seed(42)
data = {
    'id': range(1, 201),
    'name': [f'Item_{i}' for i in range(1, 201)],
    'price': np.random.uniform(10, 1000, 200),
    'quantity': np.random.randint(1, 100, 200),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'rating': np.random.uniform(1, 5, 200),
    'date': pd.date_range('2023-01-01', periods=200, freq='D')
}

df = pd.DataFrame(data)

# Introduce data quality issues
df.loc[10:20, 'price'] = np.nan
df.loc[50:55, 'rating'] = np.nan
df.loc[100:105, 'quantity'] = np.nan
df = pd.concat([df, df.iloc[[0, 1, 2, 10, 11]]], ignore_index=True)  # Duplicates
df.loc[150, 'price'] = 50000  # Outlier
df.loc[160, 'quantity'] = -10  # Invalid value

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Identify missing values
print("=" * 60)
print("Task 1: Identify Missing Values")
print("=" * 60)
# Your code here...
# - Count missing values per column
# - Visualize missing values pattern

# Task 2: Handle missing values
print("\n" + "=" * 60)
print("Task 2: Handle Missing Values")
print("=" * 60)
# Your code here...
# - Fill missing prices with median
# - Fill missing ratings with mean
# - Fill missing quantities with forward fill

# Task 3: Detect and remove duplicates
print("\n" + "=" * 60)
print("Task 3: Handle Duplicates")
print("=" * 60)
# Your code here...
# - Count duplicates
# - Remove duplicate rows
# - Verify removal

# Task 4: Identify outliers
print("\n" + "=" * 60)
print("Task 4: Identify Outliers")
print("=" * 60)
# Your code here...
# - Use IQR method to find outliers in 'price'
# - Use Z-score method to find outliers in 'quantity'
# - Visualize outliers with box plots

# Task 5: Handle outliers and invalid values
print("\n" + "=" * 60)
print("Task 5: Handle Outliers")
print("=" * 60)
# Your code here...
# - Remove or cap outliers in 'price'
# - Handle invalid negative quantity values
# - Verify data quality

# Task 6: Data transformation
print("\n" + "=" * 60)
print("Task 6: Data Transformation")
print("=" * 60)
# Your code here...
# - Normalize 'price' using Min-Max scaling
# - Standardize 'rating' using Z-score
# - Create a new feature: total_value = price * quantity

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)


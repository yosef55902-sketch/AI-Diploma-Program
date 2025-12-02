"""
Unit 1 - Exercise 1: Data Science Fundamentals Practice
تمرين 1: ممارسة أساسيات علم البيانات

Instructions:
1. Load a sample dataset (provided below)
2. Explore the data using pandas operations
3. Perform basic statistical analysis
4. Create visualizations
5. Compare CPU (pandas) operations (optional: compare with cuDF if available)

Dataset: Student performance data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure matplotlib for better display
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Sample dataset - Student Performance Data
# البيانات النموذجية - بيانات أداء الطلاب
np.random.seed(42)
data = {
    'student_id': range(1, 101),
    'student_name': [f'Student_{i}' for i in range(1, 101)],
    'age': np.random.randint(18, 25, 100),
    'math_score': np.random.uniform(50, 100, 100),
    'science_score': np.random.uniform(50, 100, 100),
    'english_score': np.random.uniform(50, 100, 100),
    'attendance': np.random.uniform(60, 100, 100),
    'study_hours': np.random.uniform(5, 40, 100),
    'department': np.random.choice(['CS', 'Engineering', 'Business', 'Arts', 'Science'], 100)
}

df = pd.DataFrame(data)

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Explore the data
print("=" * 60)
print("Task 1: Explore the data")
print("المهمة 1: استكشاف البيانات")
print("=" * 60)
# Your code here...
# - Display first 5 rows
# - Display data shape
# - Display data info
# - Display descriptive statistics

# Task 2: Basic statistical analysis
print("\n" + "=" * 60)
print("Task 2: Statistical Analysis")
print("المهمة 2: التحليل الإحصائي")
print("=" * 60)
# Your code here...
# - Calculate mean, median, std for each score column
# - Find correlation between scores
# - Calculate average scores by department

# Task 3: Data filtering and selection
print("\n" + "=" * 60)
print("Task 3: Data Filtering")
print("المهمة 3: تصفية البيانات")
print("=" * 60)
# Your code here...
# - Filter students with math_score > 80
# - Select students from 'CS' department
# - Find students with attendance > 90

# Task 4: Create visualizations
print("\n" + "=" * 60)
print("Task 4: Create Visualizations")
print("المهمة 4: إنشاء التصورات")
print("=" * 60)
# Your code here...
# - Create a histogram of math scores
# - Create a scatter plot: study_hours vs math_score
# - Create a bar chart: average score by department
# - Create a correlation heatmap

# Task 5: Data aggregation
print("\n" + "=" * 60)
print("Task 5: Data Aggregation")
print("المهمة 5: تجميع البيانات")
print("=" * 60)
# Your code here...
# - Group by department and calculate mean scores
# - Find department with highest average math score
# - Calculate total study hours per department

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("اكتمل التمرين 1!")
print("=" * 60)


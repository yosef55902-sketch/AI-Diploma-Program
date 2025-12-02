"""
Unit 3 - Exercise 1: Data Visualization Practice
تمرين 1: ممارسة تصوير البيانات

Instructions:
1. Create various types of visualizations
2. Customize plots with labels, colors, and styles
3. Create statistical visualizations
4. Create interactive visualizations (optional)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Sample dataset
np.random.seed(42)
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [1200, 1500, 1800, 1600, 2000, 2200],
    'region': np.random.choice(['North', 'South', 'East', 'West'], 6),
    'product': np.random.choice(['A', 'B', 'C'], 6),
    'rating': np.random.uniform(3, 5, 6)
}

df = pd.DataFrame(data)

# Additional data for advanced plots
np.random.seed(42)
advanced_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['Type1', 'Type2', 'Type3'], 100),
    'value': np.random.uniform(10, 100, 100)
})

# TODO: Write your code here

# Task 1: Basic matplotlib plots
print("=" * 60)
print("Task 1: Basic Plots")
print("=" * 60)
# Your code here...
# - Create a line plot of sales over months
# - Create a bar chart of sales by region
# - Create a scatter plot of x vs y from advanced_data

# Task 2: Seaborn statistical plots
print("\n" + "=" * 60)
print("Task 2: Statistical Plots")
print("=" * 60)
# Your code here...
# - Create a distribution plot (histogram + KDE) of 'value'
# - Create a box plot of 'value' by 'category'
# - Create a correlation heatmap

# Task 3: Customization
print("\n" + "=" * 60)
print("Task 3: Plot Customization")
print("=" * 60)
# Your code here...
# - Create a customized bar chart with colors, labels, title
# - Add grid, legend, and proper axis labels
# - Save the plot as PNG

# Task 4: Multiple subplots
print("\n" + "=" * 60)
print("Task 4: Multiple Subplots")
print("=" * 60)
# Your code here...
# - Create a figure with 2x2 subplots
# - Plot different visualizations in each subplot
# - Add overall title

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)


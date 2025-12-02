"""
Unit 1 - Example 2: pandas & NumPy Basics | أساسيات pandas و NumPy

This example teaches fundamental data manipulation using pandas and NumPy.
These are the building blocks for all data science work.

All concepts are explained in the code comments below - you can learn everything
from this code example alone!

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 1: Introduction to Data Science - You need to understand DataFrames first!
- ✅ Basic Python knowledge: Variables, lists, dictionaries
- ✅ Understanding of arrays and tables

If you haven't completed these, you might struggle with:
- Understanding DataFrame operations
- Understanding array operations
- Knowing when to use pandas vs NumPy

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SECOND example - it builds on the data structures from Example 1!

Why this example SECOND?
- Before you can clean data, you need to know how to manipulate it
- Before you can analyze data, you need pandas and NumPy skills
- Before you can use GPU libraries (cuDF), you need to understand pandas

Builds on: 
- Example 1: Introduction to Data Science (understanding DataFrames)

Leads to: 
- Example 3: cuDF Introduction (needs pandas knowledge)
- Unit 2: Data Cleaning (needs data manipulation skills)
- All other examples (all need pandas/NumPy!)

## The Story: Learning Your Tools | القصة: تعلم أدواتك

Imagine you're a carpenter. Before building furniture, you need to learn your tools - 
what a hammer does, how to use a saw, when to use a screwdriver. After mastering 
your tools, you can build anything!

Same with data science: Before analyzing data, we learn our tools - pandas for 
tables, NumPy for arrays, when to use each. After mastering these tools, we can 
work with any data!

## Why pandas & NumPy Matter | لماذا يهم pandas و NumPy

These libraries are essential because:
- pandas: The standard tool for working with tables (DataFrames)
- NumPy: The foundation for all numerical computing in Python
- Together: They power 90% of data science work
- Performance: NumPy is fast, pandas makes it easy

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Create and manipulate NumPy arrays (1D and 2D)
2. Perform NumPy operations (mean, std, sum, min, max)
3. Create pandas DataFrames from dictionaries
4. Select, filter, and transform data
5. Use GroupBy operations for aggregations
6. Create visualizations of your data
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# Configure matplotlib settings
# Why unicode_minus False? Prevents issues with negative signs in plots
plt.rcParams['axes.unicode_minus'] = False

# Set display options
# Why max_columns None? Shows all columns without truncation
# Why display.width None? Uses full terminal width for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("=" * 70)
print("Example 2: pandas & NumPy Basics | أساسيات pandas و NumPy")
print("=" * 70)
print("\n📚 Prerequisites: Example 1 completed, basic Python knowledge")
print("🔗 This is the SECOND example - builds data manipulation skills")
print("🎯 Goal: Master pandas DataFrames and NumPy arrays\n")
# ============================================================================
# PART 1: NUMPY BASICS - Working with Arrays
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: NumPy Array Operations")
print("=" * 70)

print("\n📋 BEFORE: You know Python lists but not fast numerical arrays")
print("📋 AFTER: You understand NumPy arrays and their power for numerical computing")
print("💡 WHY THIS MATTERS: NumPy arrays are 100x faster than Python lists for math!\n")

print("\n1. Creating NumPy Arrays")
print("-" * 70)

# Create NumPy arrays
# Why NumPy arrays? Much faster than Python lists for numerical operations
# Why these types? 1D for sequences, 2D for matrices, random for examples
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array - like a list but faster
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array - like a matrix
arr3 = np.random.rand(10)  # Random array - useful for examples

print("\n✅ Arrays created successfully!")
print("\n📊 1D Array (one dimension - like a row):")
print(f"   Array: {arr1}")
print(f"   Shape: {arr1.shape} (tells us dimensions)")
print(f"   Data Type: {arr1.dtype} (what kind of numbers)")

print("\n📊 2D Array (two dimensions - like a table):")
print(f"   Array:\n{arr2}")
print(f"   Shape: {arr2.shape} (rows, columns)")

print("\n📊 Random Array (10 random numbers between 0 and 1):")
print(f"   Array: {arr3}")
print("   Why random? Useful for examples and testing!")
# NumPy operations
# Why these operations? They're the most common statistics you'll need
# Why NumPy functions? Much faster than doing math in Python loops!
print("\n📊 NumPy Statistical Operations:")
print(f"   Mean: {np.mean(arr3):.3f} (average value)")
print(f"   Standard Deviation: {np.std(arr3):.3f} (how spread out)")
print(f"   Sum: {np.sum(arr3):.3f} (total of all values)")
print(f"   Min: {np.min(arr3):.3f} (smallest value)")
print(f"   Max: {np.max(arr3):.3f} (largest value)")

# Array operations
# Why element-wise operations? Very fast - operates on all elements at once!
# Why this is powerful? One line multiplies entire array - no loops needed!
result = arr1 * 2
print(f"\n🔢 Array Operations (element-wise):")
print(f"   {arr1} * 2 = {result}")
print("   Why element-wise? Each element multiplied by 2 - very fast!")
# ============================================================================
# PART 2: PANDAS DATAFRAME BASICS - Working with Tables
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: pandas DataFrame Basics")
print("=" * 70)

print("\n📋 BEFORE: You know NumPy arrays but not how to work with labeled tables")
print("📋 AFTER: You can create and manipulate DataFrames - the heart of data science!")
print("💡 WHY THIS MATTERS: DataFrames are how we work with real-world data (CSV, Excel)!\n")

print("\n2. Creating a pandas DataFrame")
print("-" * 70)

# Create sample DataFrame
# Why seed(42)? Makes results reproducible - same random numbers every run
np.random.seed(42)
data = {
'student_id': range(1, 21),
'name': [f'Student_{i}' for i in range(1, 21)],
'math_score': np.random.randint(60, 101, 20),
'science_score': np.random.randint(60, 101, 20),
'english_score': np.random.randint(60, 101, 20),
'grade': np.random.choice(['A', 'B', 'C'], 20)
}
# Convert dictionary to DataFrame
# Why pd.DataFrame()? Converts dictionary into structured table with rows and columns
# Why this structure? Each key becomes a column, each value list becomes rows
df = pd.DataFrame(data)

print("\n✅ DataFrame created successfully!")
print(f"\n📊 DataFrame Info:")
print(f"   Shape: {df.shape} (Rows: {df.shape[0]}, Columns: {df.shape[1]})")
print(f"   - {df.shape[0]} students (rows)")
print(f"   - {df.shape[1]} features (columns)")

print("\n📋 First 5 rows:")
print(df.head())  # Why head()? Shows sample without overwhelming output

print("\n📋 Data Types:")
print(df.dtypes)  # Why dtypes? Shows what type of data each column contains
print("   - Understanding types helps us know what operations are possible")

print("\n📋 DataFrame Info Summary:")
df.info()  # Why info()? Shows memory usage, types, and null counts
# ============================================================================
# PART 3: BASIC DATA OPERATIONS - Manipulating DataFrames
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: Basic Data Operations")
print("=" * 70)

print("\n📋 BEFORE: You have a DataFrame but don't know how to manipulate it")
print("📋 AFTER: You can select, filter, and transform data easily!")
print("💡 WHY THIS MATTERS: These operations are used in EVERY data science project!\n")

print("\n3. DataFrame Operations")
print("-" * 70)

# Selecting columns
# Why select columns? Focus on relevant data, reduce memory usage
# Why double brackets [['name', 'math_score']]? Returns DataFrame (not Series)
print("\n📌 Selecting Columns:")
print("   Selecting 'name' and 'math_score' columns:")
print(df[['name', 'math_score']].head())

# Filtering data
# Why filter? Focus on subsets of data that meet conditions
# Why boolean indexing df[df['math_score'] > 85]? Very powerful and readable!
print("\n📌 Filtering Data:")
high_scores = df[df['math_score'] > 85]
print(f"   Students with math score > 85: {len(high_scores)}")
print(f"   Why filter? Find specific groups or outliers!")
print(high_scores[['name', 'math_score']].head())

# Adding new column
# Why add columns? Create derived features (total, average, ratios)
# Why this syntax? Simple and intuitive - like Excel formulas!
df['total_score'] = df['math_score'] + df['science_score'] + df['english_score']
df['average_score'] = df['total_score'] / 3
print("\n📌 Adding New Columns:")
print("   Created 'total_score' (sum) and 'average_score' (mean)")
print("   Why create columns? Derived features often more useful than raw data!")
print(df[['name', 'total_score', 'average_score']].head())

# Statistical summary
# Why describe()? Quick overview of data distribution (mean, std, min, max)
# Why these columns? Focus on numerical columns for statistics
print("\n📌 Statistical Summary:")
print("   Quick stats for all score columns:")
print(df[['math_score', 'science_score', 'english_score']].describe())
print("   Why describe()? See distribution at a glance - find outliers and patterns!")
# ============================================================================
# PART 4: GROUPBY OPERATIONS - Aggregating by Groups
# ============================================================================
print("\n" + "=" * 70)
print("PART 4: GroupBy Operations")
print("=" * 70)

print("\n📋 BEFORE: You have individual student data but can't see patterns by group")
print("📋 AFTER: You can aggregate data by categories (grade, region, etc.)!")
print("💡 WHY THIS MATTERS: Most insights come from comparing groups!\n")

print("\n4. GroupBy and Aggregation")
print("-" * 70)

# Group by grade
# Why groupby? Analyze patterns by category (grade A vs B vs C)
# Why agg()? Apply multiple aggregations at once (mean for each score)
grade_stats = df.groupby('grade').agg({
    'math_score': 'mean',
    'science_score': 'mean',
    'english_score': 'mean',
    'average_score': 'mean'
}).round(2)

print("📌 Average Scores by Grade:")
print(grade_stats)
print("   Why groupby? Compare performance across different categories!")
print("   Grade A students vs B vs C - see patterns in the data!")

# ============================================================================
# PART 5: VISUALIZATIONS - Seeing Your Data
# ============================================================================
print("\n" + "=" * 70)
print("PART 5: Creating Visualizations")
print("=" * 70)

print("\n📋 BEFORE: You have numbers in tables - hard to see patterns")
print("📋 AFTER: You have visual plots that make patterns obvious!")
print("💡 WHY THIS MATTERS: Visualizations reveal insights numbers can't show!\n")

print("\n5. Creating Data Visualizations")
print("-" * 70)
print("   Why visualize? Humans understand pictures better than numbers!")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('pandas & NumPy Basics - Visualizations',
             fontsize=16, weight='bold')
# Plot 1: Score distribution
axes[0, 0].hist(df['math_score'], bins=15, color='#4ECDC4', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Math Score Distribution',
            fontsize=12, weight='bold')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(True, alpha=0.3)
# Plot 2: Scores comparison
subjects = ['math_score', 'science_score', 'english_score']
scores_data = [df[col].values for col in subjects]
bp = axes[0, 1].boxplot(scores_data, labels=['Math', 'Science', 'English'],
patch_artist=True)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
axes[0, 1].set_title('Score Comparison',
            fontsize=12, weight='bold')
axes[0, 1].set_ylabel('Score')
axes[0, 1].grid(True, alpha=0.3, axis='y')
# Plot 3: Average by grade
grade_stats.plot(kind='bar', ax=axes[1, 0], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
axes[1, 0].set_title('Average Scores by Grade',
            fontsize=12, weight='bold')
axes[1, 0].set_xlabel('Grade')
axes[1, 0].set_ylabel('Average Score')
axes[1, 0].legend(loc='best')
axes[1, 0].grid(True, alpha=0.3, axis='y')
# Plot 4: Correlation heatmap
corr = df[['math_score', 'science_score', 'english_score']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
square=True, ax=axes[1, 1], cbar_kws={'shrink': 0.8})
axes[1, 1].set_title('Score Correlation',
            fontsize=12, weight='bold')
plt.tight_layout()
plt.savefig('pandas_numpy_basics.png',
dpi=300, bbox_inches='tight')
print("✓ Visualizations saved as 'pandas_numpy_basics.png'")
print("  ")
# ============================================================================
# 🎯 SUMMARY: What We Learned | ملخص: ما تعلمناه
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You knew Python but not pandas or NumPy")
print("   - You didn't know how to manipulate data efficiently")
print("   - You couldn't aggregate or visualize data easily")

print("\n✅ AFTER this example:")
print("   - You can create and manipulate NumPy arrays (fast numerical computing)")
print("   - You can create and manipulate pandas DataFrames (structured tables)")
print("   - You can select, filter, and transform data")
print("   - You can aggregate data using GroupBy")
print("   - You can create visualizations to see patterns")

print("\n📚 Key Concepts Covered:")
print("   1. NumPy Arrays (1D, 2D, operations, statistics)")
print("   2. pandas DataFrames (creation, manipulation, selection)")
print("   3. Data Operations (filtering, adding columns, statistics)")
print("   4. GroupBy Operations (aggregating by categories)")
print("   5. Data Visualizations (histograms, box plots, bar charts, heatmaps)")

print("\n🔗 Where These Skills Fit:")
print("   - NumPy: Foundation for all numerical computing")
print("   - pandas: Essential for working with real-world data")
print("   - These skills are used in EVERY data science project!")

print("\n➡️  Next Steps:")
print("   - Continue to Example 3: cuDF Introduction (GPU-accelerated pandas)")
print("   - You'll learn how to use GPUs to speed up DataFrame operations")
print("   - This builds on pandas knowledge from this example!")

print("\n" + "=" * 70)
plt.show()
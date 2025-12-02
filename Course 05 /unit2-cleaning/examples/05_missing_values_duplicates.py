"""
Unit 2 - Example 5: Missing Values & Duplicates | القيم المفقودة والتكرارات



This example teaches how to identify and handle missing values and duplicates.
Learn essential data cleaning techniques for real-world datasets.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 4: Advanced Data Loading - You need to load data first!
- ✅ Understanding of DataFrames and basic pandas operations

If you haven't completed these, you might struggle with:
- Understanding missing value patterns
- Knowing when to remove vs impute missing values
- Identifying different types of duplicates

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SECOND example in Unit 2 - Data Cleaning!

Why this example SECOND?
- Before you can analyze data, you need to fix missing values and duplicates
- Before you can build models, you need clean data without missing values
- Before you can trust results, you need to remove duplicates

Builds on: 
- Example 4: Advanced Data Loading (now we clean the loaded data)

Leads to: 
- Example 6: Outliers & Transformation (needs data without missing values/duplicates)
- Unit 4: Machine Learning (needs clean data for modeling)

## The Story: Fixing Your Data | القصة: إصلاح بياناتك

Imagine you have a shopping list. Before shopping, you check for missing items (add them) 
and duplicates (remove them). After fixing the list, you can shop efficiently!

Same with data: Before analyzing, we fix missing values (impute or remove) and duplicates 
(remove). After cleaning, we have reliable data for analysis!

## Why Missing Values & Duplicates Matter | لماذا يهم

These issues cause major problems:
- Missing Values: Break ML algorithms (can't train on NaN)
- Duplicates: Bias your results (same data counted multiple times)
- Data Quality: Dirty data = unreliable insights
- Model Performance: Clean data = better models

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Identify missing values and understand their patterns
2. Handle missing values (remove or impute)
3. Detect and remove duplicates
4. Visualize missing data patterns
5. Make informed decisions about cleaning strategies
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
print("=" * 70)
print("Example 5: Missing Values & Duplicates")
print(" 5:   ")
print("=" * 70)
# ============================================================================
# 1. CREATE DATA WITH MISSING VALUES AND DUPLICATES
# ============================================================================
print("\n1. Creating Sample Data with Issues")
print("-" * 70)
np.random.seed(42)
n_samples = 200
# Create sample data
data = {
'id': range(1, n_samples + 1),
'name': [f'Person_{i}' for i in range(1, n_samples + 1)],
'age': np.random.randint(18, 80, n_samples),
'salary': np.random.normal(50000, 15000, n_samples),
'email': [f'person{i}@example.com' for i in range(1, n_samples + 1)],
'department': np.random.choice(['IT', 'HR', 'Finance', 'Sales', None], n_samples),
'join_date': pd.date_range('2020-01-01', periods=n_samples, freq='D')
}
df = pd.DataFrame(data)
# Introduce missing values
missing_indices = np.random.choice(df.index, size=30, replace=False)
df.loc[missing_indices[:10], 'age'] = np.nan
df.loc[missing_indices[10:20], 'salary'] = np.nan
df.loc[missing_indices[20:30], 'department'] = np.nan
# Introduce duplicates
duplicate_rows = df.iloc[:5].copy()
duplicate_rows['id'] = range(201, 206)  # Change IDs to make them appear as duplicates
df = pd.concat([df, duplicate_rows], ignore_index=True)
# Add some duplicate IDs
df.loc[df.index[-10:], 'id'] = df.loc[df.index[-10:], 'id'].values - 100
print(f"✓ Created dataset with {len(df)} rows and {df.shape[1]} columns")
print(f"✓      {len(df)}   {df.shape[1]} ")
# ============================================================================
# 2. DETECT MISSING VALUES
# ============================================================================
print("\n\n2. Detecting Missing Values")
print("-" * 70)
print("\nMissing values per column")
missing_counts = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
'Column': missing_counts.index,
'Missing Count': missing_counts.values,
'Missing %': missing_percent.values
})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
print(missing_df.to_string(index=False))
print(f"\nTotal missing values: {df.isnull().sum().sum()}")
print(f"  : {df.isnull().sum().sum()}")
# Visualize missing values
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Missing Values Analysis',
fontsize=16, weight='bold')
# Plot 1: Missing values bar chart
if len(missing_df) > 0:
    axes[0, 0].bar(missing_df['Column'], missing_df['Missing Count'],
                   color='#FF6B6B', edgecolor='black')
axes[0, 0].set_title('Missing Values Count',
fontsize=12, weight='bold')
axes[0, 0].set_xlabel('Column')
axes[0, 0].set_ylabel('Count')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, alpha=0.3, axis='y')
# Plot 2: Missing values percentage
if len(missing_df) > 0:
    axes[0, 1].bar(missing_df['Column'], missing_df['Missing %'],
                   color='#4ECDC4', edgecolor='black')
axes[0, 1].set_title('Missing Values Percentage',
fontsize=12, weight='bold')
axes[0, 1].set_xlabel('Column')
axes[0, 1].set_ylabel('Percentage (%)')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3, axis='y')
# Plot 3: Missing values matrix (if missingno available)
try:
    msno.matrix(df, ax=axes[1, 0])
    axes[1, 0].set_title('Missing Values Matrix',
                         fontsize=12, weight='bold')
except:
    axes[1, 0].text(0.5, 0.5, 'Missingno not available\nmissingno  ',
ha='center', va='center', transform=axes[1, 0].transAxes)
axes[1, 0].axis('off')
# Plot 4: Heatmap of missing values
missing_heatmap = df.isnull()
sns.heatmap(missing_heatmap, yticklabels=False, cbar=True, ax=axes[1, 1],
cmap='YlOrRd')
axes[1, 1].set_title('Missing Values Heatmap',
fontsize=12, weight='bold')
plt.tight_layout()
plt.savefig('missing_values_analysis.png',
dpi=300, bbox_inches='tight')
print("\n✓ Missing values visualization saved")
print("✓     ")
# ============================================================================
# 3. HANDLE MISSING VALUES
# ============================================================================
print("\n\n3. Handling Missing Values")
print("-" * 70)
# Strategy 1: Drop rows with missing values
print("\nStrategy 1: Drop rows with missing values")
df_dropped = df.dropna()
print(f"Original: {len(df)} rows → After dropping: {len(df_dropped)} rows")
print(f" : {len(df)}  →  : {len(df_dropped)} ")
# Strategy 2: Fill with mean (for numerical)
print("\nStrategy 2: Fill with mean (numerical):")
df_filled_mean = df.copy()
df_filled_mean['age'].fillna(df_filled_mean['age'].mean(), inplace=True)
df_filled_mean['salary'].fillna(df_filled_mean['salary'].mean(), inplace=True)
print(f"Filled missing values in 'age' and 'salary' with mean")
print(f"     'age'  'salary' ")
# Strategy 3: Fill with median
print("\nStrategy 3: Fill with median")
df_filled_median = df.copy()
df_filled_median['age'].fillna(df_filled_median['age'].median(), inplace=True)
df_filled_median['salary'].fillna(df_filled_median['salary'].median(), inplace=True)
print(f"Filled missing values with median")
print(f"    ")
# Strategy 4: Fill with mode (for categorical)
print("\nStrategy 4: Fill with mode (categorical):")
df_filled_mode = df.copy()
mode_dept = df['department'].mode()[0] if not df['department'].mode().empty else 'Unknown'
df_filled_mode['department'].fillna(mode_dept, inplace=True)
print(f"Filled missing values in 'department' with mode: {mode_dept}")
print(f"     'department' : {mode_dept}")
# Strategy 5: Forward fill
print("\nStrategy 5: Forward fill")
df_ffill = df.copy()
df_ffill['department'].fillna(method='ffill', inplace=True)
print(f"Filled missing values using forward fill")
print(f"      ")
# ============================================================================
# 4. DETECT DUPLICATES
# ============================================================================
print("\n\n4. Detecting Duplicates")
print("-" * 70)
# Find duplicate rows
duplicates = df.duplicated()
print(f"Total duplicate rows: {duplicates.sum()}")
print(f"  : {duplicates.sum()}")
# Find duplicates based on specific columns
duplicates_id = df.duplicated(subset=['id'])
print(f"Duplicate IDs: {duplicates_id.sum()}")
print(f" : {duplicates_id.sum()}")
duplicates_email = df.duplicated(subset=['email'])
print(f"Duplicate emails: {duplicates_email.sum()}")
print(f"  : {duplicates_email.sum()}")
# Show duplicate rows
if duplicates.sum() > 0:
    print("\nDuplicate rows:")
print(df[duplicates].head())
# ============================================================================
# 5. REMOVE DUPLICATES
# ============================================================================
print("\n\n5. Removing Duplicates")
print("-" * 70)
# Remove all duplicates (keep first)
df_no_dupes = df.drop_duplicates()
print(f"Original: {len(df)} rows → After removing duplicates: {len(df_no_dupes)} rows")
print(f" : {len(df)}  →   : {len(df_no_dupes)} ")
# Remove duplicates based on specific column (keep first)
df_no_dupe_id = df.drop_duplicates(subset=['id'], keep='first')
print(f"After removing duplicate IDs (keep first): {len(df_no_dupe_id)} rows")
print(f"    ( ): {len(df_no_dupe_id)} ")
# Remove duplicates (keep last)
df_no_dupe_last = df.drop_duplicates(subset=['id'], keep='last')
print(f"After removing duplicate IDs (keep last): {len(df_no_dupe_last)} rows")
print(f"    ( ): {len(df_no_dupe_last)} ")
# ============================================================================
# 6. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You had data with missing values and duplicates but didn't know how to handle them")
print("   - You didn't understand the impact of dirty data on analysis")
print("   - You couldn't make informed decisions about cleaning strategies")

print("\n✅ AFTER this example:")
print("   - You can identify and visualize missing value patterns")
print("   - You can handle missing values (remove or impute)")
print("   - You can detect and remove duplicates")
print("   - You know when to remove vs impute missing values")
print("   - You understand the impact of cleaning on data quality")

print("\n📚 Key Concepts Covered:")
print("   1. Missing Value Detection (isnull, isnull().sum(), visualization)")
print("   2. Missing Value Handling (drop, fillna, forward/backward fill)")
print("   3. Duplicate Detection (duplicated(), subset-based)")
print("   4. Duplicate Removal (drop_duplicates, keep options)")
print("   5. Data Quality Visualization (missingno library)")

print("\n🔗 Where These Skills Fit:")
print("   - Missing Values: Must be handled before ML (algorithms can't train on NaN)")
print("   - Duplicates: Bias results - remove before analysis")
print("   - Cleaning: Foundation for all data science work")

print("\n➡️  Next Steps:")
print("   - Continue to Example 6: Outliers & Transformation")
print("   - You'll learn to handle outliers and transform data")
print("   - After cleaning missing values and duplicates, fix outliers!")
print("\nKey Concepts Covered:")
print("1. Detecting missing values")
print("     ")
print("2. Multiple strategies for handling missing values")
print("       ")
print("3. Finding duplicate records")
print("     ")
print("4. Removing duplicates with different options")
print("      ")
print("5. Visualizing missing data patterns")
print("      ")
print("\nNext Steps: Continue to Example 6 for Outliers & Transformation")
print(" :    6   ")
plt.show()
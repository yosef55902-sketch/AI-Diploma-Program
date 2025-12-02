"""
Unit 2 - Example 6: Outliers & Data Transformation | القيم المتطرفة والتحويل



This example teaches how to detect and handle outliers, and transform data.
Learn essential techniques for preparing data for analysis and modeling.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 5: Missing Values & Duplicates - Clean data first!
- ✅ Understanding of statistics (mean, median, standard deviation)

If you haven't completed these, you might struggle with:
- Understanding outlier detection methods
- Knowing when to remove vs transform outliers
- Understanding data transformations

## 🔗 Where This Example Fits | مكان هذا المثال

This is the THIRD and FINAL example in Unit 2 - Data Cleaning!

Why this example THIRD?
- Before handling outliers, you need clean data (no missing values/duplicates)
- Before transforming data, you need to identify what needs transformation
- After this, your data is fully cleaned and ready for analysis/modeling

Builds on: 
- Example 5: Missing Values & Duplicates (cleaned data without missing values)

Leads to: 
- Unit 3: Data Visualization (clean, transformed data is ready to visualize)
- Unit 4: Machine Learning (clean data is essential for modeling)

## The Story: Refining Your Ingredients | القصة: تحسين المكونات

Imagine you're preparing ingredients. After cleaning, you need to check for any bad 
items (outliers) and cut them to same sizes (transformation). After refinement, 
everything is perfect for cooking!

Same with data: After removing missing values and duplicates, we detect outliers 
(extreme values) and transform data (normalize scales). After refinement, data is 
perfect for analysis!

## Why Outliers & Transformation Matter | لماذا يهم

These techniques are essential because:
- Outliers: Skew statistics and predictions - must be handled
- Transformation: Normalize scales so features are comparable
- Model Performance: Clean, transformed data = better models
- Analysis Accuracy: Outliers can completely change results

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Detect outliers using multiple methods (IQR, Z-score, visualization)
2. Handle outliers (remove, cap, or transform)
3. Apply data transformations (log, square root, normalization)
4. Understand when to use each transformation
5. Prepare data for machine learning models
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
print("=" * 70)
print("Example 6: Outliers & Data Transformation")
print(" 6:    ")
print("=" * 70)
# ============================================================================
# 1. CREATE DATA WITH OUTLIERS
# ============================================================================
print("\n1. Creating Data with Outliers")
print("-" * 70)
np.random.seed(42)
n_samples = 200
# Create normal data
normal_data = np.random.normal(1000, 200, n_samples - 10)
# Add outliers
outliers = np.array([2000, 2100, 2200, 180, 150, 2500, 2400, 100, 2300, 200])
# Combine
data_with_outliers = np.concatenate([normal_data, outliers])
df = pd.DataFrame({
'value': data_with_outliers,
'category': np.random.choice(['A', 'B', 'C'], len(data_with_outliers)),
'score': np.random.normal(75, 10, len(data_with_outliers))
})
print(f"✓ Created dataset with {len(df)} rows")
print(f"✓ Contains {len(outliers)} outliers")
print(f"✓      {len(df)} ")
print(f"✓   {len(outliers)}  ")
# ============================================================================
# 2. DETECT OUTLIERS - Z-SCORE METHOD
# ============================================================================
print("\n\n2. Outlier Detection Z Score Method")
print("-" * 70)
# Calculate Z-scores
z_scores = np.abs(stats.zscore(df['value']))
threshold = 3
outliers_zscore = df[z_scores > threshold]
print(f"Outliers detected (Z-score > {threshold}): {len(outliers_zscore)}")
print(f"   (Z score > {threshold}): {len(outliers_zscore)}")
print(f"\nOutlier values:")
print(outliers_zscore[['value']].head())
# ============================================================================
# 3. DETECT OUTLIERS - IQR METHOD
# ============================================================================
print("\n\n3. Outlier Detection IQR Method")
print("-" * 70)
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
print(f"Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
print(f"Outliers detected (IQR method): {len(outliers_iqr)}")
print(f"   ( IQR): {len(outliers_iqr)}")
# ============================================================================
# 4. VISUALIZE OUTLIERS
# ============================================================================
print("\n\n4. Visualizing Outliers")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Outlier Detection Visualization',
fontsize=16, weight='bold')
# Plot 1: Histogram
axes[0, 0].hist(df['value'], bins=30, color='#4ECDC4', edgecolor='black', alpha=0.7)
axes[0, 0].axvline(df['value'].mean(), color='r', linestyle='--', label='Mean')
axes[0, 0].set_title('Value Distribution')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)
# Plot 2: Box plot
bp = axes[0, 1].boxplot(df['value'], vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('#FF6B6B')
axes[0, 1].set_title('Box Plot')
axes[0, 1].set_ylabel('Value')
axes[0, 1].grid(True, alpha=0.3, axis='y')
# Plot 3: Z-score
axes[1, 0].scatter(range(len(df)), z_scores, alpha=0.6, color='#45B7D1', s=20)
axes[1, 0].axhline(y=threshold, color='r', linestyle='--', label=f'Threshold: {threshold}')
axes[1, 0].axhline(y=-threshold, color='r', linestyle='--')
axes[1, 0].fill_between(range(len(df)), -threshold, threshold, alpha=0.2, color='green', label='Normal range')
axes[1, 0].set_title('Z Scores')
axes[1, 0].set_xlabel('Index')
axes[1, 0].set_ylabel('Z-Score')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
# Plot 4: Scatter with outliers highlighted
colors = ['#FF6B6B' if z > threshold else '#98D8C8' for z in z_scores]
axes[1, 1].scatter(range(len(df)), df['value'], c=colors, alpha=0.6, s=20)
axes[1, 1].set_title('Outliers Highlighted')
axes[1, 1].set_xlabel('Index')
axes[1, 1].set_ylabel('Value')
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outliers_detection.png', dpi=300, bbox_inches='tight')
print("✓ Outlier visualization saved")
print("✓     ")
# ============================================================================
# 5. DATA TRANSFORMATION - NORMALIZATION
# ============================================================================
print("\n\n5. Data Transformation Normalization")
print("-" * 70)
# Min-Max Normalization
from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler_minmax = MinMaxScaler()
df_normalized = df.copy()
df_normalized['value_normalized'] = scaler_minmax.fit_transform(df[['value']])
print("Min Max Normalization:")
print(f"Original range: [{df['value'].min():.2f}, {df['value'].max():.2f}]")
print(f"Normalized range: [{df_normalized['value_normalized'].min():.2f}, {df_normalized['value_normalized'].max():.2f}]")
# ============================================================================
# 6. DATA TRANSFORMATION - STANDARDIZATION
# ============================================================================
print("\n\n6. Data Transformation Standardization")
print("-" * 70)
scaler_standard = StandardScaler()
df_standardized = df.copy()
df_standardized['value_standardized'] = scaler_standard.fit_transform(df[['value']])
print("Standardization (Z score):")
print(f"Original mean: {df['value'].mean():.2f}, std: {df['value'].std():.2f}")
print(f"Standardized mean: {df_standardized['value_standardized'].mean():.4f}, std: {df_standardized['value_standardized'].std():.4f}")
# ============================================================================
# 7. BEFORE/AFTER COMPARISON
# ============================================================================
print("\n\n7. BeforeAfter Comparison")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Data Transformation Comparison',
fontsize=16, weight='bold')
# Original
axes[0, 0].hist(df['value'], bins=30, color='#FF6B6B', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Original Data')
axes[0, 0].set_xlabel('Value')
axes[0, 0].grid(True, alpha=0.3)
# Normalized
axes[0, 1].hist(df_normalized['value_normalized'], bins=30, color='#4ECDC4', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Min Max Normalized')
axes[0, 1].set_xlabel('Normalized Value')
axes[0, 1].grid(True, alpha=0.3)
# Standardized
axes[1, 0].hist(df_standardized['value_standardized'], bins=30, color='#45B7D1', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Standardized')
axes[1, 0].set_xlabel('Standardized Value')
axes[1, 0].grid(True, alpha=0.3)
# Comparison
axes[1, 1].plot(df['value'].values[:50], label='Original', color='#FF6B6B', marker='o', markersize=3)
axes[1, 1].plot(df_normalized['value_normalized'].values[:50], label='Normalized', color='#4ECDC4', marker='s', markersize=3)
axes[1, 1].plot(df_standardized['value_standardized'].values[:50], label='Standardized', color='#45B7D1', marker='^', markersize=3)
axes[1, 1].set_title('Transformation Comparison')
axes[1, 1].set_xlabel('Index')
axes[1, 1].set_ylabel('Value')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('data_transformation.png', dpi=300, bbox_inches='tight')
print("✓ Transformation comparison saved")
print("✓    ")
# ============================================================================
# 8. SUMMARY
# ============================================================================
print("\n\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Outlier detection using Z-score method")
print("        Z score")
print("2. Outlier detection using IQR method")
print("        IQR")
print("3. Visualizing outliers")
print("     ")
print("4. Data normalization (Min-Max)")
print("     (Min Max)")
print("5. Data standardization (Z-score)")
print("     (Z score)")
print("\nNext Steps: Continue to Unit 3 for Data Visualization")
print(" :    3  ")
plt.show()
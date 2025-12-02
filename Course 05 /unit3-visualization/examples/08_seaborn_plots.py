"""
Unit 3 - Example 8: Seaborn Statistical Plots | مخططات Seaborn الإحصائية

This example teaches how to create beautiful statistical visualizations with Seaborn.
Learn how Seaborn simplifies complex statistical plots built on matplotlib.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 7: Matplotlib Fundamentals - Seaborn builds on matplotlib!
- ✅ Understanding of statistical concepts (distributions, correlations)

If you haven't completed these, you might struggle with:
- Understanding what Seaborn adds to matplotlib
- Knowing which statistical plot to use
- Understanding statistical visualizations

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SECOND example in Unit 3 - Data Visualization!

Why this example SECOND?
- Before using Seaborn, you need matplotlib knowledge (Seaborn is built on it)
- Before interactive plots, master statistical visualizations
- Seaborn makes statistical plots much easier than raw matplotlib

Builds on: 
- Example 7: Matplotlib Fundamentals (Seaborn uses matplotlib under the hood)

Leads to: 
- Example 9: Plotly Interactive (different approach - interactive vs static)
- Statistical analysis (Seaborn is perfect for exploring data relationships)

## The Story: Better Tools Make Better Art | القصة: الأدوات الأفضل تصنع فناً أفضل

Imagine you're painting. Basic brushes work, but specialized brushes make painting 
easier and results more beautiful. After learning specialized tools, you create better art!

Same with visualization: Matplotlib works, but Seaborn (specialized for statistics) 
makes statistical plots easier and more beautiful. After learning Seaborn, you create 
better statistical visualizations!

## Why Seaborn Matters | لماذا يهم Seaborn

Seaborn is essential because:
- Statistical Focus: Built specifically for statistical visualizations
- Beautiful Defaults: Attractive plots with minimal code
- Relationship Visualization: Perfect for exploring correlations and distributions
- Simpler Syntax: Easier than matplotlib for complex statistical plots

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Create statistical visualizations with Seaborn
2. Understand Seaborn's relationship to matplotlib
3. Create distribution plots, correlation heatmaps, and pair plots
4. Use Seaborn's beautiful default styles
5. Choose the right plot type for your statistical question
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set seaborn style
sns.set_style("whitegrid")
sns.set_palette("husl")
print("=" * 70)
print("Example 8: Seaborn Statistical Plots | مخططات Seaborn الإحصائية")
print("=" * 70)
print("\n📚 Prerequisites: Example 7 completed, matplotlib knowledge")
print("🔗 This is the SECOND example in Unit 3 - statistical visualizations")
print("🎯 Goal: Master Seaborn for beautiful statistical plots\n")
# ============================================================================
# 1. CREATE SAMPLE DATA
# ============================================================================
print("\n1. Creating Sample Data")
print("-" * 70)
np.random.seed(42)
n_samples = 200
df = pd.DataFrame({
'category': np.random.choice(['A', 'B', 'C', 'D'], n_samples),
'value1': np.random.normal(100, 15, n_samples),
'value2': np.random.normal(50, 10, n_samples),
'value3': np.random.exponential(2, n_samples),
'score': np.random.randint(0, 100, n_samples),
'group': np.random.choice(['Group1', 'Group2', 'Group3'], n_samples)
})
print(f"✓ Created dataset with {len(df)} rows")
print(df.head())
# ============================================================================
# 2. DISTRIBUTION PLOTS
# ============================================================================
print("\n2. Distribution Plots")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Seaborn Distribution Plots',
fontsize=16, weight='bold')
# Histogram with KDE
sns.histplot(data=df, x='value1', kde=True, ax=axes[0, 0], color='#FF6B6B')
axes[0, 0].set_title('Histogram with KDE',
fontsize=12, weight='bold')
# Distribution by category
sns.histplot(data=df, x='value1', hue='category', kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Distribution by Category',
fontsize=12, weight='bold')
# Box plot
sns.boxplot(data=df, x='category', y='value1', ax=axes[1, 0], palette='husl')
axes[1, 0].set_title('Box Plot')
# Violin plot
sns.violinplot(data=df, x='category', y='value2', ax=axes[1, 1], palette='husl')
axes[1, 1].set_title('Violin Plot')
plt.tight_layout()
plt.savefig('06_distribution_plots.png',
dpi=300, bbox_inches='tight')
print("✓ Distribution plots saved")
plt.close()
# ============================================================================
# 3. CATEGORICAL PLOTS
# ============================================================================
print("\n3. Categorical Plots")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Seaborn Categorical Plots',
fontsize=16, weight='bold')
# Bar plot
sns.barplot(data=df, x='category', y='value1', ax=axes[0, 0], palette='husl')
axes[0, 0].set_title('Bar Plot')
# Count plot
sns.countplot(data=df, x='category', ax=axes[0, 1], palette='husl')
axes[0, 1].set_title('Count Plot')
# Grouped bar plot
sns.barplot(data=df, x='category', y='value1', hue='group', ax=axes[1, 0], palette='husl')
axes[1, 0].set_title('Grouped Bar Plot',
fontsize=12, weight='bold')
axes[1, 0].legend(title='Group')
# Strip plot
sns.stripplot(data=df, x='category', y='value2', ax=axes[1, 1], palette='husl', size=4)
axes[1, 1].set_title('Strip Plot')
plt.tight_layout()
plt.savefig('07_categorical_plots.png',
dpi=300, bbox_inches='tight')
print("✓ Categorical plots saved")
plt.close()
# ============================================================================
# 4. RELATIONSHIP PLOTS
# ============================================================================
print("\n4. Relationship Plots")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Seaborn Relationship Plots',
fontsize=16, weight='bold')
# Scatter plot
sns.scatterplot(data=df, x='value1', y='value2', hue='category', ax=axes[0, 0], s=50)
axes[0, 0].set_title('Scatter Plot')
# Scatter with regression line
sns.regplot(data=df, x='value1', y='value2', ax=axes[0, 1], scatter_kws={'alpha': 0.5})
axes[0, 1].set_title('Regression Plot')
# Line plot
df_sorted = df.sort_values('value1')
sns.lineplot(data=df_sorted, x='value1', y='value2', hue='category', ax=axes[1, 0])
axes[1, 0].set_title('Line Plot')
# Joint plot (distribution + scatter)
from scipy.stats import pearsonr
corr, _ = pearsonr(df['value1'], df['value2'])
axes[1, 1].scatter(df['value1'], df['value2'], alpha=0.5, s=30)
axes[1, 1].set_xlabel('Value 1')
axes[1, 1].set_ylabel('Value 2')
axes[1, 1].set_title(f'Correlation: {corr:.3f}',
fontsize=12, weight='bold')
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('08_relationship_plots.png',
dpi=300, bbox_inches='tight')
print("✓ Relationship plots saved")
plt.close()
# ============================================================================
# 5. HEATMAPS AND CORRELATION
# ============================================================================
print("\n5. Heatmaps and Correlation")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Heatmaps and Correlation',
fontsize=16, weight='bold')
# Correlation heatmap
numeric_cols = ['value1', 'value2', 'value3', 'score']
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
square=True, ax=axes[0], cbar_kws={'shrink': 0.8})
axes[0].set_title('Correlation Heatmap',
fontsize=12, weight='bold')
# Pivot table heatmap
pivot_data = df.pivot_table(values='value1', index='category', columns='group', aggfunc='mean')
sns.heatmap(pivot_data, annot=True, fmt='.1f', cmap='YlOrRd', ax=axes[1])
axes[1].set_title('Pivot Table Heatmap',
fontsize=12, weight='bold')
plt.tight_layout()
plt.savefig('09_heatmaps.png',
dpi=300, bbox_inches='tight')
print("✓ Heatmaps saved")
plt.close()
# ============================================================================
# 6. PAIR PLOT
# ============================================================================
print("\n6. Pair Plot")
print("-" * 70)
pair_plot = sns.pairplot(df[numeric_cols + ['category']], hue='category', palette='husl')
pair_plot.fig.suptitle('Pair Plot')
pair_plot.savefig('10_pair_plot.png',
dpi=300, bbox_inches='tight')
print("✓ Pair plot saved")
plt.close()
# ============================================================================
# 7. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You knew matplotlib but creating statistical plots was complex")
print("   - You didn't know how to visualize distributions and correlations easily")
print("   - You couldn't create beautiful statistical visualizations quickly")

print("\n✅ AFTER this example:")
print("   - You can create statistical visualizations with Seaborn (much easier!)")
print("   - You can visualize distributions, correlations, and relationships")
print("   - You can create beautiful plots with minimal code")
print("   - You understand when to use Seaborn vs matplotlib")

print("\n📚 Key Concepts Covered:")
print("   1. Seaborn Basics (built on matplotlib, easier syntax)")
print("   2. Distribution Plots (histograms, KDE, violin plots)")
print("   3. Statistical Relationships (scatter plots, regression)")
print("   4. Correlation Heatmaps (visualize relationships)")
print("   5. Pair Plots (compare all variables at once)")

print("\n🔗 Where These Skills Fit:")
print("   - Statistical Analysis: Perfect for exploring data relationships")
print("   - Data Exploration: Quickly visualize distributions and correlations")
print("   - Beautiful Plots: Seaborn's defaults are professional-looking")
print("   - Next: Plotly adds interactivity to visualizations")

print("\n➡️  Next Steps:")
print("   - Continue to Example 9: Plotly Interactive Visualizations")
print("   - You'll learn interactive plots (zoom, pan, hover)")
print("   - Interactive plots are great for dashboards and exploration!")

print("\n" + "=" * 70)
print("\nKey Concepts Covered:")
print("1. Distribution plots (histogram, KDE, box, violin)")
print("    ")
print("2. Categorical plots (bar, count, strip)")
print("    ")
print("3. Relationship plots (scatter, regression, line)")
print("    ")
print("4. Heatmaps and correlation matrices")
print("      ")
print("5. Pair plots for multivariate analysis")
print("       ")
print("\nNext Steps: Continue to Example 9 for Interactive Plotly")
print(" :    9  Plotly ")
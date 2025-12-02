"""
Unit 3 - Example 7: Matplotlib Fundamentals | أساسيات Matplotlib

This example teaches the fundamentals of matplotlib for creating static visualizations.
Learn how to create basic plots, customize them, and communicate data visually.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 2: Data Cleaning - You need clean data to visualize!
- ✅ Understanding of DataFrames and basic data manipulation

If you haven't completed these, you might struggle with:
- Understanding what to visualize
- Knowing which plot type to use
- Customizing plots effectively

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIRST example in Unit 3 - Data Visualization!

Why this example FIRST in Unit 3?
- Before using advanced visualization libraries, learn the foundation (matplotlib)
- Before creating interactive plots, master static plots
- Before using Seaborn, understand matplotlib (Seaborn is built on matplotlib)

Builds on: 
- Unit 2: Data Cleaning (visualize the cleaned data)

Leads to: 
- Example 8: Seaborn Plots (needs matplotlib knowledge - Seaborn builds on it)
- Example 9: Plotly Interactive (builds on static plot knowledge)
- All visualization work (matplotlib is the foundation)

## The Story: Learning to Draw | القصة: تعلم الرسم

Imagine you're learning art. Before creating masterpieces, you learn basic drawing - 
lines, shapes, colors. After mastering basics, you can create beautiful artwork!

Same with visualization: Before creating advanced plots, we learn matplotlib basics - 
line plots, bar charts, histograms. After mastering basics, we can create beautiful 
data visualizations!

## Why Matplotlib Matters | لماذا يهم Matplotlib

Matplotlib is essential because:
- Foundation: All Python visualization libraries build on matplotlib
- Flexibility: Full control over every plot element
- Standard: Most widely used Python plotting library
- Static Plots: Perfect for reports, papers, presentations

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Create basic plots (line, bar, scatter, histogram)
2. Customize plots (colors, labels, legends, titles)
3. Create subplots (multiple plots in one figure)
4. Save plots to files
5. Understand matplotlib's object-oriented interface
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
print("=" * 70)
print("Example 7: Matplotlib Fundamentals | أساسيات Matplotlib")
print("=" * 70)
print("\n📚 Prerequisites: Unit 2 completed, clean data ready to visualize")
print("🔗 This is the FIRST example in Unit 3 - foundation for all visualization")
print("🎯 Goal: Master matplotlib basics for creating static visualizations\n")
# ============================================================================
# 1. BASIC LINE PLOT
# ============================================================================
print("\n1. Basic Line Plot")
print("-" * 70)
# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, label='sin(x)', linewidth=2, color='#FF6B6B')
ax.plot(x, y2, label='cos(x)', linewidth=2, color='#4ECDC4')
ax.plot(x, y3, label='sin(x)*cos(x)', linewidth=2, color='#45B7D1', linestyle='--')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Basic Line Plot')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('01_line_plot.png', dpi=300, bbox_inches='tight')
print("✓ Line plot saved")
plt.close()
# ============================================================================
# 2. BAR CHART
# ============================================================================
print("\n2. Bar Chart")
print("-" * 70)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [23, 45, 56, 78, 32]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'],
edgecolor='black', linewidth=1.5)
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Bar Chart Example')
ax.grid(True, alpha=0.3, axis='y')
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
ha='center', va='bottom', fontsize=11, weight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('02_bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Bar chart saved")
plt.close()
# ============================================================================
# 3. SCATTER PLOT
# ============================================================================
print("\n3. Scatter Plot")
print("-" * 70)
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100) * 0.5
colors_scatter = np.random.rand(100)
sizes = 100 * np.random.rand(100)
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=sizes,
alpha=0.6, cmap='viridis', edgecolors='black', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatter Plot Example')
plt.colorbar(scatter, ax=ax, label='Color Value')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('03_scatter_plot.png', dpi=300, bbox_inches='tight')
print("✓ Scatter plot saved")
plt.close()
# ============================================================================
# 4. MULTIPLE SUBPLOTS
# ============================================================================
print("\n4. Multiple Subplots")
print("-" * 70)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Multiple Subplots Example',
fontsize=16, weight='bold')
# Subplot 1: Line plot
axes[0, 0].plot(x, y1, color='#FF6B6B', linewidth=2)
axes[0, 0].set_title('Line Plot')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].grid(True, alpha=0.3)
# Subplot 2: Bar chart
axes[0, 1].bar(categories[:4], values[:4], color='#4ECDC4', edgecolor='black')
axes[0, 1].set_title('Bar Chart')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Value')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3, axis='y')
# Subplot 3: Scatter plot
axes[1, 0].scatter(x_scatter, y_scatter, alpha=0.6, c='#45B7D1', edgecolors='black', s=30)
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')
axes[1, 0].grid(True, alpha=0.3)
# Subplot 4: Histogram
axes[1, 1].hist(y_scatter, bins=20, color='#FFA07A', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Histogram')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('04_multiple_subplots.png', dpi=300, bbox_inches='tight')
print("✓ Multiple subplots saved")
plt.close()
# ============================================================================
# 5. CUSTOMIZATION
# ============================================================================
print("\n5. Advanced Customization")
print("-" * 70)
fig, ax = plt.subplots(figsize=(12, 7))
# Create multiple lines with different styles
x_custom = np.linspace(0, 2*np.pi, 100)
ax.plot(x_custom, np.sin(x_custom), label='sin(x)', linewidth=3,
color='#FF6B6B', linestyle='-', marker='o', markersize=4, markevery=10)
ax.plot(x_custom, np.cos(x_custom), label='cos(x)', linewidth=3,
color='#4ECDC4', linestyle='--', marker='s', markersize=4, markevery=10)
ax.plot(x_custom, np.sin(2*x_custom), label='sin(2x)', linewidth=3,
color='#45B7D1', linestyle='-.', marker='^', markersize=4, markevery=10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Advanced Customization')
ax.legend(fontsize=12, loc='best', framealpha=0.9, shadow=True)
ax.grid(True, alpha=0.4, linestyle='--', linewidth=0.8)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
# Add text annotation
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 1.2),
arrowprops=dict(arrowstyle='->', color='red', lw=2),
fontsize=12, color='red', weight='bold')
plt.tight_layout()
plt.savefig('05_customization.png', dpi=300, bbox_inches='tight')
print("✓ Customized plot saved")
plt.close()
# ============================================================================
# 6. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You had data but couldn't visualize it effectively")
print("   - You didn't know how to create different types of plots")
print("   - You couldn't customize plots for presentations")

print("\n✅ AFTER this example:")
print("   - You can create basic plots (line, bar, scatter, histogram)")
print("   - You can customize plots (colors, labels, legends, styles)")
print("   - You can create subplots (multiple plots in one figure)")
print("   - You can save plots to files for reports and presentations")
print("   - You understand matplotlib's object-oriented interface")

print("\n📚 Key Concepts Covered:")
print("   1. Basic Plot Types (line plots, bar charts, scatter plots, histograms)")
print("   2. Plot Customization (colors, line styles, markers, labels)")
print("   3. Subplots (creating multiple plots in one figure)")
print("   4. Saving Plots (PNG, PDF, SVG formats)")
print("   5. Matplotlib OOP Interface (fig, ax objects)")

print("\n🔗 Where These Skills Fit:")
print("   - Matplotlib: Foundation for all Python visualization")
print("   - Static Plots: Perfect for reports, papers, presentations")
print("   - Customization: Full control over every plot element")
print("   - Next: Seaborn builds on matplotlib for statistical plots")

print("\n➡️  Next Steps:")
print("   - Continue to Example 8: Seaborn Plots")
print("   - You'll learn Seaborn - easier statistical visualizations")
print("   - Seaborn builds on matplotlib knowledge from this example!")

print("\n" + "=" * 70)
print("\nKey Concepts Covered:")
print("1. Basic line plots")
print("     ")
print("2. Bar charts")
print("     ")
print("3. Scatter plots")
print("    ")
print("4. Multiple subplots")
print("     ")
print("5. Advanced customization (colors, styles, annotations)")
print("     (   )")
print("\nNext Steps: Continue to Example 8 for Seaborn")
print(" :    8  Seaborn")
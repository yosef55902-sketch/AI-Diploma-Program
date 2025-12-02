"""
Unit 1 - Example 1: Introduction to Data Science | مقدمة في علم البيانات

This example introduces the data science lifecycle and basic concepts.
This is the foundation for all other examples in the course.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have:
- ✅ Python 3.8+ installed and working
- ✅ Basic Python knowledge: Variables, data types, lists, dictionaries
- ✅ Libraries installed: pandas, numpy, matplotlib, seaborn (see ../../requirements.txt)
- ✅ Understanding of data: What is a dataset? What are rows and columns?

If you haven't completed these, you might struggle with:
- Understanding DataFrame operations
- Understanding data types and structures
- Using pandas functions
- Interpreting statistical summaries

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIRST example - it's the foundation for all data science!

Why this example FIRST?
- BEFORE you can clean data, you need to understand the data science lifecycle
- BEFORE you can visualize data, you need to know what data structures are
- BEFORE you can build ML models, you need to understand the complete workflow

Builds on: 
- Python basics (variables, data structures)
- Basic understanding of data files (CSV format)

Leads to: 
- Example 2: Pandas & NumPy Basics (needs understanding of data structures)
- Example 3: cuDF Introduction (needs pandas knowledge)
- All other examples (all need data science lifecycle understanding!)

## The Story: Building a House | القصة: بناء منزل

Imagine you're building a house. BEFORE you start, you need to see the blueprint - 
understand all the steps (foundation → walls → roof → finishing). After seeing the 
blueprint, you know where each step fits and why the order matters.

Same with data science: BEFORE doing any data work, we learn the lifecycle - 
understand all steps (problem → data → cleaning → modeling → deployment). After 
learning the lifecycle, you know where each technique fits and why order matters!

## Why Data Science Lifecycle Matters | لماذا يهم دورة حياة علم البيانات

Understanding the lifecycle is crucial because:
- Find Your Place: Know where you are in any project
- Understand Order: Know why steps come in this sequence
- See Big Picture: Understand how all parts connect
- Make Decisions: Know what to do next at each stage

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Understand the complete data science lifecycle (9 steps)
2. Know what pandas DataFrames are and how they work
3. Create basic data visualizations
4. Understand the workflow from data to insights
5. See how all course units fit into the lifecycle
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import seaborn as sns

# Set style for better plots
# Why seaborn-v0_8? It provides professional-looking plots automatically
# Why set palette? Consistent colors make comparisons easier
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=" * 70)
print("Example 1: Introduction to Data Science | مقدمة في علم البيانات")
print("=" * 70)
print("\n📚 Prerequisites: Python basics, pandas, numpy, matplotlib")
print("🔗 This is the FIRST example - foundation for all others")
print("🎯 Goal: Understand the data science lifecycle and basic workflow\n")
# ============================================================================
# PART 1: DATA SCIENCE LIFECYCLE VISUALIZATION
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: Understanding the Data Science Lifecycle")
print("=" * 70)

print("\n📋 BEFORE: You know individual data science techniques but not how they connect")
print("📋 AFTER: You understand the complete lifecycle and where each step fits")
print("💡 WHY THIS MATTERS: The lifecycle shows you the big picture - where everything fits!\n")

print("\n1. Creating the Data Science Lifecycle Diagram")
print("-" * 70)

# Define the data science lifecycle steps
# Why these 9 steps? They represent the complete journey from problem to production
# Why in this order? Each step builds on the previous one - can't skip steps!
lifecycle_steps = [
"1. Problem Definition\n ",
"2. Data Collection\n ",
"3. Data Exploration\n ",
"4. Data Cleaning\n ",
"5. Feature Engineering\n ",
"6. Model Building\n ",
"7. Model Evaluation\n ",
"8. Deployment\n",
"9. Monitoring\n"
]
# Create a flowchart-style visualization
# Why flowchart? Visual representation makes the process easy to understand
# Why figsize (14, 10)? Large enough to see all steps clearly
fig, ax = plt.subplots(figsize=(14, 10))

# Colors for different phases
# Why different colors? Helps visually distinguish each lifecycle stage
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
'#F7DC6F', '#BB8FCE', '#85C1E2', '#F8C471']
# Draw lifecycle steps as boxes
y_positions = np.linspace(0.9, 0.1, len(lifecycle_steps))
box_width = 0.3
box_height = 0.07
for i, (step, y_pos, color) in enumerate(zip(lifecycle_steps, y_positions, colors)):
    # Draw box
    box = FancyBboxPatch(
        (0.35, y_pos - box_height/2), box_width, box_height,
        boxstyle="round,pad=0.01",
        facecolor=color,
        edgecolor='black',
        linewidth=2,
        transform=ax.transAxes
    )
    ax.add_patch(box)
    # Add text
    ax.text(0.5, y_pos, step, ha='center', va='center',
            transform=ax.transAxes, fontsize=10, weight='bold')
    # Draw arrow to next step (except for last)
    if i < len(lifecycle_steps) - 1:
        ax.arrow(0.5, y_pos - box_height/2, 0, -0.01,
                transform=ax.transAxes, head_width=0.02, head_length=0.01,
                fc='black', ec='black', linewidth=2)
# Add feedback loop from Monitoring to Problem Definition
ax.annotate('', xy=(0.35, 0.9), xytext=(0.5, 0.1),
arrowprops=dict(arrowstyle='->', lw=2, color='red', linestyle='--',
connectionstyle="arc3,rad=-0.3"),
transform=ax.transAxes)
ax.text(0.2, 0.5, 'Feedback\n ', transform=ax.transAxes,
fontsize=10, color='red', weight='bold', rotation=90)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Data Science Lifecycle',
             fontsize=16, weight='bold', pad=20)
plt.tight_layout()
plt.savefig('data_science_lifecycle.png',
            dpi=300, bbox_inches='tight')
print("✓ Lifecycle diagram saved as 'data_science_lifecycle.png'")
print("    ")
# ============================================================================
# PART 2: BASIC DATA STRUCTURES DEMONSTRATION
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: Working with Data Structures")
print("=" * 70)

print("\n📋 BEFORE: You have raw data files that you can't use")
print("📋 AFTER: You have a pandas DataFrame - structured data ready for analysis")
print("💡 WHY THIS MATTERS: DataFrames are the foundation of all data science work!\n")

print("\n2. Creating Sample Data")
print("-" * 70)

# Create sample data to demonstrate data science concepts
# Why random.seed(42)? Makes results reproducible - same random numbers every time
# Why 42? It's a programming tradition (from "Hitchhiker's Guide to the Galaxy")!
np.random.seed(42)
n_samples = 100  # Why 100? Large enough to be realistic, small enough to run fast

# Generate sample dataset (sales data)
# Why sales data? Easy to understand - everyone knows what sales are!
# Why a dictionary? pandas.DataFrame() accepts dictionaries - easy way to create data
data = {
'date': pd.date_range('2024-01-01', periods=n_samples, freq='D'),
'sales': np.random.normal(1000, 200, n_samples),
'customers': np.random.poisson(50, n_samples),
'product_category': np.random.choice(['A', 'B', 'C'], n_samples),
'region': np.random.choice(['North', 'South', 'East', 'West'], n_samples)
}
# Convert dictionary to pandas DataFrame
# Why pd.DataFrame()? Converts raw data into structured format we can analyze
# DataFrame = like a spreadsheet table in Python - rows and columns
df = pd.DataFrame(data)

print("\n✅ Data created successfully!")
print(f"📊 Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"   - Rows represent individual records (data points)")
print(f"   - Columns represent features (variables we measure)")

print("\n📋 First 5 rows (head of data):")
print(df.head())  # Why head()? Shows first few rows without overwhelming output

print("\n📋 Data Types:")
print(df.dtypes)  # Why dtypes? Shows what type of data each column contains
print("   - Understanding types helps us know what operations are possible")

print("\n📋 Basic Statistics:")
print(df.describe())  # Why describe()? Gives summary statistics (mean, std, min, max)
print("   - These statistics help us understand our data's distribution")
# ============================================================================
# PART 3: DATA SCIENCE WORKFLOW DEMONSTRATION
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: Following the Data Science Workflow")
print("=" * 70)

print("\n📋 BEFORE: You have data but no clear direction")
print("📋 AFTER: You have a clear workflow from problem to solution")
print("💡 WHY THIS MATTERS: Following the workflow ensures you don't miss important steps!\n")

print("\n3. Walking Through the Data Science Workflow")
print("-" * 70)

# Step 1: Problem Definition
# Why FIRST? Without a clear problem, you don't know what to solve!
# This is like planning a trip - you need a destination before you start
print("\n📌 Step 1: Problem Definition")
print("   Problem: Predict daily sales based on customer count and region")
print("   Why define problem first? It guides all subsequent steps!")
print("   Without a clear problem, you'll analyze data aimlessly")
# Step 2: Data Collection
# Why SECOND? You need data to work with - can't analyze without data!
# In real projects, this might involve APIs, databases, files, etc.
print("\n📌 Step 2: Data Collection")
print(f"   ✓ Collected {len(df)} data points (rows)")
print(f"   ✓ Each row represents one day's sales data")
print(f"   Why collect data? Data is the raw material for all analysis!")
# Step 3: Data Exploration
# Why THIRD? You need to understand your data before cleaning or modeling
# This is like examining ingredients before cooking - know what you're working with!
print("\n📌 Step 3: Data Exploration")
missing_count = df.isnull().sum().sum()
print(f"   ✓ Found {missing_count} missing values")
print(f"   ✓ Data ranges from {df['date'].min()} to {df['date'].max()}")
print(f"   Why explore first? Understanding data helps you make informed decisions!")
print(f"   Missing values? We'll handle these in Unit 2 (Data Cleaning)")
# Step 4: Basic Analysis
# Why do analysis? To find patterns and insights in the data
# This gives us initial understanding before building models
print("\n📌 Step 4: Initial Analysis")
avg_sales = df['sales'].mean()
print(f"   ✓ Average daily sales: ${avg_sales:.2f}")
print(f"   Why calculate averages? They give us a baseline to compare against!")
print(f"   If we predict sales, we can compare to this ${avg_sales:.2f} average")
# ============================================================================
# PART 4: VISUALIZATION - Seeing the Data
# ============================================================================
print("\n" + "=" * 70)
print("PART 4: Visualizing the Data")
print("=" * 70)

print("\n📋 BEFORE: You have numbers in tables (hard to understand)")
print("📋 AFTER: You have visual plots (easy to understand patterns)")
print("💡 WHY THIS MATTERS: A picture is worth a thousand numbers - visualizations reveal patterns!\n")

print("\n4. Creating Data Visualizations")
print("-" * 70)
print("   Why visualize? Humans understand pictures better than numbers!")
print("   Visualizations help us see trends, patterns, and relationships\n")
# Create subplots - 4 plots in one figure
# Why subplots(2, 2)? Shows multiple views of data side-by-side for comparison
# Why figsize (14, 10)? Large enough to see details in all plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Data Science Introduction - Data Overview',
            fontsize=16, weight='bold')

# Plot 1: Sales over time
# Why line plot? Shows trends and patterns over time
# Why this is useful? See if sales are increasing, decreasing, or stable
axes[0, 0].plot(df['date'], df['sales'], color='#4ECDC4', linewidth=2)
axes[0, 0].axhline(y=avg_sales, color='r', linestyle='--', label=f'Average: ${avg_sales:.0f}')
axes[0, 0].set_title('Sales Over Time')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Sales ($)')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)
# Plot 2: Sales distribution (histogram)
# Why histogram? Shows how sales values are distributed
# Why bins=20? Enough to see distribution pattern without being too detailed
axes[0, 1].axvline(x=avg_sales, color='r', linestyle='--', linewidth=2, label=f'Mean: ${avg_sales:.0f}')
axes[0, 1].set_title('Sales Distribution')
axes[0, 1].set_xlabel('Sales ($)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
# Plot 3: Sales by region (bar chart)
# Why groupby? Groups data by region and calculates average sales per region
# Why bar chart? Easy to compare values across categories (regions)
axes[1, 0].bar(region_sales.index, region_sales.values, color='#45B7D1', edgecolor='black')
axes[1, 0].set_title('Average Sales by Region',
            fontsize=12, weight='bold')
axes[1, 0].set_xlabel('Region')
axes[1, 0].set_ylabel('Average Sales ($)')
axes[1, 0].grid(True, alpha=0.3, axis='y')
# Plot 4: Sales vs Customers (scatter plot)
# Why scatter plot? Shows relationship between two variables (customers and sales)
# Why this matters? Helps us see if more customers = more sales (correlation)
axes[1, 1].set_title('Sales vs Customers',
            fontsize=12, weight='bold')
axes[1, 1].set_xlabel('Number of Customers')
axes[1, 1].set_ylabel('Sales ($)')
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('data_overview.png', dpi=300, bbox_inches='tight')
print("✓ Data overview plots saved as 'data_overview.png'")
print("      ")
# ============================================================================
# 🎯 SUMMARY: What We Learned | ملخص: ما تعلمناه
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You knew Python but not the data science workflow")
print("   - You had heard of pandas but didn't understand DataFrames")
print("   - You didn't know how all data science steps connect")

print("\n✅ AFTER this example:")
print("   - You understand the complete data science lifecycle (9 steps)")
print("   - You can create and work with pandas DataFrames")
print("   - You can create basic visualizations")
print("   - You see how the workflow guides all data science work")

print("\n📚 Key Concepts Covered:")
print("   1. Data Science Lifecycle (9 steps: Problem → Monitoring)")
print("   2. Pandas DataFrames (structured data tables)")
print("   3. Data Exploration (understanding your data)")
print("   4. Basic Visualizations (line plots, histograms, bar charts, scatter plots)")

print("\n🔗 Where Each Step Fits in the Lifecycle:")
print("   - This example covered: Problem Definition, Data Collection,")
print("     Data Exploration, and Initial Analysis")
print("   - Next: Example 2 will dive deeper into data manipulation (pandas/NumPy)")
print("   - Then: Example 3 will show GPU acceleration (cuDF)")

print("\n➡️  Next Steps:")
print("   - Continue to Example 2: Pandas & NumPy Basics")
print("   - You'll learn more about manipulating DataFrames and arrays")
print("   - This builds on what you learned about data structures here!")

print("\n" + "=" * 70)
plt.show()
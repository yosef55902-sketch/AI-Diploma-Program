"""
Unit 3 - Example 9: Interactive Plotly Visualizations | تصورات Plotly التفاعلية



This example teaches how to create interactive visualizations with Plotly.
Learn how interactive plots enable exploration and better data communication.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 8: Seaborn Plots - Understanding static visualizations first
- ✅ Understanding of basic plots (scatter, line, bar)

If you haven't completed these, you might struggle with:
- Understanding what interactivity adds to plots
- Knowing when to use interactive vs static plots
- Understanding Plotly's syntax

## 🔗 Where This Example Fits | مكان هذا المثال

This is the THIRD and FINAL example in Unit 3 - Data Visualization!

Why this example THIRD?
- Before creating interactive plots, understand static plots (matplotlib, Seaborn)
- Interactive plots are more complex - learn basics first
- This completes the visualization unit with the most advanced technique

Builds on: 
- Example 7: Matplotlib Fundamentals (static plots)
- Example 8: Seaborn Plots (statistical plots)

Leads to: 
- Unit 4: Machine Learning (visualize model results interactively)
- Dashboards and presentations (interactive plots are great for sharing)

## The Story: From Photos to Interactive Maps | القصة: من الصور إلى الخرائط التفاعلية

Imagine you're showing a location. A photo shows one view, but an interactive map 
lets people zoom, pan, and explore. After seeing interactivity, people understand better!

Same with visualization: Static plots show one view, but interactive plots let users 
zoom, pan, hover for details, and explore. After experiencing interactivity, data 
communication is much more effective!

## Why Interactive Visualizations Matter | لماذا يهم

Interactive visualizations are powerful because:
- Exploration: Users can zoom, pan, and explore data themselves
- Details: Hover to see exact values and details
- Dashboards: Perfect for live dashboards and presentations
- Engagement: More engaging than static plots
- Sharing: Great for web-based reports and presentations

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Create interactive plots with Plotly
2. Understand when to use interactive vs static plots
3. Create interactive scatter, line, and bar plots
4. Add interactivity features (hover, zoom, pan)
5. Export interactive plots to HTML for sharing
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

print("=" * 70)
print("Example 9: Interactive Plotly Visualizations | تصورات Plotly التفاعلية")
print("=" * 70)
print("\n📚 Prerequisites: Examples 7 & 8 completed, understand static plots")
print("🔗 This is the THIRD example in Unit 3 - interactive visualizations")
print("🎯 Goal: Master Plotly for interactive, engaging visualizations\n")
# ============================================================================
# 1. CREATE SAMPLE DATA
# ============================================================================
print("\n1. Creating Sample Data")
print("-" * 70)
np.random.seed(42)
n_samples = 100
df = pd.DataFrame({
'x': np.random.randn(n_samples),
'y': np.random.randn(n_samples),
'category': np.random.choice(['A', 'B', 'C'], n_samples),
'size': np.random.randint(10, 100, n_samples),
'date': pd.date_range('2024-01-01', periods=n_samples, freq='D'),
'value': np.random.normal(100, 20, n_samples)
})
print(f"✓ Created dataset with {len(df)} rows")
print(df.head())
# ============================================================================
# 2. INTERACTIVE SCATTER PLOT
# ============================================================================
print("\n2. Interactive Scatter Plot")
print("-" * 70)
fig = px.scatter(df, x='x', y='y', color='category', size='size',
hover_data=['value'],
title='Interactive Scatter Plot',
labels={'x': 'X Value', 'y': 'Y Value', 'category': 'Category'})
fig.update_layout(
font=dict(size=12),
title_font_size=16,
width=800,
height=600
)
fig.write_html('11_interactive_scatter.html')
print("✓ Interactive scatter plot saved as HTML")
print("  Open '11_interactive_scatter.html' in browser to view interactively")
# ============================================================================
# 3. INTERACTIVE LINE PLOT
# ============================================================================
print("\n3. Interactive Line Plot")
print("-" * 70)
df_sorted = df.sort_values('date')
fig = px.line(df_sorted, x='date', y='value', color='category',
title='Interactive Line Plot',
labels={'date': 'Date', 'value': 'Value', 'category': 'Category'})
fig.update_traces(mode='lines+markers', marker_size=5)
fig.update_xaxes(rangeslider_visible=True)
fig.write_html('12_interactive_line.html')
print("✓ Interactive line plot saved with range slider")
# ============================================================================
# 4. INTERACTIVE BAR CHART
# ============================================================================
print("\n4. Interactive Bar Chart")
print("-" * 70)
category_values = df.groupby('category')['value'].mean().reset_index()
fig = px.bar(category_values, x='category', y='value',
title='Interactive Bar Chart',
labels={'category': 'Category', 'value': 'Average Value'},
color='category',
text='value')
fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
fig.update_layout(showlegend=False)
fig.write_html('13_interactive_bar.html')
print("✓ Interactive bar chart saved")
# ============================================================================
# 5. MULTI-PANEL DASHBOARD
# ============================================================================
print("\n5. Multi Panel Dashboard")
print("-" * 70)
fig = make_subplots(
rows=2, cols=2,
subplot_titles=('Scatter Plot', 'Line Plot', 'Bar Chart', 'Distribution'),
specs=[[{"secondary_y": False}, {"secondary_y": False}],
[{"secondary_y": False}, {"type": "histogram"}]]
)
# Scatter
fig.add_trace(
go.Scatter(x=df['x'], y=df['y'], mode='markers',
marker=dict(color=df['value'], colorscale='Viridis', size=8),
name='Scatter'),
row=1, col=1
)
# Line
fig.add_trace(
go.Scatter(x=df_sorted['date'], y=df_sorted['value'],
mode='lines+markers', name='Line'),
row=1, col=2
)
# Bar
fig.add_trace(
go.Bar(x=category_values['category'], y=category_values['value'],
name='Bar'),
row=2, col=1
)
# Histogram
fig.add_trace(
go.Histogram(x=df['value'], nbinsx=20, name='Distribution'),
row=2, col=2
)
fig.update_layout(
height=800,
title_text="Interactive Dashboard",
showlegend=True
)
fig.write_html('14_interactive_dashboard.html')
print("✓ Interactive dashboard saved")
# ============================================================================
# 6. 3D SCATTER PLOT
# ============================================================================
print("\n6. 3D Scatter Plot")
print("-" * 70)
z = np.random.randn(n_samples)
fig = px.scatter_3d(df, x='x', y='y', z=z, color='category',
size='size', hover_data=['value'],
title='3D Scatter Plot')
fig.write_html('15_3d_scatter.html')
print("✓ 3D scatter plot saved")
# ============================================================================
# 7. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You could create static plots but not interactive ones")
print("   - You didn't know how to create engaging, explorable visualizations")
print("   - You couldn't create dashboards or web-based visualizations")

print("\n✅ AFTER this example:")
print("   - You can create interactive plots with Plotly (zoom, pan, hover)")
print("   - You can create engaging visualizations for dashboards")
print("   - You can export interactive plots to HTML for sharing")
print("   - You know when to use interactive vs static plots")

print("\n📚 Key Concepts Covered:")
print("   1. Interactive Plots (zoom, pan, hover, explore)")
print("   2. Plotly Express (easy, high-level interface)")
print("   3. Plotly Graph Objects (powerful, low-level control)")
print("   4. Interactive Features (hover tooltips, zoom, selection)")
print("   5. HTML Export (share interactive plots on the web)")

print("\n🔗 Where These Skills Fit:")
print("   - Dashboards: Perfect for live, interactive dashboards")
print("   - Web Reports: Export to HTML for web-based presentations")
print("   - Data Exploration: Let users explore data themselves")
print("   - Presentations: More engaging than static plots")

print("\n➡️  Next Steps:")
print("   - Continue to Unit 4: Introduction to Machine Learning")
print("   - You'll learn ML algorithms and use visualization for model results")
print("   - Interactive plots are great for visualizing model predictions!")

print("\n✅ Unit 3 (Visualization) COMPLETE!")
print("   - You've mastered matplotlib (static plots)")
print("   - You've mastered Seaborn (statistical plots)")
print("   - You've mastered Plotly (interactive plots)")

print("\n" + "=" * 70)
print("\nKey Concepts Covered:")
print("1. Interactive scatter plots with hover information")
print("        ")
print("2. Interactive line plots with range sliders")
print("        ")
print("3. Interactive bar charts")
print("     ")
print("4. Multi-panel dashboards")
print("      ")
print("5. 3D visualizations")
print("     ")
print("\nNote: Plotly HTML files can be opened in any web browser")
print(":    Plotly HTML    ")
print("\nNext Steps: Continue to Unit 4 for Machine Learning")
print(" :    4  ")
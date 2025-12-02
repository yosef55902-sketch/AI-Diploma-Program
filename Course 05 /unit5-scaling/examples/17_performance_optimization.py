"""
Unit 5 - Example 17: Performance Optimization | تحسين الأداء

This example teaches how to profile and optimize data science code performance.
Learn to identify bottlenecks and make code faster.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 4: Machine Learning - Understand data science workflows
- ✅ Basic understanding of performance concepts

If you haven't completed these, you might struggle with:
- Understanding what makes code slow
- Knowing how to measure performance
- Understanding optimization techniques

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FOURTH example in Unit 5 - Scaling Data Science!

Why this example FOURTH?
- After learning scaling techniques, learn to optimize them
- Performance optimization makes code faster
- Essential before deployment (fast code = better user experience)

Builds on: 
- Example 14, 15, 16: Scaling workflows (optimize these)

Leads to: 
- Example 18: Large Datasets (optimize for large data)
- Example 19: Deployment (optimized code deploys better)

## The Story: Making Things Faster | القصة: جعل الأشياء أسرع

Imagine you have a car. Optimization is like tuning it - finding what's slow, fixing 
bottlenecks, making everything faster. After optimization, your car (code) runs much faster!

Same with code: Profiling finds slow parts, optimization makes them fast. After learning 
optimization, your code runs efficiently!

## Why Performance Optimization Matters | لماذا يهم

Performance optimization is essential because:
- Speed: Faster code = better user experience
- Cost: Faster code = lower compute costs
- Scalability: Optimized code scales better
- Resources: Use hardware efficiently

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Profile code to find bottlenecks
2. Measure performance accurately
3. Optimize data processing operations
4. Identify optimization opportunities
5. Apply optimization best practices
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import cProfile
import pstats
from io import StringIO
print("=" * 70)
print("Example 17: Performance Optimization")
print(" 17:  ")
print("=" * 70)
# ============================================================================
# 1. CREATE DATASET FOR OPTIMIZATION DEMO
# ============================================================================
print("\n1. Creating Dataset")
print("-" * 70)
np.random.seed(42)
n_samples = 100000
data = {
'id': range(n_samples),
'value1': np.random.randn(n_samples),
'value2': np.random.randn(n_samples),
'category': np.random.choice(['A', 'B', 'C', 'D'], n_samples),
'score': np.random.randint(0, 100, n_samples)
}
df = pd.DataFrame(data)
print(f"✓ Created dataset with {len(df):,} rows")
# ============================================================================
# 2. PERFORMANCE PROFILING
# ============================================================================
print("\n\n2. Performance Profiling")
print("-" * 70)
def slow_operation(df):
    """Inefficient operation"""
    result = []
    for idx, row in df.iterrows():
        result.append(row['value1'] * row['value2'])
    return pd.Series(result)
def fast_operation(df):
    """Optimized operation"""
    return df['value1'] * df['value2']
# Profile slow operation
print("\nProfiling slow operation (iterrows)...")
start_time = time.time()
result_slow = slow_operation(df.head(1000))  # Use subset for demo
slow_time = time.time() - start_time
print(f"Slow operation time: {slow_time:.4f} seconds")
# Profile fast operation
print("\nProfiling fast operation (vectorized)...")
start_time = time.time()
result_fast = fast_operation(df.head(1000))
fast_time = time.time() - start_time
print(f"Fast operation time: {fast_time:.4f} seconds")
print(f"Speedup: {slow_time/fast_time:.2f}x")
# ============================================================================
# 3. MEMORY OPTIMIZATION
# ============================================================================
print("\n\n3. Memory Optimization")
print("-" * 70)
print("\nOriginal memory usage:")
print(f"Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
# Optimize data types
df_optimized = df.copy()
df_optimized['score'] = df_optimized['score'].astype('int8')
df_optimized['category'] = df_optimized['category'].astype('category')
print("\nOptimized memory usage:")
print(f"Memory: {df_optimized.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Reduction: {(1 - df_optimized.memory_usage(deep=True).sum() / df.memory_usage(deep=True).sum()) * 100:.1f}%")
# ============================================================================
# 4. VISUALIZATION
# ============================================================================
print("\n\n4. Creating Optimization Visualization")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Performance Optimization')
# Speed comparison
ops = ['Iterrows\n()', 'Vectorized\n()']
times = [slow_time, fast_time]
colors = ['#FF6B6B', '#4ECDC4']
axes[0].bar(ops, times, color=colors, edgecolor='black')
axes[0].set_ylabel('Time (seconds)')
axes[0].set_title('Operation Speed Comparison',
fontsize=12, weight='bold')
axes[0].grid(True, alpha=0.3, axis='y')
# Memory comparison
memory_original = df.memory_usage(deep=True).sum() / 1024**2
memory_optimized = df_optimized.memory_usage(deep=True).sum() / 1024**2
axes[1].bar(['Original\n', 'Optimized\n'],
[memory_original, memory_optimized],
color=['#FF6B6B', '#4ECDC4'], edgecolor='black')
axes[1].set_ylabel('Memory (MB)')
axes[1].set_title('Memory Usage Comparison',
fontsize=12, weight='bold')
axes[1].grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('17_optimization.png', dpi=300, bbox_inches='tight')
print("✓ Optimization visualization saved")
plt.close()
# ============================================================================
# 5. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Performance profiling")
print("2. Identifying bottlenecks")
print("3. Vectorization")
print("4. Memory optimization")
print("\nNext Steps: Continue to Example 18 for Large Dataset Handling")
print(" :    18     ")
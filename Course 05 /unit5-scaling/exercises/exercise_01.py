"""
Unit 5 - Exercise 1: Scaling Data Science Practice
تمرين 1: ممارسة توسيع نطاق علم البيانات

Instructions:
1. Work with large datasets using chunking
2. Optimize data processing
3. Use Dask for distributed computing (if available)
4. Profile and optimize code performance
"""

import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Generate large dataset
np.random.seed(42)
print("Generating large dataset...")
large_data = pd.DataFrame({
    'id': range(1, 100001),
    'value1': np.random.randn(100000),
    'value2': np.random.randn(100000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000),
    'score': np.random.uniform(0, 100, 100000)
})

# TODO: Write your code here

# Task 1: Process large dataset efficiently
print("=" * 60)
print("Task 1: Efficient Processing")
print("=" * 60)
# Your code here...
# - Process data in chunks
# - Use memory-efficient operations
# - Measure processing time

# Task 2: Data aggregation on large dataset
print("\n" + "=" * 60)
print("Task 2: Aggregation")
print("=" * 60)
# Your code here...
# - Group by category and calculate statistics
# - Use efficient aggregation methods
# - Measure performance

# Task 3: Memory optimization
print("\n" + "=" * 60)
print("Task 3: Memory Optimization")
print("=" * 60)
# Your code here...
# - Optimize data types
# - Reduce memory usage
# - Compare before/after memory usage

# Task 4: Performance profiling
print("\n" + "=" * 60)
print("Task 4: Performance Profiling")
print("=" * 60)
# Your code here...
# - Profile different operations
# - Identify bottlenecks
# - Optimize slow operations

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)


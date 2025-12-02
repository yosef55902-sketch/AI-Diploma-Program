"""
Unit 2 - Example 4: Advanced Data Loading | تحميل البيانات المتقدم

This example teaches advanced techniques for loading data from various sources.
Learn how to load CSV, Excel, JSON files and handle large datasets efficiently.

All concepts are explained in the code comments below - you can learn everything
from this code example alone!

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 1: All examples (pandas, NumPy, cuDF basics)
- ✅ Understanding of DataFrames and basic file operations
- ✅ Knowledge of different file formats (CSV, Excel, JSON)

If you haven't completed these, you might struggle with:
- Understanding DataFrame operations
- Knowing which loading method to use
- Handling file paths and errors

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIRST example in Unit 2 - Data Cleaning and Preparation!

Why this example FIRST in Unit 2?
- Before you can clean data, you need to load it from files
- Before you can analyze data, you need to load it correctly
- Before you can handle large datasets, you need chunking strategies

Builds on: 
- Unit 1: pandas DataFrame knowledge

Leads to: 
- Example 5: Missing Values & Duplicates (needs data loading skills)
- Example 6: Outliers & Transformation (needs loaded data)
- All cleaning operations (all need data loaded first!)

## The Story: Getting Your Ingredients | القصة: الحصول على المكونات

Imagine you're cooking. Before you can clean and prepare ingredients, you need to get 
them from the store - know what's available, handle different packages, check if items 
are missing. After getting everything loaded, you can start preparing!

Same with data science: Before cleaning and analyzing, we load data from files - know 
file formats, handle different sources, check for errors. After loading successfully, 
we can start cleaning!

## Why Advanced Data Loading Matters | لماذا يهم تحميل البيانات المتقدم

Advanced loading techniques are essential because:
- Multiple Formats: Real data comes in CSV, Excel, JSON, databases
- Large Files: Need chunking to load huge datasets that don't fit in memory
- Error Handling: Files may be missing, corrupted, or have encoding issues
- Performance: Correct loading options make your code faster

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Load data from CSV files with advanced options
2. Load data from Excel files and multiple sheets
3. Load data from JSON files (including nested structures)
4. Handle large files using chunking techniques
5. Implement error handling for robust data loading
"""
import pandas as pd
import numpy as np
import json
import os
from pathlib import Path

print("=" * 70)
print("Example 4: Advanced Data Loading | تحميل البيانات المتقدم")
print("=" * 70)
print("\n📚 Prerequisites: Unit 1 completed, pandas DataFrame knowledge")
print("🔗 This is the FIRST example in Unit 2 - foundation for data cleaning")
print("🎯 Goal: Master loading data from multiple sources and formats\n")
# ============================================================================
# PART 1: LOADING FROM CSV - The Most Common Format
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: Loading from CSV Files")
print("=" * 70)

print("\n📋 BEFORE: You know basic pd.read_csv() but not advanced options")
print("📋 AFTER: You can load CSV with encoding, date parsing, and error handling")
print("💡 WHY THIS MATTERS: CSV is the most common format - master it first!\n")

print("\n1. Loading from CSV")
print("-" * 70)

# Create sample CSV data
# Why create sample data? Practice with realistic examples before loading real files
sample_data = {
'id': range(1, 101),
'name': [f'Person_{i}' for i in range(1, 101)],
'age': np.random.randint(18, 80, 100),
'salary': np.random.normal(50000, 15000, 100),
'department': np.random.choice(['IT', 'HR', 'Finance', 'Sales'], 100),
'join_date': pd.date_range('2020-01-01', periods=100, freq='D')
}
df_sample = pd.DataFrame(sample_data)
csv_file = 'unit2-cleaning/examples/sample_data.csv'
os.makedirs(os.path.dirname(csv_file), exist_ok=True)
df_sample.to_csv(csv_file, index=False)
print(f"✓ Created sample CSV file: {csv_file}")
# Load CSV with different options
# Why default first? See what happens without options - sometimes it's enough!
print("\n📌 Loading CSV with default options:")
df1 = pd.read_csv(csv_file)
print(f"   Shape: {df1.shape}")
print("   Why default? Simple cases don't need options - keep it simple!")

print("\n📌 Loading CSV with advanced options:")
# Why encoding='utf-8'? Handles international characters correctly
# Why na_values? Treat empty strings and 'NULL' as missing values (not strings)
# Why parse_dates? Convert date strings to actual dates (enables date operations)
df2 = pd.read_csv(csv_file,
                  encoding='utf-8',
                  na_values=['', 'NULL', 'null'],
                  parse_dates=['join_date'])
print(f"   Shape: {df2.shape}")
print("   Why options? Handle edge cases - encoding, missing values, dates!")
# ============================================================================
# 2. LOAD FROM EXCEL
# ============================================================================
print("\n\n2. Loading from Excel")
print("-" * 70)
excel_file = 'unit2-cleaning/examples/sample_data.xlsx'
df_sample.to_excel(excel_file, index=False, sheet_name='Employees')
print(f"✓ Created sample Excel file: {excel_file}")
# Load Excel file
print("\nLoading Excel file")
df_excel = pd.read_excel(excel_file, sheet_name='Employees')
print(f"Shape: {df_excel.shape}")
print(f"Columns: {list(df_excel.columns)}")
# Load specific sheet
print("\nLoading specific sheet")
df_excel2 = pd.read_excel(excel_file, sheet_name=0)  # First sheet
print(f"Shape: {df_excel2.shape}")
# ============================================================================
# 3. LOAD FROM JSON
# ============================================================================
print("\n\n3. Loading from JSON")
print("-" * 70)
# Create sample JSON data
json_data = {
'employees': [
{'id': i, 'name': f'Employee_{i}', 'age': np.random.randint(25, 55)}
for i in range(1, 21)
]
}
json_file = 'unit2-cleaning/examples/sample_data.json'
with open(json_file, 'w') as f:
    json.dump(json_data, f, indent=2)
print(f"✓ Created sample JSON file: {json_file}")
# Load JSON
print("\nLoading JSON file")
df_json = pd.read_json(json_file)
print(f"Shape: {df_json.shape}")
# Load JSON with nested structure
df_json2 = pd.json_normalize(json_data, record_path='employees')
print(f"\nNormalized JSON shape: {df_json2.shape}")
# ============================================================================
# 4. HANDLING LARGE FILES (CHUNKING)
# ============================================================================
print("\n\n4. Handling Large Files (Chunking)")
print("-" * 70)
# Create larger dataset
large_data = {
'id': range(1, 100001),
'value': np.random.randn(100000),
'category': np.random.choice(['A', 'B', 'C'], 100000)
}
df_large = pd.DataFrame(large_data)
large_csv = 'unit2-cleaning/examples/large_data.csv'
df_large.to_csv(large_csv, index=False)
print(f"✓ Created large CSV file: {large_csv} ({len(df_large):,} rows)")
# Load in chunks
print("\nLoading in chunks")
chunk_size = 10000
chunks = []
for chunk in pd.read_csv(large_csv, chunksize=chunk_size):
    chunks.append(chunk)
    print(f"  Loaded chunk with {len(chunk)} rows")
df_chunked = pd.concat(chunks, ignore_index=True)
print(f"\n✓ Total rows loaded: {len(df_chunked):,}")
# ============================================================================
# 5. ERROR HANDLING
# ============================================================================
print("\n\n5. Error Handling During Loading")
print("-" * 70)
def safe_load_csv(filepath, **kwargs):
    """Safely load CSV with error handling"""
    try:
        df = pd.read_csv(filepath, **kwargs)
        print(f"✓ Successfully loaded {len(df)} rows from {filepath}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File {filepath} not found")
        return None
    except pd.errors.EmptyDataError:
        print(f"✗ Error: File {filepath} is empty")
        return None
    except Exception as e:
        print(f"✗ Error loading {filepath}: {str(e)}")
        return None
# Test error handling
print("\nTesting error handling")
safe_load_csv('nonexistent_file.csv')
safe_load_csv(csv_file)  # Should succeed
# ============================================================================
# 🎯 SUMMARY: What We Learned | ملخص: ما تعلمناه
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You knew basic pd.read_csv() but not advanced options")
print("   - You couldn't load Excel or JSON files")
print("   - You didn't know how to handle large files")

print("\n✅ AFTER this example:")
print("   - You can load CSV with encoding, date parsing, and custom options")
print("   - You can load Excel files and work with multiple sheets")
print("   - You can load JSON files and handle nested structures")
print("   - You can handle large files using chunking")
print("   - You can implement error handling for robust loading")

print("\n📚 Key Concepts Covered:")
print("   1. CSV Loading (advanced options: encoding, na_values, parse_dates)")
print("   2. Excel Loading (multiple sheets, specific sheet selection)")
print("   3. JSON Loading (normal JSON and nested structures)")
print("   4. Large File Handling (chunking for memory efficiency)")
print("   5. Error Handling (robust loading with try/except)")

print("\n🔗 Where These Skills Fit:")
print("   - CSV: Most common format - master this first")
print("   - Excel: Common in business - often need to work with Excel files")
print("   - JSON: API responses, web data - essential for modern data science")
print("   - Chunking: Essential for big data that doesn't fit in memory")
print("   - Error Handling: Production code must handle failures gracefully")

print("\n➡️  Next Steps:")
print("   - Continue to Example 5: Missing Values & Duplicates")
print("   - You'll learn how to clean the data you just loaded")
print("   - Cleaning is the next step after loading!")

print("\n✓ Sample files created in 'unit2-cleaning/examples' directory")
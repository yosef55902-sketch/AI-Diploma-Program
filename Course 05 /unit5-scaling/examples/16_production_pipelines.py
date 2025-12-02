"""
Unit 5 - Example 16: Production Pipelines | خطوط الأنابيب الإنتاجية

This example teaches how to build production-ready data science pipelines.
Learn error handling, logging, and best practices for production code.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 4: Machine Learning - Understand ML workflows
- ✅ Example 14 & 15: Scaling techniques - Understand distributed/GPU workflows
- ✅ Understanding of Python best practices

If you haven't completed these, you might struggle with:
- Understanding production requirements
- Knowing how to structure production code
- Understanding error handling and logging

## 🔗 Where This Example Fits | مكان هذا المثال

This is the THIRD example in Unit 5 - Scaling Data Science!

Why this example THIRD?
- Before deployment, understand production pipelines
- Production code needs error handling, logging, structure
- Foundation for deploying models to production

Builds on: 
- Example 14: Dask (distributed pipelines)
- Example 15: RAPIDS (GPU workflows)
- Unit 4: ML workflows

Leads to: 
- Example 19: Deployment (deploy production pipelines)
- Production systems (real-world deployment)

## The Story: Building for Production | القصة: البناء للإنتاج

Imagine building a house vs a model. Production code is like building a real house - 
needs foundations (error handling), utilities (logging), and durability (testing). 
After learning production pipelines, your code works reliably in production!

Same with data science: Production pipelines need structure, error handling, and logging. 
After learning production pipelines, your code works reliably for real users!

## Why Production Pipelines Matter | لماذا يهم

Production pipelines are essential because:
- Reliability: Handle errors gracefully (don't crash)
- Monitoring: Log everything (know what's happening)
- Maintainability: Structured code (easy to update)
- Scalability: Work reliably at scale

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Build production-ready pipelines with error handling
2. Implement logging for monitoring and debugging
3. Structure code for maintainability
4. Handle edge cases and errors gracefully
5. Prepare code for deployment
"""
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Imputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging
import json
from datetime import datetime
# Configure logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler('unit5-scaling/examples/pipeline.log'),
logging.StreamHandler()
]
)
logger = logging.getLogger(__name__)
print("=" * 70)
print("Example 16: Production Pipelines")
print(" 16:  ")
print("=" * 70)
# ============================================================================
# 1. CREATE SAMPLE DATA
# ============================================================================
print("\n1. Creating Sample Data")
print("-" * 70)
np.random.seed(42)
n_samples = 1000
data = {
'feature1': np.random.randn(n_samples),
'feature2': np.random.randn(n_samples),
'feature3': np.random.randn(n_samples),
'target': np.random.randn(n_samples)
}
df = pd.DataFrame(data)
# Introduce some missing values
missing_indices = np.random.choice(df.index, size=50, replace=False)
df.loc[missing_indices[:25], 'feature1'] = np.nan
df.loc[missing_indices[25:], 'feature2'] = np.nan
print(f"✓ Created dataset with {len(df)} rows")
print(f"✓ Missing values: {df.isnull().sum().sum()}")
# ============================================================================
# 2. BUILD PRODUCTION PIPELINE
# ============================================================================
print("\n\n2. Building Production Pipeline")
print("-" * 70)
try:
    logger.info("Starting pipeline execution")
    # Prepare data
    X = df[['feature1', 'feature2', 'feature3']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    logger.info(f"Train set: {len(X_train)} samples, Test set: {len(X_test)} samples")
    # Create pipeline
    pipeline = Pipeline([
('scaler', StandardScaler()),
('model', LinearRegression())
    ])
    # Train pipeline
    logger.info("Training pipeline...")
    pipeline.fit(X_train, y_train)
    # Make predictions
    y_pred = pipeline.predict(X_test)
    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    logger.info(f"Pipeline trained successfully")
    logger.info(f"MSE: {mse:.4f}, R²: {r2:.4f}")
    print(f"\n✓ Pipeline executed successfully")
    print(f"MSE: {mse:.4f}, R² Score: {r2:.4f}")
except Exception as e:
    logger.error(f"Pipeline execution failed: {str(e)}", exc_info=True)
raise
# ============================================================================
# 3. SAVE PIPELINE METADATA
# ============================================================================
print("\n\n3. Saving Pipeline Metadata")
print("-" * 70)
metadata = {
'pipeline_version': '1.0',
'created_at': datetime.now().isoformat(),
'train_samples': len(X_train),
'test_samples': len(X_test),
'metrics': {
'mse': float(mse),
'r2': float(r2)
},
'features': list(X.columns)
}
with open('unit5-scaling/examples/pipeline_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print("✓ Pipeline metadata saved")
print("✓     ")
# ============================================================================
# 4. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Pipeline design and structure")
print("2. Error handling and logging")
print("3. Metadata and versioning")
print("4. Production best practices")
print("\nNext Steps: Continue to Example 17 for Performance Optimization")
print(" :    17  ")
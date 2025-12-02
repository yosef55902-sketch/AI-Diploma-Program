"""
Unit 5 - Example 19: Deployment & Monitoring | النشر والمراقبة

This example teaches how to deploy machine learning models to production.
Learn deployment strategies, model versioning, and monitoring.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ All previous examples - Complete data science workflow knowledge
- ✅ Example 16: Production Pipelines - Understand production code
- ✅ Understanding of deployment concepts

If you haven't completed these, you might struggle with:
- Understanding deployment strategies
- Knowing how to monitor models
- Understanding production requirements

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SIXTH and FINAL example in Unit 5 - Scaling Data Science!

Why this example LAST?
- After learning all scaling techniques, learn to deploy them
- Deployment is the final step - getting models to users
- This completes the entire course workflow

Builds on: 
- All previous examples (complete data science knowledge)
- Example 16: Production Pipelines (production code structure)

Leads to: 
- Real-world deployment (deploy your own models)
- Production ML systems (production career)

## The Story: Launching Your Product | القصة: إطلاق منتجك

Imagine you built a product. Deployment is like launching it - making it available to 
users, monitoring how it performs, fixing issues. After deployment, your work reaches users!

Same with ML: Deployment makes models available to users, monitoring tracks performance, 
updates fix issues. After learning deployment, you can deploy real ML systems!

## Why Deployment Matters | لماذا يهم

Deployment is essential because:
- Impact: Models only help if they're deployed
- Monitoring: Track model performance in production
- Updates: Deploy improved versions
- Production: Real-world ML systems need deployment

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Deploy ML models to production
2. Implement model versioning
3. Monitor deployed models
4. Handle model updates and rollbacks
5. Understand deployment best practices
"""
import pandas as pd
import numpy as np
import json
import pickle
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
print("=" * 70)
print("Example 19: Deployment & Monitoring")
print(" 19:  ")
print("=" * 70)
# ============================================================================
# 1. TRAIN MODEL FOR DEPLOYMENT
# ============================================================================
print("\n1. Training Model for Deployment")
print("-" * 70)
np.random.seed(42)
n_samples = 1000
X = np.random.randn(n_samples, 3)
y = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + np.random.randn(n_samples) * 0.1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"✓ Model trained successfully")
print(f"MSE: {mse:.4f}, R²: {r2:.4f}")
# ============================================================================
# 2. SAVE MODEL FOR DEPLOYMENT
# ============================================================================
print("\n\n2. Saving Model")
print("-" * 70)
# Save model using pickle
model_path = 'unit5-scaling/examples/deployed_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"✓ Model saved to {model_path}")
# Save model metadata
metadata = {
'model_version': '1.0.0',
'deployed_at': datetime.now().isoformat(),
'training_date': datetime.now().isoformat(),
'metrics': {
'mse': float(mse),
'r2': float(r2)
},
'features': ['feature_0', 'feature_1', 'feature_2'],
'model_type': 'LinearRegression'
}
metadata_path = 'unit5-scaling/examples/model_metadata.json'
with open(metadata_path, 'w') as f:
    json.dump(metadata, f, indent=2)
print(f"✓ Model metadata saved to {metadata_path}")
# ============================================================================
# 3. DEPLOYMENT FUNCTION
# ============================================================================
print("\n\n3. Deployment Function")
print("-" * 70)
def predict(model, features):
    """
    Make predictions using deployed model
    """
    try:
        logger.info(f"Making prediction for {len(features)} samples")
        # Validate input
        if len(features.shape) != 2:
            raise ValueError("Features must be 2D array")
        # Make prediction
        prediction = model.predict(features)
        logger.info(f"Prediction successful: {len(prediction)} results")
        return prediction
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}", exc_info=True)
        raise
# Test deployment function
test_features = X_test[:5]
predictions = predict(model, test_features)
print(f"\n✓ Deployment function tested successfully")
print(f"Sample predictions: {predictions[:3]}")
# ============================================================================
# 4. MONITORING SETUP
# ============================================================================
print("\n\n4. Monitoring Setup")
print("-" * 70)
class ModelMonitor:
    """Simple model monitoring class"""
    def __init__(self):
        self.predictions_log = []
        self.errors_log = []
    
    def log_prediction(self, features, prediction, actual=None):
        """Log prediction for monitoring"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'features': features.tolist() if isinstance(features, np.ndarray) else features,
            'prediction': float(prediction) if np.isscalar(prediction) else prediction.tolist(),
            'actual': float(actual) if actual is not None and np.isscalar(actual) else None
        }
        self.predictions_log.append(log_entry)
        logger.info(f"Logged prediction: {log_entry['prediction']}")
    
    def log_error(self, error_message):
        """Log error for monitoring"""
        error_entry = {
            'timestamp': datetime.now().isoformat(),
            'error': error_message
        }
        self.errors_log.append(error_entry)
        logger.error(f"Logged error: {error_message}")
    
    def get_stats(self):
        """Get monitoring statistics"""
        return {
            'total_predictions': len(self.predictions_log),
            'total_errors': len(self.errors_log),
            'latest_prediction': self.predictions_log[-1] if self.predictions_log else None
        }
monitor = ModelMonitor()
# Simulate monitoring
for i in range(5):
    features = X_test[i:i+1]
    pred = model.predict(features)[0]
actual = y_test.iloc[i] if hasattr(y_test, 'iloc') else y_test[i]
monitor.log_prediction(features[0], pred, actual)
stats = monitor.get_stats()
print(f"\nMonitoring Statistics:")
print(f"  Total predictions: {stats['total_predictions']}")
print(f"  Total errors: {stats['total_errors']}")
# ============================================================================
# 5. DEPLOYMENT CHECKLIST
# ============================================================================
print("\n\n5. Deployment Checklist")
print("-" * 70)
checklist = {
'Model trained and validated': True,
'Model saved and versioned': True,
'Metadata documented': True,
'Error handling implemented': True,
'Logging configured': True,
'Monitoring set up': True,
'Documentation created': True
}
print("\nDeployment Checklist:")
for item, status in checklist.items():
    status_symbol = "✓" if status else "✗"
    print(f"  {status_symbol} {item}")
# ============================================================================
# 6. SUMMARY
# ============================================================================
print("\n\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Model serialization and saving")
print("2. Deployment functions")
print("3. Monitoring and logging")
print("4. Version control")
print("5. Deployment best practices")
print("\n" + "=" * 70)
print("Course Complete! All 19 examples created successfully!")
print(" !      19 !")
print("=" * 70)
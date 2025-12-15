# Implementation Guide | دليل التنفيذ
## Project 01: Implement ML Algorithms from Scratch

---

## Step-by-Step Implementation | التنفيذ خطوة بخطوة

### Step 1: Linear Regression
- Implement gradient descent
- Calculate cost function (MSE)
- Update weights iteratively
- Handle bias term

**Key Formula:**
```
Cost = (1/2m) * Σ(h(x) - y)²
Gradient = (1/m) * X^T * (h(x) - y)
```

---

### Step 2: Logistic Regression
- Implement sigmoid function
- Calculate binary cross-entropy loss
- Apply gradient descent
- Handle regularization

**Key Formula:**
```
Sigmoid: σ(z) = 1 / (1 + e^(-z))
Loss: L = -[y*log(h) + (1-y)*log(1-h)]
```

---

### Step 3: PCA (Principal Component Analysis)
- Calculate covariance matrix
- Find eigenvalues and eigenvectors
- Project data to lower dimensions
- Reconstruct original data

**Key Steps:**
1. Standardize data
2. Calculate covariance matrix
3. Find eigenvectors (principal components)
4. Project data

---

## Code Structure | هيكل الكود

```python
# linear_regression.py
class LinearRegression:
    def fit(self, X, y):
        # Gradient descent
    def predict(self, X):
        # Make predictions

# logistic_regression.py
class LogisticRegression:
    def fit(self, X, y):
        # Gradient descent with sigmoid
    def predict(self, X):
        # Binary predictions

# pca.py
class PCA:
    def fit(self, X):
        # Calculate principal components
    def transform(self, X):
        # Project to lower dimensions
```

---

**See Template folder for starter code!**


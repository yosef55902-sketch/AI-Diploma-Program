"""
Exercise 01: Statistical Inference and Hypothesis Testing

This exercise helps you understand statistical inference methods
used to evaluate machine learning models.

Instructions:
1. Implement statistical tests
2. Understand confidence intervals
3. Apply to model comparison
"""

import numpy as np
from scipy import stats


def compute_confidence_interval(data, confidence=0.95):
    """
    Compute confidence interval for data.
    
    WHY: Quantify uncertainty in predictions
    HOW: Use t-distribution for sample mean
    
    Args:
        data: Sample data
        confidence: Confidence level (default: 0.95 for 95%)
        
    Returns:
        Tuple of (lower_bound, upper_bound)
    """
    # TODO: Compute confidence interval
    # Steps:
    # 1. Calculate sample mean and standard error
    # 2. Get t-critical value for confidence level
    # 3. CI = mean ± t_critical * standard_error
    pass


def t_test_two_samples(sample1, sample2):
    """
    Perform two-sample t-test.
    
    WHY: Compare if two models perform significantly differently
    HOW: t-test compares means of two samples
    
    Args:
        sample1: First sample
        sample2: Second sample
        
    Returns:
        Tuple of (t_statistic, p_value)
    """
    # TODO: Perform two-sample t-test
    # Use scipy.stats.ttest_ind()
    pass


def interpret_p_value(p_value, alpha=0.05):
    """
    Interpret p-value from statistical test.
    
    WHY: Make informed decisions about model differences
    HOW: Compare p-value to significance level
    
    Args:
        p_value: P-value from test
        alpha: Significance level (default: 0.05)
        
    Returns:
        String interpretation
    """
    # TODO: Interpret p-value
    # If p < alpha: significant difference
    # If p >= alpha: no significant difference
    pass


def compare_models(model1_scores, model2_scores, alpha=0.05):
    """
    Compare two models using statistical inference.
    
    Args:
        model1_scores: Performance scores of model 1
        model2_scores: Performance scores of model 2
        alpha: Significance level
        
    Returns:
        Dictionary with comparison results
    """
    # TODO: 
    # 1. Compute means and confidence intervals
    # 2. Perform t-test
    # 3. Interpret results
    # 4. Return comprehensive comparison
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 01: Statistical Inference")
    print("=" * 60)
    
    # Test data
    np.random.seed(42)
    sample1 = np.random.normal(0.85, 0.02, 100)
    sample2 = np.random.normal(0.87, 0.02, 100)
    
    # Test 1: Confidence interval
    print("\n1. Testing compute_confidence_interval:")
    ci = compute_confidence_interval(sample1, confidence=0.95)
    mean = np.mean(sample1)
    print(f"   Sample mean: {mean:.4f}")
    print(f"   95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
    assert ci[0] < mean < ci[1], "Mean should be in CI"
    print("   ✅ Passed!")
    
    # Test 2: t-test
    print("\n2. Testing t_test_two_samples:")
    t_stat, p_value = t_test_two_samples(sample1, sample2)
    print(f"   t-statistic: {t_stat:.4f}")
    print(f"   p-value: {p_value:.4f}")
    assert isinstance(t_stat, float) and isinstance(p_value, float)
    print("   ✅ Passed!")
    
    # Test 3: Interpretation
    print("\n3. Testing interpret_p_value:")
    interpretation = interpret_p_value(p_value)
    print(f"   Interpretation: {interpretation}")
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")

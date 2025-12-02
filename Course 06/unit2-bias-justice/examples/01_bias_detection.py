"""
Unit 2: Bias, Justice, and Discrimination in AI
Example 1: Bias Detection in Machine Learning Models
التحيز والعدالة والتمييز في الذكاء الاصطناعي - مثال 1: اكتشاف التحيز في نماذج تعلم الآلة

This example demonstrates how to detect bias in ML models using fairness metrics.
Note: This example uses synthetic data. In practice, use fairlearn or aif360 libraries.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)

# ============================================================================
# GENERATE SYNTHETIC DATA WITH BIAS
# إنشاء بيانات اصطناعية مع تحيز
# ============================================================================

def generate_biased_data(n_samples=2000):
    """
    Generate synthetic hiring data with inherent bias
    إنشاء بيانات توظيف اصطناعية مع تحيز متأصل
    """
    np.random.seed(42)
    
    # Create synthetic dataset
    # إنشاء مجموعة بيانات اصطناعية
    data = {
        'age': np.random.randint(22, 65, n_samples),
        'experience_years': np.random.randint(0, 20, n_samples),
        'education_level': np.random.choice([1, 2, 3, 4], n_samples, 
                                           p=[0.2, 0.3, 0.3, 0.2]),  # 1-4 scale
        'skill_score': np.random.normal(70, 15, n_samples),
        'group': np.random.choice(['Group_A', 'Group_B'], n_samples, p=[0.5, 0.5])
    }
    
    df = pd.DataFrame(data)
    
    # Introduce bias: Group_B has lower success rates even with similar qualifications
    # إدخال التحيز: المجموعة ب لديها معدلات نجاح أقل حتى مع مؤهلات مماثلة
    bias_factor = np.where(df['group'] == 'Group_B', -0.15, 0)
    
    # Calculate hiring probability (biased)
    # حساب احتمالية التوظيف (متحيزة)
    base_prob = (df['skill_score'] / 100 + 
                 df['experience_years'] / 20 + 
                 df['education_level'] / 4) / 3 + bias_factor
    
    # Add some noise
    base_prob += np.random.normal(0, 0.1, n_samples)
    base_prob = np.clip(base_prob, 0, 1)
    
    # Create binary outcome (hired = 1, not hired = 0)
    df['hired'] = (base_prob > 0.5).astype(int)
    
    return df

# ============================================================================
# BIAS DETECTION FUNCTIONS
# دوال اكتشاف التحيز
# ============================================================================

def calculate_demographic_parity(df, group_col='group', outcome_col='hired'):
    """
    Calculate demographic parity (statistical parity)
    حساب التكافؤ الديموغرافي (التكافؤ الإحصائي)
    
    Demographic Parity: P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups
    """
    groups = df[group_col].unique()
    parity_rates = {}
    
    for group in groups:
        group_data = df[df[group_col] == group]
        positive_rate = group_data[outcome_col].mean()
        parity_rates[group] = positive_rate
    
    # Calculate disparity
    rates = list(parity_rates.values())
    disparity = max(rates) - min(rates)
    
    return parity_rates, disparity

def calculate_equalized_odds(df, group_col='group', outcome_col='hired', 
                             prediction_col='predicted'):
    """
    Calculate equalized odds
    حساب التكافؤ في الاحتمالات
    
    Equalized Odds: P(Ŷ=1|Y=y, A=a) = P(Ŷ=1|Y=y, A=b) for all groups and outcomes
    """
    groups = df[group_col].unique()
    metrics = {}
    
    for group in groups:
        group_data = df[df[group_col] == group]
        
        # True Positive Rate (TPR) / Sensitivity
        tp = ((group_data[outcome_col] == 1) & 
              (group_data[prediction_col] == 1)).sum()
        fn = ((group_data[outcome_col] == 1) & 
              (group_data[prediction_col] == 0)).sum()
        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        # False Positive Rate (FPR)
        fp = ((group_data[outcome_col] == 0) & 
              (group_data[prediction_col] == 1)).sum()
        tn = ((group_data[outcome_col] == 0) & 
              (group_data[prediction_col] == 0)).sum()
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
        
        metrics[group] = {'TPR': tpr, 'FPR': fpr}
    
    # Calculate disparities
    tprs = [m['TPR'] for m in metrics.values()]
    fprs = [m['FPR'] for m in metrics.values()]
    tpr_disparity = max(tprs) - min(tprs)
    fpr_disparity = max(fprs) - min(fprs)
    
    return metrics, tpr_disparity, fpr_disparity

# ============================================================================
# TRAIN MODEL AND DETECT BIAS
# تدريب النموذج واكتشاف التحيز
# ============================================================================

def train_and_analyze_bias(df):
    """Train a model and analyze for bias"""
    # تدريب نموذج وتحليل التحيز
    
    # Prepare features
    X = df[['age', 'experience_years', 'education_level', 'skill_score']]
    y = df['hired']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Add predictions to test data
    test_df = X_test.copy()
    test_df['hired'] = y_test.values
    test_df['predicted'] = y_pred
    test_df['group'] = df.loc[X_test.index, 'group'].values
    
    # Calculate bias metrics
    parity_rates, parity_disparity = calculate_demographic_parity(test_df)
    equalized_odds, tpr_disparity, fpr_disparity = calculate_equalized_odds(test_df)
    
    return test_df, model, parity_rates, parity_disparity, equalized_odds, tpr_disparity, fpr_disparity

# ============================================================================
# VISUALIZATIONS
# التصورات
# ============================================================================

def visualize_demographic_parity(parity_rates, disparity):
    """Visualize demographic parity"""
    # تصور التكافؤ الديموغرافي
    
    groups = list(parity_rates.keys())
    rates = list(parity_rates.values())
    colors = ['#3498db', '#e74c3c']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(groups, rates, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar, rate in zip(bars, rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{rate:.3f}\n({rate*100:.1f}%)',
               ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Add disparity line
    ax.axhline(y=max(rates), color='red', linestyle='--', alpha=0.5, label='Max')
    ax.axhline(y=min(rates), color='blue', linestyle='--', alpha=0.5, label='Min')
    
    ax.set_ylabel('Positive Prediction Rate / معدل التنبؤ الإيجابي', 
                  fontsize=12, fontweight='bold')
    ax.set_title(f'Demographic Parity Analysis\n'
                f'تحليل التكافؤ الديموغرافي\n'
                f'Disparity: {disparity:.3f} / الفرق: {disparity:.3f}',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, max(rates) * 1.2)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('demographic_parity.png',
                dpi=300, bbox_inches='tight')
    print("✅ Saved: demographic_parity.png")
    plt.close()

def visualize_equalized_odds(equalized_odds, tpr_disparity, fpr_disparity):
    """Visualize equalized odds metrics"""
    # تصور مقاييس التكافؤ في الاحتمالات
    
    groups = list(equalized_odds.keys())
    tprs = [equalized_odds[g]['TPR'] for g in groups]
    fprs = [equalized_odds[g]['FPR'] for g in groups]
    
    x = np.arange(len(groups))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars1 = ax.bar(x - width/2, tprs, width, label='True Positive Rate (TPR) / معدل الإيجابي الحقيقي',
                   color='#2ecc71', alpha=0.8, edgecolor='black')
    bars2 = ax.bar(x + width/2, fprs, width, label='False Positive Rate (FPR) / معدل الإيجابي الخاطئ',
                   color='#e74c3c', alpha=0.8, edgecolor='black')
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Group / المجموعة', fontsize=12, fontweight='bold')
    ax.set_ylabel('Rate / المعدل', fontsize=12, fontweight='bold')
    ax.set_title(f'Equalized Odds Analysis\n'
                f'تحليل التكافؤ في الاحتمالات\n'
                f'TPR Disparity: {tpr_disparity:.3f} | FPR Disparity: {fpr_disparity:.3f}',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.legend(fontsize=10)
    ax.set_ylim(0, max(max(tprs), max(fprs)) * 1.2)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('equalized_odds.png',
                dpi=300, bbox_inches='tight')
    print("✅ Saved: equalized_odds.png")
    plt.close()

def visualize_confusion_matrices(test_df):
    """Visualize confusion matrices by group"""
    # تصور مصفوفات الارتباك حسب المجموعة
    
    groups = test_df['group'].unique()
    fig, axes = plt.subplots(1, len(groups), figsize=(14, 5))
    
    for idx, group in enumerate(groups):
        group_data = test_df[test_df['group'] == group]
        cm = confusion_matrix(group_data['hired'], group_data['predicted'])
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                   cbar_kws={'label': 'Count / العدد'})
        axes[idx].set_title(f'{group}\nConfusion Matrix / مصفوفة الارتباك',
                           fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Predicted / المتوقع', fontsize=10)
        axes[idx].set_ylabel('Actual / الفعلي', fontsize=10)
        axes[idx].set_xticklabels(['Not Hired', 'Hired'])
        axes[idx].set_yticklabels(['Not Hired', 'Hired'])
    
    plt.tight_layout()
    plt.savefig('confusion_matrices_by_group.png',
                dpi=300, bbox_inches='tight')
    print("✅ Saved: confusion_matrices_by_group.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# التنفيذ الرئيسي
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Example 1: Bias Detection in ML Models")
    print("الوحدة 2 - مثال 1: اكتشاف التحيز في نماذج تعلم الآلة")
    print("="*80)
    
    # Generate data
    print("\n📊 Generating synthetic data with bias...")
    print("إنشاء بيانات اصطناعية مع تحيز...")
    df = generate_biased_data(n_samples=2000)
    
    # Show data summary
    print("\n📋 Data Summary / ملخص البيانات:")
    print("-" * 60)
    print(f"Total samples: {len(df)}")
    print(f"Groups: {df['group'].value_counts().to_dict()}")
    print(f"\nHiring rates by group:")
    for group in df['group'].unique():
        rate = df[df['group'] == group]['hired'].mean()
        print(f"  {group}: {rate:.3f} ({rate*100:.1f}%)")
    
    # Train model and analyze
    print("\n🔍 Training model and analyzing bias...")
    print("تدريب النموذج وتحليل التحيز...")
    test_df, model, parity_rates, parity_disparity, equalized_odds, tpr_disparity, fpr_disparity = train_and_analyze_bias(df)
    
    # Print results
    print("\n📊 BIAS DETECTION RESULTS / نتائج اكتشاف التحيز:")
    print("="*80)
    
    print("\n1. Demographic Parity / التكافؤ الديموغرافي:")
    print("-" * 60)
    for group, rate in parity_rates.items():
        print(f"  {group}: {rate:.3f} ({rate*100:.1f}%)")
    print(f"\n  Disparity / الفرق: {parity_disparity:.3f}")
    if parity_disparity > 0.1:
        print("  ⚠️  HIGH DISPARITY - Potential bias detected!")
        print("     تحيز محتمل - فرق عالي!")
    else:
        print("  ✅ Low disparity - Fair from demographic parity perspective")
        print("     فرق منخفض - عادل من منظور التكافؤ الديموغرافي")
    
    print("\n2. Equalized Odds / التكافؤ في الاحتمالات:")
    print("-" * 60)
    for group, metrics in equalized_odds.items():
        print(f"  {group}:")
        print(f"    TPR: {metrics['TPR']:.3f}")
        print(f"    FPR: {metrics['FPR']:.3f}")
    print(f"\n  TPR Disparity / فرق TPR: {tpr_disparity:.3f}")
    print(f"  FPR Disparity / فرق FPR: {fpr_disparity:.3f}")
    
    if tpr_disparity > 0.1 or fpr_disparity > 0.1:
        print("  ⚠️  HIGH DISPARITY - Bias in equalized odds!")
        print("     تحيز في التكافؤ في الاحتمالات - فرق عالي!")
    else:
        print("  ✅ Low disparity - Fair from equalized odds perspective")
        print("     فرق منخفض - عادل من منظور التكافؤ في الاحتمالات")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations / إنشاء التصورات...")
    print("="*80)
    
    visualize_demographic_parity(parity_rates, parity_disparity)
    visualize_equalized_odds(equalized_odds, tpr_disparity, fpr_disparity)
    visualize_confusion_matrices(test_df)
    
    print("\n" + "="*80)
    print("✅ Example completed successfully!")
    print("✅ اكتمل المثال بنجاح!")
    print("="*80)
    print("\nKey Takeaways / النقاط الرئيسية:")
    print("1. Multiple fairness metrics can reveal different types of bias")
    print("   (مقاييس الإنصاف المتعددة يمكن أن تكشف أنواعاً مختلفة من التحيز)")
    print("2. Demographic parity and equalized odds measure different aspects")
    print("   (التكافؤ الديموغرافي والتكافؤ في الاحتمالات يقيسان جوانب مختلفة)")
    print("3. It's important to test for bias before and after model deployment")
    print("   (من المهم اختبار التحيز قبل وبعد نشر النموذج)")
    print("="*80 + "\n")


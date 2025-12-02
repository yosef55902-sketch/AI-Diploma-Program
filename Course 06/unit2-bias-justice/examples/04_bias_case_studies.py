"""
Unit 2: Bias, Justice, and Discrimination in AI
Example 4: Bias Case Studies

This example analyzes real-world case studies of bias in AI systems:
- Facial Recognition and Racial Bias
- Gender Bias in Hiring Algorithms
- Predictive Policing and Criminal Justice AI
- Discrimination in Credit Scoring and Lending AI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import warnings
import os
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# CASE STUDY 1: FACIAL RECOGNITION AND RACIAL BIAS
# ============================================================================

def case_study_facial_recognition():
    """
    Analyze bias in facial recognition systems
    """
    print("="*80)
    print("CASE STUDY 1: Facial Recognition and Racial Bias")
    print("="*80)
    
    # Simulated accuracy data by demographic group
    groups = ['White', 'Black', 'Asian', 'Hispanic']
    accuracy_rates = {
        'White': 0.99,
        'Black': 0.65,
        'Asian': 0.88,
        'Hispanic': 0.75
    }
    
    false_positive_rates = {
        'White': 0.01,
        'Black': 0.35,
        'Asian': 0.12,
        'Hispanic': 0.25
    }
    
    print("\nAccuracy Rates by Demographic Group:")
    for group in groups:
        print(f"  {group}: {accuracy_rates[group]:.2%}")
    
    print("\nFalse Positive Rates by Demographic Group:")
    for group in groups:
        print(f"  {group}: {false_positive_rates[group]:.2%}")
    
    # Calculate disparity
    max_acc = max(accuracy_rates.values())
    min_acc = min(accuracy_rates.values())
    disparity = max_acc - min_acc
    
    print(f"\nAccuracy Disparity: {disparity:.2%}")
    print("This represents significant bias against minority groups.")
    
    return groups, accuracy_rates, false_positive_rates

# ============================================================================
# CASE STUDY 2: GENDER BIAS IN HIRING ALGORITHMS
# ============================================================================

def case_study_hiring_bias():
    """
    Analyze gender bias in hiring algorithms
    """
    print("\n" + "="*80)
    print("CASE STUDY 2: Gender Bias in Hiring Algorithms")
    print("="*80)
    
    # Simulated hiring data
    np.random.seed(42)
    n_candidates = 1000
    
    # Generate candidate data
    data = {
        'gender': np.random.choice(['Male', 'Female'], n_candidates, p=[0.5, 0.5]),
        'experience_years': np.random.randint(0, 20, n_candidates),
        'education_level': np.random.choice([1, 2, 3, 4], n_candidates),
        'skill_score': np.random.normal(70, 15, n_candidates)
    }
    
    df = pd.DataFrame(data)
    
    # Introduce bias: Female candidates have lower hiring probability
    base_prob = (df['skill_score'] / 100 + 
                 df['experience_years'] / 20 + 
                 df['education_level'] / 4) / 3
    
    # Bias factor: reduce probability for female candidates
    bias_factor = np.where(df['gender'] == 'Female', -0.15, 0)
    hire_prob = base_prob + bias_factor + np.random.normal(0, 0.05, n_candidates)
    hire_prob = np.clip(hire_prob, 0, 1)
    
    df['hired'] = (hire_prob > 0.5).astype(int)
    
    # Analyze by gender
    print("\nHiring Rates by Gender:")
    for gender in ['Male', 'Female']:
        gender_data = df[df['gender'] == gender]
        hire_rate = gender_data['hired'].mean()
        avg_skill = gender_data['skill_score'].mean()
        print(f"  {gender}:")
        print(f"    Hiring Rate: {hire_rate:.2%}")
        print(f"    Average Skill Score: {avg_skill:.2f}")
    
    # Calculate disparity
    male_rate = df[df['gender'] == 'Male']['hired'].mean()
    female_rate = df[df['gender'] == 'Female']['hired'].mean()
    disparity = male_rate - female_rate
    
    print(f"\nHiring Rate Disparity: {disparity:.2%}")
    print("This indicates gender bias in the hiring algorithm.")
    
    return df

# ============================================================================
# CASE STUDY 3: PREDICTIVE POLICING AND CRIMINAL JUSTICE AI
# ============================================================================

def case_study_predictive_policing():
    """
    Analyze bias in predictive policing systems
    """
    print("\n" + "="*80)
    print("CASE STUDY 3: Predictive Policing and Criminal Justice AI")
    print("="*80)
    
    # Simulated recidivism prediction data
    np.random.seed(42)
    n_cases = 2000
    
    # Generate data with bias
    data = {
        'race': np.random.choice(['White', 'Black', 'Hispanic'], n_cases, 
                                p=[0.6, 0.25, 0.15]),
        'age': np.random.randint(18, 65, n_cases),
        'prior_convictions': np.random.poisson(2, n_cases),
        'employment_status': np.random.choice([0, 1], n_cases, p=[0.4, 0.6])
    }
    
    df = pd.DataFrame(data)
    
    # True recidivism probability (should be race-neutral)
    true_prob = (df['prior_convictions'] / 10 + 
                 (1 - df['employment_status']) * 0.2 + 
                 np.random.normal(0, 0.1, n_cases))
    
    # Introduce bias: higher false positive rate for minority groups
    bias_factor = np.where(df['race'] == 'Black', 0.15, 
                          np.where(df['race'] == 'Hispanic', 0.10, 0))
    predicted_prob = true_prob + bias_factor
    predicted_prob = np.clip(predicted_prob, 0, 1)
    
    df['true_recidivism'] = (true_prob > 0.5).astype(int)
    df['predicted_high_risk'] = (predicted_prob > 0.5).astype(int)
    
    # Analyze by race
    print("\nPrediction Rates by Race:")
    for race in ['White', 'Black', 'Hispanic']:
        race_data = df[df['race'] == race]
        high_risk_rate = race_data['predicted_high_risk'].mean()
        true_rate = race_data['true_recidivism'].mean()
        print(f"  {race}:")
        print(f"    Predicted High Risk Rate: {high_risk_rate:.2%}")
        print(f"    True Recidivism Rate: {true_rate:.2%}")
        print(f"    Disparity: {high_risk_rate - true_rate:.2%}")
    
    return df

# ============================================================================
# CASE STUDY 4: CREDIT SCORING AND LENDING AI
# ============================================================================

def case_study_credit_scoring():
    """
    Analyze discrimination in credit scoring and lending AI
    """
    print("\n" + "="*80)
    print("CASE STUDY 4: Discrimination in Credit Scoring and Lending AI")
    print("="*80)
    
    # Simulated credit application data
    np.random.seed(42)
    n_applications = 1500
    
    data = {
        'race': np.random.choice(['White', 'Black', 'Hispanic', 'Asian'], 
                                n_applications, p=[0.5, 0.2, 0.2, 0.1]),
        'income': np.random.normal(50000, 20000, n_applications),
        'credit_score': np.random.normal(650, 100, n_applications),
        'debt_to_income': np.random.uniform(0.1, 0.5, n_applications),
        'employment_years': np.random.uniform(0, 20, n_applications)
    }
    
    df = pd.DataFrame(data)
    
    # True creditworthiness (should be race-neutral)
    true_score = (df['credit_score'] / 850 * 0.4 +
                  (1 - df['debt_to_income']) * 0.3 +
                  df['employment_years'] / 20 * 0.2 +
                  df['income'] / 100000 * 0.1 +
                  np.random.normal(0, 0.05, n_applications))
    
    # Introduce bias: lower approval rates for certain groups
    bias_penalty = np.where(df['race'] == 'Black', -0.12,
                           np.where(df['race'] == 'Hispanic', -0.08, 0))
    approval_score = true_score + bias_penalty
    approval_score = np.clip(approval_score, 0, 1)
    
    df['approved'] = (approval_score > 0.5).astype(int)
    df['true_creditworthy'] = (true_score > 0.5).astype(int)
    
    # Analyze by race
    print("\nLoan Approval Rates by Race:")
    for race in ['White', 'Black', 'Hispanic', 'Asian']:
        race_data = df[df['race'] == race]
        approval_rate = race_data['approved'].mean()
        true_rate = race_data['true_creditworthy'].mean()
        avg_credit_score = race_data['credit_score'].mean()
        
        print(f"  {race}:")
        print(f"    Approval Rate: {approval_rate:.2%}")
        print(f"    True Creditworthy Rate: {true_rate:.2%}")
        print(f"    Average Credit Score: {avg_credit_score:.0f}")
        print(f"    Disparity: {approval_rate - true_rate:.2%}")
    
    return df

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_facial_recognition_bias(groups, accuracy_rates, false_positive_rates):
    """
    Plot facial recognition bias analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    acc_values = [accuracy_rates[g] for g in groups]
    fpr_values = [false_positive_rates[g] for g in groups]
    
    axes[0].bar(groups, acc_values, color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
    axes[0].set_title('Facial Recognition Accuracy by Demographic Group', 
                     fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Accuracy Rate')
    axes[0].set_ylim([0, 1])
    axes[0].grid(axis='y', alpha=0.3)
    
    axes[1].bar(groups, fpr_values, color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
    axes[1].set_title('False Positive Rate by Demographic Group', 
                     fontsize=12, fontweight='bold')
    axes[1].set_ylabel('False Positive Rate')
    axes[1].set_ylim([0, 0.4])
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'case_study_facial_recognition.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("\n✅ Saved: case_study_facial_recognition.png")
    plt.close()

def plot_hiring_bias(df):
    """
    Plot hiring bias analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Hiring rates by gender
    gender_rates = df.groupby('gender')['hired'].mean()
    axes[0].bar(gender_rates.index, gender_rates.values, 
               color=['#3498db', '#e74c3c'])
    axes[0].set_title('Hiring Rates by Gender', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Hiring Rate')
    axes[0].set_ylim([0, 1])
    axes[0].grid(axis='y', alpha=0.3)
    
    # Skill score distribution by gender and hiring status
    for gender in ['Male', 'Female']:
        for hired in [0, 1]:
            subset = df[(df['gender'] == gender) & (df['hired'] == hired)]
            axes[1].hist(subset['skill_score'], alpha=0.5, 
                       label=f'{gender} - {"Hired" if hired else "Not Hired"}',
                       bins=20)
    
    axes[1].set_title('Skill Score Distribution by Gender and Hiring Status', 
                     fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Skill Score')
    axes[1].set_ylabel('Frequency')
    axes[1].legend()
    axes[1].grid(alpha=0.3)
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'case_study_hiring_bias.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: case_study_hiring_bias.png")
    plt.close()

def plot_predictive_policing_bias(df):
    """
    Plot predictive policing bias analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Prediction rates by race
    race_pred = df.groupby('race')['predicted_high_risk'].mean()
    race_true = df.groupby('race')['true_recidivism'].mean()
    
    x = np.arange(len(race_pred.index))
    width = 0.35
    
    axes[0].bar(x - width/2, race_pred.values, width, label='Predicted High Risk', 
               alpha=0.8, color='#e74c3c')
    axes[0].bar(x + width/2, race_true.values, width, label='True Recidivism', 
               alpha=0.8, color='#3498db')
    axes[0].set_title('Recidivism Prediction vs Reality by Race', 
                     fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Rate')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(race_pred.index)
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    # Disparity calculation
    disparity = race_pred - race_true
    axes[1].bar(disparity.index, disparity.values, color='#e74c3c')
    axes[1].axhline(y=0, color='black', linestyle='--', linewidth=1)
    axes[1].set_title('Prediction Disparity by Race', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Disparity (Predicted - True)')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'case_study_predictive_policing.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: case_study_predictive_policing.png")
    plt.close()

def plot_credit_scoring_bias(df):
    """
    Plot credit scoring bias analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Approval rates by race
    race_approved = df.groupby('race')['approved'].mean()
    race_true = df.groupby('race')['true_creditworthy'].mean()
    
    x = np.arange(len(race_approved.index))
    width = 0.35
    
    axes[0].bar(x - width/2, race_approved.values, width, label='Approval Rate', 
               alpha=0.8, color='#2ecc71')
    axes[0].bar(x + width/2, race_true.values, width, label='True Creditworthy Rate', 
               alpha=0.8, color='#3498db')
    axes[0].set_title('Loan Approval vs Creditworthiness by Race', 
                     fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Rate')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(race_approved.index, rotation=15)
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    # Average credit score by race
    race_credit = df.groupby('race')['credit_score'].mean()
    axes[1].bar(race_credit.index, race_credit.values, color='#f39c12')
    axes[1].set_title('Average Credit Score by Race', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Credit Score')
    axes[1].set_xticklabels(race_credit.index, rotation=15)
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'case_study_credit_scoring.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: case_study_credit_scoring.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Example 4: Bias Case Studies")
    print("="*80)
    
    # Case Study 1: Facial Recognition
    groups, accuracy_rates, false_positive_rates = case_study_facial_recognition()
    
    # Case Study 2: Hiring Bias
    df_hiring = case_study_hiring_bias()
    
    # Case Study 3: Predictive Policing
    df_policing = case_study_predictive_policing()
    
    # Case Study 4: Credit Scoring
    df_credit = case_study_credit_scoring()
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_facial_recognition_bias(groups, accuracy_rates, false_positive_rates)
    plot_hiring_bias(df_hiring)
    plot_predictive_policing_bias(df_policing)
    plot_credit_scoring_bias(df_credit)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Facial recognition systems show significant accuracy disparities across racial groups")
    print("2. Hiring algorithms can perpetuate gender bias")
    print("3. Predictive policing systems may over-predict risk for minority groups")
    print("4. Credit scoring algorithms can discriminate against certain demographic groups")
    print("5. All these cases highlight the importance of bias detection and mitigation")
    print("="*80 + "\n")


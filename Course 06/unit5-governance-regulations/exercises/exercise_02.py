"""
Unit 5: AI Governance, Regulations, and Future Challenges
Exercise 2: Governance Framework Design

This exercise requires you to design and implement governance frameworks
for AI systems.
"""

import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================================
# TASK 1: Risk Assessment Framework
# ============================================================================

def assess_ai_risk(use_case, data_sensitivity, decision_impact, automation_level):
    """
    TODO: Assess risk level of AI system.
    
    Requirements:
    - Categorize risk based on use case, data sensitivity, decision impact, automation
    - Return risk level (Low, Medium, High, Critical)
    - Provide risk justification
    """
    # TODO: Your code here
    # Hint: Create risk scoring system
    pass

def create_risk_matrix():
    """
    TODO: Create risk assessment matrix.
    
    Requirements:
    - Define risk categories
    - Map use cases to risk levels
    - Return risk matrix
    """
    # TODO: Your code here
    pass

# ============================================================================
# TASK 2: Compliance Checklist
# ============================================================================

def create_gdpr_compliance_checklist():
    """
    TODO: Create GDPR compliance checklist for AI systems.
    
    Requirements:
    - List key GDPR requirements for AI
    - Create checklist items
    - Return checklist DataFrame
    """
    # TODO: Your code here
    # Hint: Include data minimization, purpose limitation, right to explanation, etc.
    pass

def check_compliance_status(checklist, system_info):
    """
    TODO: Check compliance status against checklist.
    
    Requirements:
    - Evaluate system against checklist
    - Return compliance report
    """
    # TODO: Your code here
    pass

# ============================================================================
# TASK 3: Governance Framework Design
# ============================================================================

def design_governance_framework(organization_type='enterprise'):
    """
    TODO: Design governance framework for AI systems.
    
    Requirements:
    - Define governance structure
    - Include roles and responsibilities
    - Define processes and procedures
    - Return framework document
    """
    # TODO: Your code here
    # Hint: Include ethics board, review processes, monitoring, etc.
    pass

def create_ai_ethics_board_structure():
    """
    TODO: Design AI ethics board structure.
    
    Requirements:
    - Define board composition
    - Define responsibilities
    - Define review processes
    - Return board structure
    """
    # TODO: Your code here
    pass

# ============================================================================
# TASK 4: Monitoring and Auditing Framework
# ============================================================================

def design_monitoring_framework():
    """
    TODO: Design monitoring framework for AI systems.
    
    Requirements:
    - Define key metrics to monitor
    - Define monitoring frequency
    - Define alerting thresholds
    - Return monitoring framework
    """
    # TODO: Your code here
    # Hint: Monitor accuracy, fairness, privacy, security
    pass

def create_audit_report(model_performance, fairness_metrics, privacy_compliance):
    """
    TODO: Create comprehensive audit report.
    
    Requirements:
    - Compile performance metrics
    - Include fairness assessment
    - Include privacy compliance
    - Return audit report
    """
    # TODO: Your code here
    pass

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Exercise 2: Governance Framework Design")
    print("="*80)
    
    print("\nSample use cases for analysis:")
    use_cases = [
        {
            'name': 'Healthcare Diagnosis',
            'data_sensitivity': 'High',
            'decision_impact': 'High',
            'automation_level': 'Medium'
        },
        {
            'name': 'Recommendation System',
            'data_sensitivity': 'Medium',
            'decision_impact': 'Low',
            'automation_level': 'High'
        }
    ]
    
    for use_case in use_cases:
        print(f"\n{use_case['name']}:")
        print(f"  Data Sensitivity: {use_case['data_sensitivity']}")
        print(f"  Decision Impact: {use_case['decision_impact']}")
        print(f"  Automation Level: {use_case['automation_level']}")
    
    print("\n" + "="*80)
    print("Complete the TODO sections in this file.")
    print("="*80)


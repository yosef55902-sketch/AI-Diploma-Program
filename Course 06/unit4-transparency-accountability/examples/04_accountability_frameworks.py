"""
Unit 4: Interpretability, Transparency, and Accountability
Example 4: Accountability Frameworks

This example demonstrates accountability frameworks for AI systems:
- Key stakeholders and responsibilities
- Mechanisms for tracking and auditing
- Model cards and data sheets
- Audit trails
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# STAKEHOLDER RESPONSIBILITIES
# ============================================================================

def define_stakeholder_responsibilities():
    """
    Define key stakeholders and their responsibilities in AI accountability
    """
    stakeholders = {
        'Developers': {
            'responsibilities': [
                'Design fair and transparent algorithms',
                'Document model decisions and limitations',
                'Implement bias detection and mitigation',
                'Create model cards and documentation'
            ],
            'accountability_level': 9
        },
        'Data Scientists': {
            'responsibilities': [
                'Ensure data quality and representativeness',
                'Document data sources and preprocessing',
                'Identify potential biases in data',
                'Maintain data lineage'
            ],
            'accountability_level': 8
        },
        'Product Managers': {
            'responsibilities': [
                'Define ethical requirements',
                'Oversee deployment and monitoring',
                'Ensure compliance with regulations',
                'Manage stakeholder communication'
            ],
            'accountability_level': 7
        },
        'Legal/Compliance': {
            'responsibilities': [
                'Ensure regulatory compliance',
                'Review model for legal risks',
                'Handle liability issues',
                'Manage data privacy requirements'
            ],
            'accountability_level': 9
        },
        'End Users': {
            'responsibilities': [
                'Use AI system responsibly',
                'Report issues and biases',
                'Provide feedback',
                'Understand system limitations'
            ],
            'accountability_level': 5
        }
    }
    
    return stakeholders

# ============================================================================
# MODEL CARD TEMPLATE
# ============================================================================

def create_model_card(model_name, model_type, performance_metrics, training_data_info, 
                     limitations, use_cases):
    """
    Create a model card documenting key information about an AI model
    """
    model_card = {
        'model_name': model_name,
        'model_type': model_type,
        'date_created': datetime.now().strftime('%Y-%m-%d'),
        'performance_metrics': performance_metrics,
        'training_data': training_data_info,
        'limitations': limitations,
        'intended_use_cases': use_cases,
        'ethical_considerations': {
            'bias_mitigation': 'Applied reweighing and fairness constraints',
            'transparency': 'SHAP and LIME explanations available',
            'accountability': 'Full audit trail maintained'
        }
    }
    
    return model_card

# ============================================================================
# AUDIT TRAIL
# ============================================================================

def create_audit_trail():
    """
    Create an audit trail for AI system decisions
    """
    audit_entries = []
    
    # Simulate audit trail entries
    base_time = datetime.now() - timedelta(days=30)
    
    events = [
        {'timestamp': base_time, 'event': 'Model trained', 'user': 'Data Scientist', 'details': 'Initial model training'},
        {'timestamp': base_time + timedelta(days=1), 'event': 'Bias check performed', 'user': 'Developer', 'details': 'Demographic parity: 0.05'},
        {'timestamp': base_time + timedelta(days=2), 'event': 'Model deployed', 'user': 'Product Manager', 'details': 'Production deployment'},
        {'timestamp': base_time + timedelta(days=5), 'event': 'Performance monitoring', 'user': 'System', 'details': 'Accuracy: 0.87'},
        {'timestamp': base_time + timedelta(days=10), 'event': 'Bias detected', 'user': 'Monitoring System', 'details': 'Fairness metric degraded'},
        {'timestamp': base_time + timedelta(days=11), 'event': 'Model retrained', 'user': 'Data Scientist', 'details': 'Retraining with fairness constraints'},
        {'timestamp': base_time + timedelta(days=12), 'event': 'Model updated', 'user': 'Product Manager', 'details': 'New version deployed'},
    ]
    
    for event in events:
        audit_entries.append({
            'timestamp': event['timestamp'],
            'event_type': event['event'],
            'user': event['user'],
            'details': event['details']
        })
    
    return pd.DataFrame(audit_entries)

# ============================================================================
# ACCOUNTABILITY FRAMEWORK
# ============================================================================

def accountability_framework_checklist():
    """
    Create accountability framework checklist
    """
    checklist = {
        'Pre-deployment': [
            'Model documentation complete',
            'Bias assessment performed',
            'Fairness metrics calculated',
            'Stakeholder review completed',
            'Legal compliance verified'
        ],
        'Deployment': [
            'Monitoring systems in place',
            'Audit trail enabled',
            'User notifications configured',
            'Rollback plan prepared'
        ],
        'Post-deployment': [
            'Regular performance monitoring',
            'Fairness metrics tracking',
            'User feedback collection',
            'Periodic model audits',
            'Incident response plan'
        ]
    }
    
    return checklist

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_stakeholder_responsibilities(stakeholders):
    """
    Plot stakeholder responsibility matrix
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    names = list(stakeholders.keys())
    accountability = [stakeholders[name]['accountability_level'] for name in names]
    num_responsibilities = [len(stakeholders[name]['responsibilities']) for name in names]
    
    scatter = ax.scatter(num_responsibilities, accountability, s=200, alpha=0.6, c=accountability, 
                        cmap='RdYlGn', edgecolors='black', linewidth=2)
    
    for i, name in enumerate(names):
        ax.annotate(name, (num_responsibilities[i], accountability[i]), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Number of Responsibilities', fontsize=11, fontweight='bold')
    ax.set_ylabel('Accountability Level (1-10)', fontsize=11, fontweight='bold')
    ax.set_title('Stakeholder Accountability Matrix', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3)
    plt.colorbar(scatter, ax=ax, label='Accountability Level')
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/stakeholder_accountability.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: stakeholder_accountability.png")
    plt.close()

def plot_audit_timeline(audit_df):
    """
    Plot audit trail timeline
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Convert timestamps to days since first event
    first_time = audit_df['timestamp'].min()
    audit_df['days_since_start'] = (audit_df['timestamp'] - first_time).dt.days
    
    # Plot events
    event_types = audit_df['event_type'].unique()
    colors = plt.cm.Set3(np.linspace(0, 1, len(event_types)))
    color_map = dict(zip(event_types, colors))
    
    for idx, row in audit_df.iterrows():
        ax.scatter(row['days_since_start'], idx, s=200, 
                 c=color_map[row['event_type']], alpha=0.7, edgecolors='black')
        ax.text(row['days_since_start'], idx, f"  {row['event_type']}", 
               va='center', fontsize=9)
    
    ax.set_xlabel('Days Since First Event', fontsize=11, fontweight='bold')
    ax.set_ylabel('Event Index', fontsize=11, fontweight='bold')
    ax.set_title('AI System Audit Trail Timeline', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=color_map[et], label=et) for et in event_types]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/audit_timeline.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: audit_timeline.png")
    plt.close()

def plot_accountability_checklist(checklist):
    """
    Plot accountability checklist status
    """
    phases = list(checklist.keys())
    items_per_phase = [len(items) for items in checklist.values()]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars = ax.bar(phases, items_per_phase, color=['#3498db', '#2ecc71', '#f39c12'], alpha=0.8)
    
    # Add value labels
    for bar, count in zip(bars, items_per_phase):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{int(count)} items',
               ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Number of Checklist Items', fontsize=11, fontweight='bold')
    ax.set_title('Accountability Framework Checklist by Phase', 
                fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/accountability_checklist.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: accountability_checklist.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 4: Accountability Frameworks")
    print("="*80)
    
    # Define stakeholders
    print("\n1. Stakeholder Responsibilities:")
    stakeholders = define_stakeholder_responsibilities()
    for name, info in stakeholders.items():
        print(f"\n{name}:")
        print(f"  Accountability Level: {info['accountability_level']}/10")
        print(f"  Responsibilities:")
        for resp in info['responsibilities']:
            print(f"    - {resp}")
    
    # Create model card
    print("\n2. Model Card:")
    model_card = create_model_card(
        model_name='Loan Approval Classifier',
        model_type='Random Forest',
        performance_metrics={'accuracy': 0.87, 'fairness_score': 0.92},
        training_data_info={'samples': 10000, 'features': 10, 'date_range': '2023-01 to 2023-12'},
        limitations=['May have bias for certain demographic groups', 'Requires periodic retraining'],
        use_cases=['Loan approval decisions', 'Credit risk assessment']
    )
    print(f"  Model: {model_card['model_name']}")
    print(f"  Created: {model_card['date_created']}")
    print(f"  Performance: {model_card['performance_metrics']}")
    
    # Create audit trail
    print("\n3. Audit Trail:")
    audit_df = create_audit_trail()
    print(f"  Total audit entries: {len(audit_df)}")
    print(f"  Date range: {audit_df['timestamp'].min()} to {audit_df['timestamp'].max()}")
    
    # Accountability checklist
    print("\n4. Accountability Checklist:")
    checklist = accountability_framework_checklist()
    for phase, items in checklist.items():
        print(f"\n{phase}:")
        for item in items:
            print(f"  [ ] {item}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_stakeholder_responsibilities(stakeholders)
    plot_audit_timeline(audit_df)
    plot_accountability_checklist(checklist)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Clear stakeholder responsibilities ensure accountability")
    print("2. Model cards document model characteristics and limitations")
    print("3. Audit trails track all system decisions and changes")
    print("4. Accountability checklists ensure comprehensive coverage")
    print("5. Accountability frameworks are essential for trustworthy AI")
    print("="*80 + "\n")


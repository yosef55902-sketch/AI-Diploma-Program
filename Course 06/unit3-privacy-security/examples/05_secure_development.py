"""
Unit 3: Privacy, Security, and Data Protection
Example 5: Secure AI Development Practices

This example demonstrates secure AI development practices:
- Security vulnerabilities in AI systems
- Secure coding practices
- Security testing
- Incident response
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# SECURITY VULNERABILITIES
# ============================================================================

def identify_security_vulnerabilities():
    """
    Identify common security vulnerabilities in AI systems
    """
    vulnerabilities = {
        'Adversarial Attacks': {
            'severity': 'High',
            'impact': 9,
            'likelihood': 7,
            'description': 'Malicious inputs designed to fool AI models'
        },
        'Model Inversion': {
            'severity': 'High',
            'impact': 8,
            'likelihood': 6,
            'description': 'Reconstructing training data from model outputs'
        },
        'Membership Inference': {
            'severity': 'Medium',
            'impact': 7,
            'likelihood': 7,
            'description': 'Determining if specific data was in training set'
        },
        'Data Poisoning': {
            'severity': 'High',
            'impact': 9,
            'likelihood': 5,
            'description': 'Injecting malicious data into training set'
        },
        'Model Theft': {
            'severity': 'Medium',
            'impact': 6,
            'likelihood': 6,
            'description': 'Stealing model architecture and parameters'
        },
        'Insufficient Access Controls': {
            'severity': 'High',
            'impact': 8,
            'likelihood': 8,
            'description': 'Unauthorized access to models or data'
        }
    }
    return vulnerabilities

# ============================================================================
# SECURE DEVELOPMENT PRACTICES
# ============================================================================

def secure_development_practices():
    """
    Define secure AI development practices
    """
    practices = {
        'Input Validation': {
            'phase': 'Development',
            'importance': 10,
            'implementation': 'Validate and sanitize all inputs'
        },
        'Output Sanitization': {
            'phase': 'Development',
            'importance': 9,
            'implementation': 'Sanitize model outputs before use'
        },
        'Access Control': {
            'phase': 'Deployment',
            'importance': 10,
            'implementation': 'Implement role-based access control'
        },
        'Encryption': {
            'phase': 'All Phases',
            'importance': 10,
            'implementation': 'Encrypt data at rest and in transit'
        },
        'Security Testing': {
            'phase': 'Testing',
            'importance': 9,
            'implementation': 'Regular security audits and penetration testing'
        },
        'Monitoring': {
            'phase': 'Operations',
            'importance': 9,
            'implementation': 'Monitor for anomalies and attacks'
        },
        'Incident Response': {
            'phase': 'Operations',
            'importance': 8,
            'implementation': 'Have response plan for security incidents'
        }
    }
    return practices

# ============================================================================
# SECURITY RISK MATRIX
# ============================================================================

def create_risk_matrix(vulnerabilities):
    """
    Create risk matrix for security vulnerabilities
    """
    risk_matrix = []
    for vuln, info in vulnerabilities.items():
        risk_score = info['impact'] * info['likelihood']
        risk_matrix.append({
            'vulnerability': vuln,
            'impact': info['impact'],
            'likelihood': info['likelihood'],
            'risk_score': risk_score,
            'severity': info['severity']
        })
    return risk_matrix

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_security_vulnerabilities(vulnerabilities):
    """
    Plot security vulnerabilities analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    vuln_names = list(vulnerabilities.keys())
    impacts = [v['impact'] for v in vulnerabilities.values()]
    likelihoods = [v['likelihood'] for v in vulnerabilities.values()]
    
    # Risk matrix
    scatter = axes[0].scatter(likelihoods, impacts, s=300, alpha=0.7, 
                             c=impacts, cmap='RdYlGn_r', edgecolors='black', linewidth=2)
    for i, name in enumerate(vuln_names):
        axes[0].annotate(name, (likelihoods[i], impacts[i]), 
                        xytext=(5, 5), textcoords='offset points', fontsize=8)
    axes[0].set_xlabel('Likelihood (1-10)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Impact (1-10)', fontsize=11, fontweight='bold')
    axes[0].set_title('Security Risk Matrix', fontsize=12, fontweight='bold')
    axes[0].grid(alpha=0.3)
    axes[0].set_xlim([0, 11])
    axes[0].set_ylim([0, 11])
    plt.colorbar(scatter, ax=axes[0], label='Impact')
    
    # Severity distribution
    severity_counts = {}
    for v in vulnerabilities.values():
        sev = v['severity']
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
    
    colors = {'High': '#e74c3c', 'Medium': '#f39c12', 'Low': '#2ecc71'}
    axes[1].bar(severity_counts.keys(), severity_counts.values(), 
               color=[colors[s] for s in severity_counts.keys()], alpha=0.8)
    axes[1].set_title('Vulnerability Severity Distribution', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Count')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/security_vulnerabilities.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: security_vulnerabilities.png")
    plt.close()

def plot_secure_practices(practices):
    """
    Plot secure development practices by phase
    """
    phases = {}
    for practice, info in practices.items():
        phase = info['phase']
        if phase not in phases:
            phases[phase] = []
        phases[phase].append((practice, info['importance']))
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    y_pos = 0
    colors = ['#3498db', '#2ecc71', '#f39c12', '#9b59b6']
    color_idx = 0
    
    for phase, items in phases.items():
        practices_list = [item[0] for item in items]
        importance_list = [item[1] for item in items]
        
        x_start = y_pos
        for i, (practice, importance) in enumerate(items):
            ax.barh(y_pos, importance, left=0, color=colors[color_idx % len(colors)], 
                   alpha=0.7, edgecolor='black')
            ax.text(importance/2, y_pos, practice, ha='center', va='center', 
                   fontsize=9, fontweight='bold')
            y_pos += 1
        
        # Add phase label
        ax.text(-0.5, (x_start + y_pos - 1) / 2, phase, ha='right', va='center',
               fontsize=10, fontweight='bold', rotation=0)
        y_pos += 0.5
        color_idx += 1
    
    ax.set_xlabel('Importance (1-10)', fontsize=11, fontweight='bold')
    ax.set_title('Secure Development Practices by Phase', fontsize=12, fontweight='bold')
    ax.set_xlim([0, 11])
    ax.grid(axis='x', alpha=0.3)
    ax.set_yticks([])
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/secure_practices.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: secure_practices.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Example 5: Secure AI Development Practices")
    print("="*80)
    
    # Security Vulnerabilities
    print("\n1. Security Vulnerabilities in AI Systems:")
    vulnerabilities = identify_security_vulnerabilities()
    for vuln, info in vulnerabilities.items():
        print(f"\n{vuln}:")
        print(f"  Severity: {info['severity']}")
        print(f"  Impact: {info['impact']}/10")
        print(f"  Likelihood: {info['likelihood']}/10")
        print(f"  Description: {info['description']}")
    
    # Secure Practices
    print("\n" + "="*80)
    print("2. Secure Development Practices:")
    print("="*80)
    practices = secure_development_practices()
    for practice, info in practices.items():
        print(f"\n{practice} ({info['phase']}):")
        print(f"  Importance: {info['importance']}/10")
        print(f"  Implementation: {info['implementation']}")
    
    # Risk Matrix
    print("\n" + "="*80)
    print("3. Security Risk Matrix:")
    print("="*80)
    risk_matrix = create_risk_matrix(vulnerabilities)
    for risk in sorted(risk_matrix, key=lambda x: x['risk_score'], reverse=True):
        print(f"\n{risk['vulnerability']}:")
        print(f"  Risk Score: {risk['risk_score']}/100")
        print(f"  Impact: {risk['impact']}, Likelihood: {risk['likelihood']}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_security_vulnerabilities(vulnerabilities)
    plot_secure_practices(practices)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. AI systems face unique security vulnerabilities")
    print("2. Secure development practices should be applied throughout the lifecycle")
    print("3. Risk assessment helps prioritize security measures")
    print("4. Security testing and monitoring are essential")
    print("5. Incident response plans should be prepared in advance")
    print("="*80 + "\n")

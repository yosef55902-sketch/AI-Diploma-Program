"""
Unit 1: Foundations of AI Ethics
Example 3: Case Study Analysis - COMPAS Recidivism Algorithm
أسس أخلاقيات الذكاء الاصطناعي - مثال 3: تحليل دراسة حالة - خوارزمية COMPAS

This example analyzes the COMPAS case study using ethical frameworks.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)

# ============================================================================
# COMPAS CASE STUDY DATA
# بيانات دراسة حالة COMPAS
# ============================================================================

def analyze_compas_case():
    """
    Analyze the COMPAS (Correctional Offender Management Profiling for 
    Alternative Sanctions) case study
    تحليل دراسة حالة COMPAS
    """
    
    print("="*80)
    print("CASE STUDY: COMPAS Recidivism Algorithm")
    print("دراسة الحالة: خوارزمية COMPAS للعودة للإجرام")
    print("="*80)
    
    # Background
    print("\n📋 BACKGROUND / الخلفية:")
    print("-" * 60)
    print("COMPAS is an algorithm used by US courts to assess the likelihood")
    print("that a defendant will reoffend (recidivate).")
    print("\nCOMPAS هي خوارزمية تستخدمها المحاكم الأمريكية لتقييم احتمالية")
    print("عودة المتهم للإجرام (العودة للإجرام).")
    
    # The Problem
    print("\n\n⚠️ THE PROBLEM / المشكلة:")
    print("-" * 60)
    print("ProPublica investigation (2016) found that COMPAS showed:")
    print("1. Higher false positive rates for Black defendants")
    print("   (معدلات إيجابية خاطئة أعلى للمتهمين السود)")
    print("2. Higher false negative rates for White defendants")
    print("   (معدلات سلبية خاطئة أعلى للمتهمين البيض)")
    print("3. Racial bias in risk predictions")
    print("   (تحيز عرقي في توقعات المخاطر)")
    
    # Ethical Analysis
    print("\n\n🔍 ETHICAL ANALYSIS / التحليل الأخلاقي:")
    print("="*80)
    
    ethical_issues = {
        'Justice and Fairness': {
            'issue': 'Unequal treatment based on race',
            'issue_ar': 'معاملة غير متساوية على أساس العرق',
            'severity': 9,
            'framework': 'Rights-Based, Deontology'
        },
        'Transparency': {
            'issue': 'Proprietary algorithm, unclear how it works',
            'issue_ar': 'خوارزمية احتكارية، غير واضح كيف تعمل',
            'severity': 8,
            'framework': 'Rights-Based'
        },
        'Accountability': {
            'issue': 'Who is responsible for biased outcomes?',
            'issue_ar': 'من المسؤول عن النتائج المتحيزة؟',
            'severity': 7,
            'framework': 'Virtue Ethics, Deontology'
        },
        'Harm': {
            'issue': 'People may receive harsher sentences due to bias',
            'issue_ar': 'قد يتلقى الناس أحكاماً أقسى بسبب التحيز',
            'severity': 10,
            'framework': 'Utilitarianism, Care Ethics'
        }
    }
    
    for issue_name, details in ethical_issues.items():
        print(f"\n{issue_name} / {details['issue_ar']}")
        print("-" * 60)
        print(f"Issue: {details['issue']} / {details['issue_ar']}")
        print(f"Severity (1-10): {details['severity']}/10")
        print(f"Relevant Framework: {details['framework']}")
    
    return ethical_issues

# ============================================================================
# VISUALIZATION: Ethical Issues Severity
# التصور: شدة القضايا الأخلاقية
# ============================================================================

def create_ethical_issues_chart(ethical_issues):
    """Create a chart showing severity of ethical issues"""
    # إنشاء مخطط يوضح شدة القضايا الأخلاقية
    
    issues = list(ethical_issues.keys())
    severities = [details['severity'] for details in ethical_issues.values()]
    colors = ['#e74c3c' if s >= 9 else '#f39c12' if s >= 7 else '#3498db' 
              for s in severities]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    bars = ax.barh(issues, severities, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Severity Score (1-10) / درجة الشدة (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('COMPAS Case Study: Ethical Issues Severity\n'
                'دراسة حالة COMPAS: شدة القضايا الأخلاقية',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels
    for i, (bar, severity) in enumerate(zip(bars, severities)):
        ax.text(severity + 0.2, i, f'{severity}/10', 
               va='center', fontweight='bold', fontsize=11)
    
    # Add legend
    high_severity = mpatches.Patch(color='#e74c3c', label='High Severity (9-10) / شدة عالية')
    medium_severity = mpatches.Patch(color='#f39c12', label='Medium Severity (7-8) / شدة متوسطة')
    low_severity = mpatches.Patch(color='#3498db', label='Low Severity (<7) / شدة منخفضة')
    ax.legend(handles=[high_severity, medium_severity, low_severity], 
             loc='lower right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('unit1-ethics-foundations/examples/compas_ethical_issues.png',
                dpi=300, bbox_inches='tight')
    print("\n✅ Saved: compas_ethical_issues.png")
    plt.close()

# ============================================================================
# FRAMEWORK APPLICATION
# تطبيق الأطر
# ============================================================================

def apply_frameworks_to_compas():
    """Apply different ethical frameworks to COMPAS case"""
    # تطبيق أطر أخلاقية مختلفة على حالة COMPAS
    
    print("\n" + "="*80)
    print("APPLYING ETHICAL FRAMEWORKS / تطبيق الأطر الأخلاقية")
    print("="*80)
    
    framework_analysis = {
        'Utilitarianism': {
            'analysis': 'COMPAS may maximize efficiency but causes harm to minority groups',
            'analysis_ar': 'قد تعظم COMPAS الكفاءة لكنها تسبب ضرراً للمجموعات الأقلية',
            'verdict': 'Unethical - harms outweigh benefits',
            'verdict_ar': 'غير أخلاقي - الأضرار تفوق الفوائد'
        },
        'Deontology': {
            'analysis': 'Violates principle of equal treatment regardless of race',
            'analysis_ar': 'ينتهك مبدأ المعاملة المتساوية بغض النظر عن العرق',
            'verdict': 'Unethical - violates moral duty',
            'verdict_ar': 'غير أخلاقي - ينتهك الواجب الأخلاقي'
        },
        'Rights-Based': {
            'analysis': 'Violates right to fair treatment and equal protection',
            'analysis_ar': 'ينتهك الحق في المعاملة العادلة والحماية المتساوية',
            'verdict': 'Unethical - violates fundamental rights',
            'verdict_ar': 'غير أخلاقي - ينتهك الحقوق الأساسية'
        },
        'Virtue Ethics': {
            'analysis': 'Lacks fairness, justice, and respect for human dignity',
            'analysis_ar': 'يفتقر إلى العدالة والإنصاف واحترام الكرامة الإنسانية',
            'verdict': 'Unethical - lacks virtuous character',
            'verdict_ar': 'غير أخلاقي - يفتقر إلى الشخصية الفاضلة'
        }
    }
    
    for framework, details in framework_analysis.items():
        print(f"\n{framework}:")
        print("-" * 60)
        print(f"Analysis: {details['analysis']}")
        print(f"التحليل: {details['analysis_ar']}")
        print(f"Verdict: {details['verdict']}")
        print(f"الحكم: {details['verdict_ar']}")

# ============================================================================
# LESSONS LEARNED
# الدروس المستفادة
# ============================================================================

def print_lessons_learned():
    """Print key lessons from COMPAS case"""
    # طباعة الدروس الرئيسية من حالة COMPAS
    
    print("\n" + "="*80)
    print("LESSONS LEARNED / الدروس المستفادة")
    print("="*80)
    
    lessons = [
        {
            'lesson': 'Test for bias before deployment',
            'lesson_ar': 'اختبار التحيز قبل النشر',
            'description': 'Comprehensive bias testing is essential'
        },
        {
            'lesson': 'Transparency is crucial',
            'lesson_ar': 'الشفافية حاسمة',
            'description': 'Proprietary algorithms need transparency'
        },
        {
            'lesson': 'Multiple perspectives matter',
            'lesson_ar': 'وجهات النظر المتعددة مهمة',
            'description': 'Diverse teams can identify issues earlier'
        },
        {
            'lesson': 'Continuous monitoring required',
            'lesson_ar': 'المراقبة المستمرة مطلوبة',
            'description': 'Monitor for bias even after deployment'
        },
        {
            'lesson': 'Accountability is essential',
            'lesson_ar': 'المساءلة ضرورية',
            'description': 'Clear responsibility for AI decisions'
        }
    ]
    
    for i, lesson in enumerate(lessons, 1):
        print(f"\n{i}. {lesson['lesson']} / {lesson['lesson_ar']}")
        print(f"   {lesson['description']}")

# ============================================================================
# MAIN EXECUTION
# التنفيذ الرئيسي
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 1 - Example 3: Case Study Analysis - COMPAS")
    print("الوحدة 1 - مثال 3: تحليل دراسة حالة - COMPAS")
    print("="*80)
    
    # Analyze case
    ethical_issues = analyze_compas_case()
    
    # Apply frameworks
    apply_frameworks_to_compas()
    
    # Lessons learned
    print_lessons_learned()
    
    # Create visualization
    print("\n" + "="*80)
    print("Creating Visualization / إنشاء التصور...")
    print("="*80)
    create_ethical_issues_chart(ethical_issues)
    
    print("\n" + "="*80)
    print("✅ Example completed successfully!")
    print("✅ اكتمل المثال بنجاح!")
    print("="*80)
    print("\nKey Takeaways / النقاط الرئيسية:")
    print("1. Real-world AI systems can have serious ethical issues")
    print("   (أنظمة الذكاء الاصطناعي في العالم الحقيقي يمكن أن يكون لها قضايا أخلاقية خطيرة)")
    print("2. Multiple ethical frameworks help identify different types of problems")
    print("   (الأطر الأخلاقية المتعددة تساعد في تحديد أنواع مختلفة من المشاكل)")
    print("3. Case studies provide valuable lessons for future development")
    print("   (دراسات الحالة توفر دروساً قيمة للتطوير المستقبلي)")
    print("="*80 + "\n")


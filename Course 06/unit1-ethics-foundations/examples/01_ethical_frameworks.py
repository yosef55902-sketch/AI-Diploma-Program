"""
Unit 1: Foundations of AI Ethics
Example 1: Ethical Frameworks Comparison
أسس أخلاقيات الذكاء الاصطناعي - مثال 1: مقارنة الأطر الأخلاقية

This example demonstrates different ethical frameworks and how they apply to AI development.
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams

# Set up bilingual support for plots
# إعداد الدعم ثنائي اللغة للرسوم البيانية
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (12, 8)

# ============================================================================
# ETHICAL FRAMEWORKS DATA
# بيانات الأطر الأخلاقية
# ============================================================================

frameworks = {
    'Utilitarianism': {
        'name_en': 'Utilitarianism',
        'name_ar': 'النفعية',
        'focus': 'Maximize overall happiness/utility',
        'focus_ar': 'تعظيم السعادة/المنفعة الإجمالية',
        'ai_application': 'AI that benefits the greatest number of people',
        'ai_application_ar': 'الذكاء الاصطناعي الذي يفيد أكبر عدد من الناس',
        'strength': 8,
        'weakness': 6,
        'practicality': 7
    },
    'Deontology': {
        'name_en': 'Deontology',
        'name_ar': 'الواجباتية',
        'focus': 'Follow moral rules and duties',
        'focus_ar': 'اتباع القواعد والواجبات الأخلاقية',
        'ai_application': 'AI that follows ethical principles regardless of outcomes',
        'ai_application_ar': 'الذكاء الاصطناعي الذي يتبع المبادئ الأخلاقية بغض النظر عن النتائج',
        'strength': 7,
        'weakness': 5,
        'practicality': 6
    },
    'Virtue Ethics': {
        'name_en': 'Virtue Ethics',
        'name_ar': 'أخلاق الفضيلة',
        'focus': 'Develop good character and virtues',
        'focus_ar': 'تطوير الشخصية الجيدة والفضائل',
        'ai_application': 'AI that reflects good character traits (honesty, fairness)',
        'ai_application_ar': 'الذكاء الاصطناعي الذي يعكس صفات شخصية جيدة (الصدق، العدالة)',
        'strength': 6,
        'weakness': 7,
        'practicality': 5
    },
    'Rights-Based': {
        'name_en': 'Rights-Based Ethics',
        'name_ar': 'أخلاقيات الحقوق',
        'focus': 'Protect individual rights',
        'focus_ar': 'حماية الحقوق الفردية',
        'ai_application': 'AI that respects human rights (privacy, autonomy)',
        'ai_application_ar': 'الذكاء الاصطناعي الذي يحترم حقوق الإنسان (الخصوصية، الاستقلالية)',
        'strength': 9,
        'weakness': 4,
        'practicality': 8
    },
    'Care Ethics': {
        'name_en': 'Care Ethics',
        'name_ar': 'أخلاقيات الرعاية',
        'focus': 'Emphasize relationships and care',
        'focus_ar': 'التركيز على العلاقات والرعاية',
        'ai_application': 'AI that considers relationships and emotional well-being',
        'ai_application_ar': 'الذكاء الاصطناعي الذي يأخذ في الاعتبار العلاقات والرفاهية العاطفية',
        'strength': 7,
        'weakness': 6,
        'practicality': 6
    }
}

# ============================================================================
# VISUALIZATION 1: Framework Comparison Bar Chart
# الرسم البياني 1: مقارنة الأطر
# ============================================================================

def create_framework_comparison():
    """Create a bar chart comparing ethical frameworks"""
    # إنشاء مخطط شريطي لمقارنة الأطر الأخلاقية
    
    framework_names = [f['name_en'] for f in frameworks.values()]
    strengths = [f['strength'] for f in frameworks.values()]
    weaknesses = [f['weakness'] for f in frameworks.values()]
    practicality = [f['practicality'] for f in frameworks.values()]
    
    x = np.arange(len(framework_names))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    bars1 = ax.bar(x - width, strengths, width, label='Strengths / نقاط القوة', 
                   color='#2ecc71', alpha=0.8)
    bars2 = ax.bar(x, weaknesses, width, label='Weaknesses / نقاط الضعف', 
                   color='#e74c3c', alpha=0.8)
    bars3 = ax.bar(x + width, practicality, width, label='Practicality / العملية', 
                   color='#3498db', alpha=0.8)
    
    ax.set_xlabel('Ethical Framework / الإطار الأخلاقي', fontsize=12, fontweight='bold')
    ax.set_ylabel('Score (1-10) / النقاط (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Ethical Frameworks Comparison / مقارنة الأطر الأخلاقية', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(framework_names, rotation=15, ha='right')
    ax.legend(fontsize=10)
    ax.set_ylim(0, 10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    # إضافة تسميات القيم على الأشرطة
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), 'ethical_frameworks_comparison.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: ethical_frameworks_comparison.png")
    plt.close()

# ============================================================================
# VISUALIZATION 2: Framework Application to AI Scenarios
# الرسم البياني 2: تطبيق الأطر على سيناريوهات الذكاء الاصطناعي
# ============================================================================

def create_ai_scenario_analysis():
    """Analyze how different frameworks apply to AI scenarios"""
    # تحليل كيفية تطبيق الأطر المختلفة على سيناريوهات الذكاء الاصطناعي
    
    scenarios = {
        'Autonomous Vehicles': {
            'Utilitarianism': 9,
            'Deontology': 7,
            'Virtue Ethics': 6,
            'Rights-Based': 8,
            'Care Ethics': 7
        },
        'Healthcare AI': {
            'Utilitarianism': 8,
            'Deontology': 9,
            'Virtue Ethics': 8,
            'Rights-Based': 9,
            'Care Ethics': 9
        },
        'Facial Recognition': {
            'Utilitarianism': 5,
            'Deontology': 6,
            'Virtue Ethics': 4,
            'Rights-Based': 3,
            'Care Ethics': 5
        },
        'Hiring Algorithms': {
            'Utilitarianism': 6,
            'Deontology': 7,
            'Virtue Ethics': 7,
            'Rights-Based': 8,
            'Care Ethics': 6
        }
    }
    
    # Create heatmap
    # إنشاء خريطة حرارية
    scenario_names = list(scenarios.keys())
    framework_names = list(frameworks.keys())
    
    data_matrix = np.array([[scenarios[s][f] for f in framework_names] 
                           for s in scenario_names])
    
    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(data_matrix, cmap='RdYlGn', aspect='auto', vmin=0, vmax=10)
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(framework_names)))
    ax.set_yticks(np.arange(len(scenario_names)))
    ax.set_xticklabels(framework_names, rotation=15, ha='right')
    ax.set_yticklabels(scenario_names)
    
    # Add text annotations
    # إضافة تعليقات نصية
    for i in range(len(scenario_names)):
        for j in range(len(framework_names)):
            text = ax.text(j, i, data_matrix[i, j],
                          ha="center", va="center", color="black", fontweight='bold')
    
    ax.set_title('Ethical Framework Applicability to AI Scenarios\n'
                 'قابلية تطبيق الأطر الأخلاقية على سيناريوهات الذكاء الاصطناعي',
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Applicability Score (1-10) / درجة القابلية للتطبيق (1-10)', 
                   fontsize=10)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), 'ai_scenario_framework_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: ai_scenario_framework_analysis.png")
    plt.close()

# ============================================================================
# FRAMEWORK DESCRIPTION TABLE
# جدول وصف الأطر
# ============================================================================

def print_framework_descriptions():
    """Print detailed framework descriptions"""
    # طباعة أوصاف مفصلة للأطر
    
    print("\n" + "="*80)
    print("ETHICAL FRAMEWORKS FOR AI / الأطر الأخلاقية للذكاء الاصطناعي")
    print("="*80 + "\n")
    
    for key, framework in frameworks.items():
        print(f"\n{framework['name_en']} / {framework['name_ar']}")
        print("-" * 60)
        print(f"Focus / التركيز: {framework['focus']} / {framework['focus_ar']}")
        print(f"AI Application / تطبيق الذكاء الاصطناعي:")
        print(f"  {framework['ai_application']}")
        print(f"  {framework['ai_application_ar']}")
        print(f"Strengths Score / نقاط القوة: {framework['strength']}/10")
        print(f"Weaknesses Score / نقاط الضعف: {framework['weakness']}/10")
        print(f"Practicality Score / العملية: {framework['practicality']}/10")

# ============================================================================
# MAIN EXECUTION
# التنفيذ الرئيسي
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 1 - Example 1: Ethical Frameworks Comparison")
    print("الوحدة 1 - مثال 1: مقارنة الأطر الأخلاقية")
    print("="*80)
    
    # Print framework descriptions
    # طباعة أوصاف الأطر
    print_framework_descriptions()
    
    # Create visualizations
    # إنشاء الرسوم البيانية
    print("\n" + "="*80)
    print("Creating Visualizations / إنشاء الرسوم البيانية...")
    print("="*80)
    
    create_framework_comparison()
    create_ai_scenario_analysis()
    
    print("\n" + "="*80)
    print("✅ Example completed successfully!")
    print("✅ اكتمل المثال بنجاح!")
    print("="*80)
    print("\nKey Takeaways / النقاط الرئيسية:")
    print("1. Different ethical frameworks offer different perspectives")
    print("   (الأطر الأخلاقية المختلفة تقدم وجهات نظر مختلفة)")
    print("2. No single framework is perfect for all AI scenarios")
    print("   (لا يوجد إطار واحد مثالي لجميع سيناريوهات الذكاء الاصطناعي)")
    print("3. Combining frameworks provides more comprehensive ethical analysis")
    print("   (دمج الأطر يوفر تحليلاً أخلاقياً أكثر شمولية)")
    print("="*80 + "\n")


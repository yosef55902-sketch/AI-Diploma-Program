"""
Unit 1: Foundations of AI Ethics
Example 2: Ethical Decision-Making Framework
أسس أخلاقيات الذكاء الاصطناعي - مثال 2: إطار اتخاذ القرارات الأخلاقية

This example demonstrates a structured approach to ethical decision-making in AI development.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Set up plotting
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 10)

# ============================================================================
# ETHICAL DECISION-MAKING FRAMEWORK
# إطار اتخاذ القرارات الأخلاقية
# ============================================================================

class EthicalDecisionFramework:
    """
    A framework for making ethical decisions in AI development
    إطار لاتخاذ قرارات أخلاقية في تطوير الذكاء الاصطناعي
    """
    
    def __init__(self):
        self.steps = [
            {
                'step': 1,
                'name_en': 'Identify the Problem',
                'name_ar': 'تحديد المشكلة',
                'description_en': 'Clearly define the ethical issue or dilemma',
                'description_ar': 'تحديد المشكلة الأخلاقية أو المعضلة بوضوح',
                'questions': [
                    'What is the AI system supposed to do?',
                    'What ethical concerns might arise?',
                    'Who are the stakeholders?'
                ]
            },
            {
                'step': 2,
                'name_en': 'Gather Information',
                'name_ar': 'جمع المعلومات',
                'description_en': 'Collect relevant facts and context',
                'description_ar': 'جمع الحقائق والسياق ذات الصلة',
                'questions': [
                    'What data will be used?',
                    'How will the system be deployed?',
                    'What are the potential impacts?'
                ]
            },
            {
                'step': 3,
                'name_en': 'Identify Stakeholders',
                'name_ar': 'تحديد أصحاب المصلحة',
                'description_en': 'List all affected parties',
                'description_ar': 'سرد جميع الأطراف المتأثرة',
                'questions': [
                    'Who will use the system?',
                    'Who might be affected?',
                    'Who has decision-making power?'
                ]
            },
            {
                'step': 4,
                'name_en': 'Apply Ethical Frameworks',
                'name_ar': 'تطبيق الأطر الأخلاقية',
                'description_en': 'Analyze using multiple ethical perspectives',
                'description_ar': 'التحليل باستخدام وجهات نظر أخلاقية متعددة',
                'questions': [
                    'What would utilitarianism suggest?',
                    'What would deontology require?',
                    'What rights are at stake?'
                ]
            },
            {
                'step': 5,
                'name_en': 'Evaluate Options',
                'name_ar': 'تقييم الخيارات',
                'description_en': 'Consider different approaches and their consequences',
                'description_ar': 'النظر في أساليب مختلفة وعواقبها',
                'questions': [
                    'What are the alternative approaches?',
                    'What are the trade-offs?',
                    'What are the risks and benefits?'
                ]
            },
            {
                'step': 6,
                'name_en': 'Make Decision',
                'name_ar': 'اتخاذ القرار',
                'description_en': 'Choose the most ethical course of action',
                'description_ar': 'اختيار المسار الأكثر أخلاقية',
                'questions': [
                    'Which option best balances ethical considerations?',
                    'Can the decision be justified?',
                    'Is it transparent and accountable?'
                ]
            },
            {
                'step': 7,
                'name_en': 'Monitor and Review',
                'name_ar': 'المراقبة والمراجعة',
                'description_en': 'Continuously assess and improve',
                'description_ar': 'التقييم والتحسين المستمر',
                'questions': [
                    'Is the system working as intended?',
                    'Are there unintended consequences?',
                    'How can we improve?'
                ]
            }
        ]
    
    def analyze_scenario(self, scenario_name, scenario_data):
        """Analyze an AI scenario using the framework"""
        # تحليل سيناريو ذكاء اصطناعي باستخدام الإطار
        
        print(f"\n{'='*80}")
        print(f"ETHICAL ANALYSIS: {scenario_name}")
        print(f"التحليل الأخلاقي: {scenario_name}")
        print(f"{'='*80}\n")
        
        for step in self.steps:
            print(f"\nStep {step['step']}: {step['name_en']} / {step['name_ar']}")
            print("-" * 60)
            print(f"Description: {step['description_en']} / {step['description_ar']}")
            print(f"\nKey Questions / الأسئلة الرئيسية:")
            for i, question in enumerate(step['questions'], 1):
                print(f"  {i}. {question}")
            
            # Apply to scenario if data provided
            # تطبيق على السيناريو إذا كانت البيانات متوفرة
            if scenario_data and step['step'] in scenario_data:
                print(f"\nAnalysis / التحليل:")
                print(f"  {scenario_data[step['step']]}")

# ============================================================================
# VISUALIZATION: Decision-Making Flowchart
# الرسم البياني: مخطط انسيابي لاتخاذ القرار
# ============================================================================

def create_decision_flowchart():
    """Create a flowchart of the ethical decision-making process"""
    # إنشاء مخطط انسيابي لعملية اتخاذ القرار الأخلاقي
    
    fig, ax = plt.subplots(figsize=(14, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Define colors for different step types
    # تحديد الألوان لأنواع الخطوات المختلفة
    start_color = '#2ecc71'  # Green
    process_color = '#3498db'  # Blue
    decision_color = '#f39c12'  # Orange
    end_color = '#9b59b6'  # Purple
    
    # Step positions and sizes
    # مواضع وأحجام الخطوات
    steps = [
        {'step': 0, 'name': 'Start', 'x': 5, 'y': 13, 'width': 2, 'height': 0.6, 
         'color': start_color, 'text': 'Start\nبدء'},
        {'step': 1, 'name': 'Identify Problem', 'x': 5, 'y': 11.5, 'width': 2.5, 
         'height': 0.6, 'color': process_color, 'text': '1. Identify\nProblem'},
        {'step': 2, 'name': 'Gather Info', 'x': 5, 'y': 10, 'width': 2.5, 
         'height': 0.6, 'color': process_color, 'text': '2. Gather\nInformation'},
        {'step': 3, 'name': 'Stakeholders', 'x': 5, 'y': 8.5, 'width': 2.5, 
         'height': 0.6, 'color': process_color, 'text': '3. Identify\nStakeholders'},
        {'step': 4, 'name': 'Apply Frameworks', 'x': 5, 'y': 7, 'width': 2.5, 
         'height': 0.6, 'color': decision_color, 'text': '4. Apply Ethical\nFrameworks'},
        {'step': 5, 'name': 'Evaluate', 'x': 5, 'y': 5.5, 'width': 2.5, 
         'height': 0.6, 'color': decision_color, 'text': '5. Evaluate\nOptions'},
        {'step': 6, 'name': 'Make Decision', 'x': 5, 'y': 4, 'width': 2.5, 
         'height': 0.6, 'color': process_color, 'text': '6. Make\nDecision'},
        {'step': 7, 'name': 'Monitor', 'x': 5, 'y': 2.5, 'width': 2.5, 
         'height': 0.6, 'color': process_color, 'text': '7. Monitor &\nReview'},
        {'step': 8, 'name': 'End', 'x': 5, 'y': 1, 'width': 2, 'height': 0.6, 
         'color': end_color, 'text': 'End\nنهاية'},
    ]
    
    # Draw boxes
    # رسم الصناديق
    for step in steps:
        box = FancyBboxPatch(
            (step['x'] - step['width']/2, step['y'] - step['height']/2),
            step['width'], step['height'],
            boxstyle="round,pad=0.1",
            edgecolor='black',
            facecolor=step['color'],
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(box)
        
        # Add text
        ax.text(step['x'], step['y'], step['text'],
               ha='center', va='center', fontsize=9, fontweight='bold',
               color='white' if step['color'] != '#f39c12' else 'black')
    
    # Draw arrows
    # رسم الأسهم
    for i in range(len(steps) - 1):
        arrow = FancyArrowPatch(
            (steps[i]['x'], steps[i]['y'] - steps[i]['height']/2),
            (steps[i+1]['x'], steps[i+1]['y'] + steps[i+1]['height']/2),
            arrowstyle='->', mutation_scale=20, linewidth=2, color='black'
        )
        ax.add_patch(arrow)
    
    # Add feedback loop from step 7 to step 4
    # إضافة حلقة تغذية راجعة من الخطوة 7 إلى الخطوة 4
    feedback_arrow = FancyArrowPatch(
        (steps[6]['x'] - steps[6]['width']/2 - 0.3, steps[6]['y']),
        (steps[3]['x'] - steps[3]['width']/2 - 0.3, steps[3]['y']),
        arrowstyle='->', mutation_scale=20, linewidth=2, 
        color='red', linestyle='--', alpha=0.7
    )
    ax.add_patch(feedback_arrow)
    
    # Add label for feedback loop
    ax.text(2, 5.5, 'Feedback Loop\nحلقة التغذية الراجعة',
           ha='center', va='center', fontsize=8, 
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    ax.set_title('Ethical Decision-Making Framework for AI\n'
                'إطار اتخاذ القرارات الأخلاقية للذكاء الاصطناعي',
                fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'ethical_decision_flowchart.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: ethical_decision_flowchart.png")
    plt.close()

# ============================================================================
# EXAMPLE SCENARIO ANALYSIS
# مثال تحليل السيناريو
# ============================================================================

def example_scenario_analysis():
    """Example: Analyzing an AI hiring system"""
    # مثال: تحليل نظام توظيف بالذكاء الاصطناعي
    
    scenario_data = {
        1: "AI system to screen job applicants based on resumes and interviews",
        2: "Uses historical hiring data, may contain biases, deployed in HR department",
        3: "Applicants, HR staff, company management, society at large",
        4: "Utilitarianism: Maximize hiring efficiency vs. Deontology: Fair treatment regardless of outcome",
        5: "Option A: Use as-is (fast but potentially biased), Option B: Add fairness constraints (slower but fairer)",
        6: "Choose Option B with fairness monitoring and transparency measures",
        7: "Regular audits, track hiring demographics, adjust as needed"
    }
    
    framework = EthicalDecisionFramework()
    framework.analyze_scenario("AI Hiring System", scenario_data)

# ============================================================================
# STAKEHOLDER ANALYSIS VISUALIZATION
# تصور تحليل أصحاب المصلحة
# ============================================================================

def create_stakeholder_analysis():
    """Create a stakeholder impact matrix"""
    # إنشاء مصفوفة تأثير أصحاب المصلحة
    
    stakeholders = ['Users', 'Developers', 'Company', 'Society', 'Regulators']
    impact_levels = [9, 7, 8, 6, 7]  # High impact scores
    influence_levels = [5, 8, 9, 4, 9]  # Influence scores
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Impact chart
    colors = plt.cm.viridis(np.linspace(0, 1, len(stakeholders)))
    bars1 = ax1.barh(stakeholders, impact_levels, color=colors, alpha=0.8)
    ax1.set_xlabel('Impact Level (1-10) / مستوى التأثير (1-10)', fontsize=11)
    ax1.set_title('Stakeholder Impact / تأثير أصحاب المصلحة', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 10)
    ax1.grid(axis='x', alpha=0.3)
    
    for i, (bar, value) in enumerate(zip(bars1, impact_levels)):
        ax1.text(value + 0.2, i, f'{value}', va='center', fontweight='bold')
    
    # Influence chart
    bars2 = ax2.barh(stakeholders, influence_levels, color=colors, alpha=0.8)
    ax2.set_xlabel('Influence Level (1-10) / مستوى التأثير (1-10)', fontsize=11)
    ax2.set_title('Stakeholder Influence / تأثير أصحاب المصلحة', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 10)
    ax2.grid(axis='x', alpha=0.3)
    
    for i, (bar, value) in enumerate(zip(bars2, influence_levels)):
        ax2.text(value + 0.2, i, f'{value}', va='center', fontweight='bold')
    
    plt.tight_layout()
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'stakeholder_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("✅ Saved: stakeholder_analysis.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# التنفيذ الرئيسي
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 1 - Example 2: Ethical Decision-Making Framework")
    print("الوحدة 1 - مثال 2: إطار اتخاذ القرارات الأخلاقية")
    print("="*80)
    
    # Create framework
    framework = EthicalDecisionFramework()
    
    # Print framework steps
    print("\nETHICAL DECISION-MAKING FRAMEWORK")
    print("إطار اتخاذ القرارات الأخلاقية")
    print("="*80)
    for step in framework.steps:
        print(f"\nStep {step['step']}: {step['name_en']} / {step['name_ar']}")
        print(f"  {step['description_en']} / {step['description_ar']}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations / إنشاء الرسوم البيانية...")
    print("="*80)
    
    create_decision_flowchart()
    create_stakeholder_analysis()
    
    # Example scenario
    print("\n" + "="*80)
    print("Example Scenario Analysis / مثال تحليل السيناريو")
    print("="*80)
    example_scenario_analysis()
    
    print("\n" + "="*80)
    print("✅ Example completed successfully!")
    print("✅ اكتمل المثال بنجاح!")
    print("="*80)
    print("\nKey Takeaways / النقاط الرئيسية:")
    print("1. Structured frameworks help ensure comprehensive ethical analysis")
    print("   (الأطر المنظمة تساعد في ضمان تحليل أخلاقي شامل)")
    print("2. Multiple perspectives lead to better decisions")
    print("   (وجهات النظر المتعددة تؤدي إلى قرارات أفضل)")
    print("3. Continuous monitoring is essential for ethical AI")
    print("   (المراقبة المستمرة ضرورية للذكاء الاصطناعي الأخلاقي)")
    print("="*80 + "\n")


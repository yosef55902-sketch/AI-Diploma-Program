# Beginner's Guide: Knowledge-Based System
## دليل المبتدئين: نظام قائم على المعرفة

---

## 🎯 Real-World Application | التطبيق في الحياة الواقعية

### Example: Medical Diagnosis Assistant
**Imagine you're building a simple medical diagnosis system like WebMD or symptom checker apps.**

**Problem:** A patient has symptoms and you need to determine possible conditions and recommend actions.

**Solution:** Your knowledge-based system uses rules to:
- Match symptoms to conditions
- Recommend tests or treatments
- Explain the reasoning

**Real-World Impact:**
- ✅ Helps doctors make faster diagnoses
- ✅ Educates patients about their symptoms
- ✅ Reduces medical errors
- ✅ Available 24/7 for basic consultations

**Example Rules:**
```
IF patient has fever AND cough THEN possible_condition = flu
IF patient has chest_pain AND shortness_of_breath THEN possible_condition = heart_issue
IF patient has fever AND rash THEN possible_condition = infection
```

---

## 📚 Step-by-Step Guide for Beginners | دليل خطوة بخطوة للمبتدئين

### Step 1: Understand Knowledge-Based Systems (Day 1)

**What is a Knowledge-Based System?**
A system that:
- Stores facts (information)
- Has rules (IF-THEN statements)
- Can reason (make conclusions)
- Explains its decisions

**Example:**
```
Facts:
- John has fever
- John has cough
- John is 25 years old

Rules:
- IF has_fever AND has_cough THEN might_have_flu
- IF has_fever AND age < 12 THEN see_pediatrician

Conclusion:
- John might have flu
- John should see a general doctor (not pediatrician)
```

---

### Step 2: Set Up Your Project (Day 1)

**Create these files:**

1. **`knowledge_base.py`** - Stores facts and rules
2. **`inference_engine.py`** - Makes conclusions
3. **`main.py`** - Runs the system
4. **`README.md`** - Documentation

---

### Step 3: Create Knowledge Base (Day 2)

**File: `knowledge_base.py`**

```python
class KnowledgeBase:
    """Stores facts and rules"""
    
    def __init__(self):
        self.facts = []  # List of facts
        self.rules = []  # List of rules
    
    def add_fact(self, fact):
        """Add a fact to the knowledge base"""
        if fact not in self.facts:
            self.facts.append(fact)
            print(f"Added fact: {fact}")
    
    def add_rule(self, condition, conclusion):
        """
        Add a rule: IF condition THEN conclusion
        condition: List of facts that must be true
        conclusion: Fact that becomes true
        """
        rule = {
            'if': condition,
            'then': conclusion
        }
        self.rules.append(rule)
        print(f"Added rule: IF {condition} THEN {conclusion}")
    
    def get_facts(self):
        """Get all facts"""
        return self.facts
    
    def get_rules(self):
        """Get all rules"""
        return self.rules
```

**Example Usage:**
```python
kb = KnowledgeBase()

# Add facts
kb.add_fact("patient_has_fever")
kb.add_fact("patient_has_cough")
kb.add_fact("patient_age_25")

# Add rules
kb.add_rule(
    condition=["patient_has_fever", "patient_has_cough"],
    conclusion="possible_flu"
)
```

---

### Step 4: Implement Forward Chaining (Day 3)

**File: `inference_engine.py`**

```python
class InferenceEngine:
    """Makes conclusions from facts and rules"""
    
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.working_memory = []  # Facts we know
    
    def forward_chaining(self):
        """
        Forward Chaining: Start with facts, apply rules
        Keep applying rules until no new facts can be derived
        """
        # Start with known facts
        self.working_memory = self.kb.get_facts().copy()
        changed = True
        
        while changed:
            changed = False
            
            # Check each rule
            for rule in self.kb.get_rules():
                conditions = rule['if']
                conclusion = rule['then']
                
                # Check if all conditions are met
                if all(cond in self.working_memory for cond in conditions):
                    # If conclusion not already known
                    if conclusion not in self.working_memory:
                        self.working_memory.append(conclusion)
                        print(f"New conclusion: {conclusion}")
                        changed = True
        
        return self.working_memory
```

**How It Works:**
1. Start with known facts
2. Check each rule
3. If rule conditions are met, add conclusion
4. Repeat until no new facts

---

### Step 5: Implement Backward Chaining (Day 4)

```python
def backward_chaining(self, goal):
    """
    Backward Chaining: Start with goal, find what's needed
    Returns True if goal can be proven, False otherwise
    """
    # If goal is already a fact, we're done
    if goal in self.working_memory:
        return True
    
    # Find rules that can prove this goal
    for rule in self.kb.get_rules():
        if rule['then'] == goal:
            # Check if all conditions can be proven
            conditions = rule['if']
            if all(self.backward_chaining(cond) for cond in conditions):
                self.working_memory.append(goal)
                return True
    
    return False
```

**Forward vs Backward:**
- **Forward:** Start with facts → find conclusions
- **Backward:** Start with goal → find needed facts

---

### Step 6: Add Explanation (Day 5)

```python
def explain(self, conclusion):
    """Explain how a conclusion was reached"""
    explanation = []
    
    # Find rule that led to this conclusion
    for rule in self.kb.get_rules():
        if rule['then'] == conclusion:
            explanation.append(f"Rule: IF {rule['if']} THEN {conclusion}")
            explanation.append(f"Conditions met: {rule['if']}")
            break
    
    return "\n".join(explanation)
```

---

### Step 7: Create Medical Diagnosis System (Day 6)

**File: `medical_system.py`**

```python
from knowledge_base import KnowledgeBase
from inference_engine import InferenceEngine

class MedicalDiagnosisSystem:
    """Medical diagnosis knowledge-based system"""
    
    def __init__(self):
        self.kb = KnowledgeBase()
        self.setup_rules()
        self.engine = InferenceEngine(self.kb)
    
    def setup_rules(self):
        """Set up medical diagnosis rules"""
        # Rule 1: Flu diagnosis
        self.kb.add_rule(
            condition=["has_fever", "has_cough", "has_headache"],
            conclusion="possible_flu"
        )
        
        # Rule 2: Cold diagnosis
        self.kb.add_rule(
            condition=["has_cough", "has_runny_nose"],
            conclusion="possible_cold"
        )
        
        # Rule 3: Allergy diagnosis
        self.kb.add_rule(
            condition=["has_sneezing", "has_itchy_eyes"],
            conclusion="possible_allergy"
        )
        
        # Rule 4: Recommendation
        self.kb.add_rule(
            condition=["possible_flu"],
            conclusion="recommend_rest_and_fluids"
        )
    
    def diagnose(self, symptoms):
        """Diagnose based on symptoms"""
        # Add symptoms as facts
        for symptom in symptoms:
            self.kb.add_fact(symptom)
        
        # Run inference
        conclusions = self.engine.forward_chaining()
        
        # Get diagnosis
        diagnoses = [c for c in conclusions if c.startswith("possible_")]
        recommendations = [c for c in conclusions if c.startswith("recommend_")]
        
        return {
            'diagnoses': diagnoses,
            'recommendations': recommendations,
            'all_conclusions': conclusions
        }
```

---

### Step 8: Create Main Program (Day 7)

**File: `main.py`**

```python
from medical_system import MedicalDiagnosisSystem

def main():
    print("=" * 50)
    print("Medical Diagnosis Assistant")
    print("=" * 50)
    
    system = MedicalDiagnosisSystem()
    
    # Example: Patient symptoms
    symptoms = [
        "has_fever",
        "has_cough",
        "has_headache"
    ]
    
    print(f"\nPatient symptoms: {symptoms}")
    print("\nRunning diagnosis...")
    
    result = system.diagnose(symptoms)
    
    print("\n" + "=" * 50)
    print("Diagnosis Results:")
    print("=" * 50)
    print(f"Possible conditions: {result['diagnoses']}")
    print(f"Recommendations: {result['recommendations']}")
    print(f"\nAll conclusions: {result['all_conclusions']}")
    
    # Explain reasoning
    if result['diagnoses']:
        print("\n" + "=" * 50)
        print("Explanation:")
        print("=" * 50)
        for diagnosis in result['diagnoses']:
            explanation = system.engine.explain(diagnosis)
            print(explanation)

if __name__ == "__main__":
    main()
```

---

## 🎓 Learning Checklist | قائمة التعلم

- [ ] Day 1: Understand knowledge-based systems
- [ ] Day 2: Create knowledge base structure
- [ ] Day 3: Implement forward chaining
- [ ] Day 4: Implement backward chaining
- [ ] Day 5: Add explanation capability
- [ ] Day 6: Create domain-specific system
- [ ] Day 7: Test with different scenarios
- [ ] Day 8: Add more rules and facts
- [ ] Day 9: Improve user interface
- [ ] Day 10: Write documentation

---

## 💡 Real-World Examples | أمثلة من الحياة الواقعية

### 1. Medical Diagnosis
- Symptoms → Conditions → Treatments

### 2. Technical Support
- Error messages → Problems → Solutions

### 3. Financial Advisor
- Income, expenses → Investment recommendations

### 4. Recipe Recommender
- Available ingredients → Recipe suggestions

### 5. Career Counselor
- Skills, interests → Career paths

---

## 🔧 Troubleshooting | حل المشاكل

**Problem:** No conclusions reached  
**Solution:** Check if facts match rule conditions

**Problem:** Too many conclusions  
**Solution:** Add priority rules or confidence scores

**Problem:** Rules conflict  
**Solution:** Add rule priorities or conflict resolution

---

**Good luck building your knowledge-based system!** 🚀


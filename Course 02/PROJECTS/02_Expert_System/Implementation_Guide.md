# Implementation Guide | دليل التنفيذ
## Project 02: Expert System

---

## Step-by-Step Implementation | التنفيذ خطوة بخطوة

### Step 1: Choose Domain
Examples:
- Medical diagnosis (symptoms → disease)
- Troubleshooting (problems → solutions)
- Recommendations (preferences → suggestions)
- Weather advice (conditions → recommendations)

**Tip:** Choose a domain you understand well!

---

### Step 2: Build Knowledge Base
- Create knowledge graph with NetworkX
- Add entities (nodes)
- Add relationships (edges)
- Define facts

**Example:**
```python
import networkx as nx
G = nx.DiGraph()
G.add_node("Fever", type="symptom")
G.add_node("Flu", type="disease")
G.add_edge("Fever", "Flu", relation="indicates")
```

---

### Step 3: Define Rules
- Create rule class
- Define IF-THEN rules
- Store rules in knowledge base

**Example:**
```python
class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions  # List of facts
        self.conclusion = conclusion  # New fact

rule1 = Rule(["fever", "cough"], "flu")
```

---

### Step 4: Implement Forward Chaining
- Start with known facts
- Apply rules to derive new facts
- Continue until no new facts

**Algorithm:**
1. Initialize with known facts
2. While new facts can be derived:
   - Find rules whose conditions are satisfied
   - Add conclusions to facts
3. Return all derived facts

---

### Step 5: Implement Backward Chaining
- Start with goal
- Find rules that can achieve goal
- Work backwards to find required facts

**Algorithm:**
1. Start with goal
2. Find rules with goal as conclusion
3. For each rule:
   - Check if conditions are known
   - If not, recursively check conditions
4. Return if goal can be achieved

---

### Step 6: Create Interface
- Allow user input
- Process queries
- Display reasoning
- Show conclusions

**Interface Options:**
- Command-line interface (simple)
- Interactive prompt (medium)
- Web interface (advanced)

---

## Code Structure | هيكل الكود

### Recommended File Organization:

```python
# knowledge_base.py
class KnowledgeBase:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.facts = set()
        self.rules = []
    def add_fact(self, fact):
        # Add fact
    def add_rule(self, rule):
        # Add rule

# reasoning_engine.py
def forward_chaining(kb, initial_facts):
    # Forward chaining
def backward_chaining(kb, goal):
    # Backward chaining

# expert_system.py
class ExpertSystem:
    def __init__(self, kb):
        # Initialize
    def query(self, question):
        # Answer question

# interface.py
def get_user_input():
    # Get input
def display_result(result):
    # Display result
```

---

## Testing | الاختبار

### Test Cases:
1. **Simple Query:** Single fact, one rule
2. **Complex Query:** Multiple facts, chain of rules
3. **No Solution:** Goal cannot be achieved
4. **Multiple Solutions:** Several possible conclusions

---

## Troubleshooting | حل المشاكل

### Common Issues:

**Problem:** Rules not firing  
**Solution:** Check rule conditions match facts exactly

**Problem:** Infinite loop in chaining  
**Solution:** Track processed rules/facts to avoid cycles

**Problem:** Knowledge graph too complex  
**Solution:** Start simple, add complexity gradually

---

**See Template folder for starter code!**


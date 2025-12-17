# Course 06 - Course Summary
## ملخص الدورة

This document provides a comprehensive text summary of all course materials.
هذا المستند يوفر ملخص نصي شامل لجميع مواد الدورة.

---


## Pptx Files



### 01

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Bias Detection and Explainable AI
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

1. Identify and detect bias in datasets and machine learning models.  
2. Identify bias mitigation techniques at different stages of the ML pipeline.  
3. Utilize explainability methods like LIME, SHAP, and counterfactual analysis to interpret AI models.

--- Slide 4 ---

Bias Detection and Mitigation Techniques
Bias in machine learning models can lead to unfair or discriminatory outcomes, particularly when working with sensitive attributes like race, gender, or age. This section covers techniques to detect and mitigate bias in data and models. 

Before mitigating bias, it is crucial to detect it. Here are some common approaches:

Methods for Detecting Bias in Data and Models

Data Bias Detection

b. Model Bias Detection

--- Slide 5 ---

a. Data Bias Detection
Disparate Impact Analysis – Measures the proportion of positive outcomes across different demographic groups (e.g., male vs. female).

Statistical Parity Difference – Checks if different groups receive favourable outcomes at similar rates.

Conditional Demographic Disparity (CDD) – Examines disparities within subgroups under similar conditions.

Correlation Analysis – Identifies if sensitive attributes (e.g., race, gender) are highly correlated with the target variable.

--- Slide 6 ---

b. Model Bias Detection
Accuracy Disparity – Measures if the model's performance varies across different demographic groups.

Equalized Odds – Ensures that different groups have equal true positive and false positive rates.

Calibration – Checks if predicted probabilities are consistent across groups.

--- Slide 7 ---

Pre-processing, In-processing, and Post-processing Bias Mitigation Techniques
Bias can be mitigated at different stages of the machine learning pipeline:

Pre-processing Techniques (Before Model Training) 

b. In-processing Techniques (During Model Training)

c. Post-processing Techniques (After Model Training)

--- Slide 8 ---

Pre-processing Techniques (Before Model Training)
Modifies the data to reduce bias before training the model.

Reweighing – Assigns different weights to different data points to balance group representation.

Data Augmentation – Introduces more examples from underrepresented groups.

Fair Representation Learning – Transforms features to be less correlated with sensitive attributes.

Removing Sensitive Attributes – Eliminates biased variables (e.g., race, gender) from the dataset.

--- Slide 9 ---

In-processing Techniques (During Model Training)
Modifies the learning algorithm to reduce bias while training the model.
Adversarial Debiasing – Uses adversarial training to make predictions that are independent of sensitive attributes.

Fairness-Aware Loss Functions – Adds fairness constraints to the model’s loss function.

Regularization for Fairness – Introduces penalties to discourage biased decisions.

--- Slide 10 ---

Post-processing Techniques (After Model Training)
Modifies the model’s predictions to reduce bias after training.

Equalized Odds Post-processing – Adjusts decision thresholds to ensure equal false positive and true positive rates.

Calibrated Equalized Odds – Ensures fairness while maintaining probabilistic calibration.

Reject Option-Based Classification – Allows the model to abstain from making predictions in uncertain cases.

--- Slide 11 ---

Fair Representation Learning and Adversarial Debiasing
These are advanced techniques that use machine learning to learn unbiased data representations.
a. Fair Representation Learning
The goal is to learn transformed features that do not contain bias.
Uses techniques like Principal Component Analysis (PCA) and Autoencoders to remove correlations with sensitive attributes.

b. Adversarial Debiasing
Uses a two-network approach:
Main Model – Predicts the target variable.
Adversarial Model – Predicts the sensitive attribute (e.g., gender, race).
The goal is to minimize the adversary’s ability to predict sensitive attributes, ensuring that the learned features are unbiased.

--- Slide 12 ---

Explainability and Transparency in AI Models
As AI models become more complex, understanding how they make decisions is critical for ensuring fairness, trust, and accountability. 
Explainable AI (XAI) refers to techniques that make AI models more transparent and interpretable, helping stakeholders understand and trust their decisions.

--- Slide 13 ---

Importance of Explainable AI (XAI) in Fairness
AI models can sometimes act as “black boxes,” making decisions that are difficult to interpret. This lack of transparency can lead to bias, unfair treatment, and ethical concerns. Explainability plays a key role in:

Fairness & Bias Detection – Helps identify if a model is making biased decisions based on sensitive attributes (e.g., gender, race).

Trust & Adoption – Users and stakeholders are more likely to trust AI models when they understand how they work.

Regulatory Compliance – Laws like the GDPR (General Data Protection Regulation) require explanations for automated decisions.

Debugging & Model Improvement – Understanding the decision process helps in identifying errors and improving model performance.

--- Slide 14 ---

2. Techniques for Improving Model Interpretability
Several techniques help explain AI models, making their decision-making process transparent:
a. LIME (Local Interpretable Model-agnostic Explanations)
What it does: Generates local explanations by perturbing input features and observing their effect on model predictions.
How it works:
Takes a complex model (e.g., deep learning, ensemble methods).
Creates slightly modified versions of an input instance.
Fits a simple interpretable model (e.g., linear regression) to approximate the complex model’s decision locally.
Use case: Explains individual predictions by highlighting influential features.

--- Slide 15 ---

2. Techniques for Improving Model Interpretability
b. SHAP (SHapley Additive Explanations)
What it does: Assigns importance values (Shapley values) to each feature, showing its contribution to a prediction.
How it works:
Considers all possible feature combinations and their effects on predictions.
Assigns a contribution score to each feature.
Provides global (overall model) and local (specific prediction) explanations.
Use case: Helps understand how features impact model predictions across an entire dataset.

--- Slide 16 ---

2. Techniques for Improving Model Interpretability
c. Counterfactual Analysis
What it does: Finds minimal changes needed in input features to alter a model’s decision.
How it works:
Takes an instance and determines the smallest change needed to produce a different outcome.
Answers questions like: “What if this person had a slightly higher income? Would they have received a loan?”
Use case: Used in fairness auditing, especially for models in finance and hiring.

--- Slide 17 ---

Challenges in Achieving Transparent and Accountable AI
Despite advancements in explainability techniques, several challenges remain:
a. Complexity of Deep Learning Models
Neural networks and transformers have millions of parameters, making them difficult to interpret.
Trade-off between accuracy and interpretability – simpler models are more explainable but may have lower accuracy.
b. Trade-offs Between Fairness and Performance
Reducing bias may lead to lower accuracy for certain groups, making it challenging to balance fairness and model effectiveness.
c. Lack of Standardized Explainability Metrics
There is no universal way to measure explainability, leading to inconsistent implementations across different industries.
d. Risk of Misinterpretation
Users may misunderstand explainability outputs, leading to incorrect conclusions about model fairness.

--- Slide 18 ---

RECAP
Bias Detection & Mitigation

Essential for ensuring fairness and responsibility in AI.
Techniques are applied at different ML pipeline stages (pre-processing, in-processing, post-processing).
Advanced methods like fair representation learning and adversarial debiasing help reduce bias.

Explainability & Transparency

Crucial for ethical AI and fair decision-making.
Methods like LIME, SHAP, and counterfactual analysis improve model interpretability.
Challenge: Balancing accuracy, fairness, and interpretability remains complex.

--- Slide 19 ---

Practice with Google COLAB
Click here 
https://colab.research.google.com/drive/1NWNKmR4i2Pn8WZen2aiBUIwW9T_cI0fD

--- Slide 20 ---

الشراكات العالمية

--- Slide 21 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 02

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Accountability and Ethical challenges in AI Decision-Making
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Define accountability in AI decision-making.
Identify who is responsible for AI decisions (developers, users, organizations).
Explore mechanisms for ensuring AI accountability (audits, certifications, ethical boards).
Understand ethical challenges in AI deployment, including bias, fairness, and security.
Analyze regulatory challenges, including global vs. local AI governance.
Evaluate the role of AI in critical sectors like healthcare, justice, and finance.

--- Slide 4 ---

Introduction to Accountability in AI Systems
Accountability in AI refers to the responsibility of individuals, organizations, or systems for the decisions made by artificial intelligence models. 
AI accountability refers to assigning responsibility for decisions made by AI systems.
This ensures transparency, fairness, and compliance with ethical/legal standards.
As AI systems increasingly influence critical areas like healthcare, finance, and law enforcement, ensuring responsible AI decision-making becomes essential.

Example:
AI-driven loan approval system rejects applications from a particular ethnic group unfairly.
Who is responsible for the bias? The developer? The organization using the AI? The AI itself?

--- Slide 5 ---

Defining Accountability in AI Systems
Accountability in AI involves:

Transparency: Understanding how AI reaches its decisions.

Fairness: Ensuring AI does not reinforce biases or unethical behaviors.

Responsibility: Assigning clear roles for monitoring AI decisions and addressing errors.

Compliance: Adhering to legal and ethical guidelines for AI governance.

--- Slide 6 ---

Key Stakeholders & Their Responsibilities:

--- Slide 7 ---

Mechanisms for Establishing Accountability
Several mechanisms help in ensuring AI accountability:

a) AI Audits
Regularly reviewing AI systems to detect biases and unintended consequences.
Identifying errors in training data, model performance, and real-world applications.

b) Certifications and Standards
AI systems can be assessed against frameworks such as:
ISO/IEC 42001 – AI management system standards.
IEEE Ethically Aligned Design – Guidelines for responsible AI.
Certification ensures AI compliance with ethical and legal standards.

c) Ethical Boards & Governance Committees
Organizations form AI ethics committees to oversee AI deployment.
These boards ensure fairness, prevent discrimination, and protect users.

--- Slide 8 ---

Summarizing AI AccountabilityAI accountability is crucial to prevent misuse and ensure fairness.Multiple stakeholders (developers, organizations, users, regulators) play a role in accountability.AI audits, certifications, and ethical boards help monitor and enforce responsible AI use.Accountability in AI is critical to building trust and mitigating risks. Developers, organizations, and regulators must collaborate to ensure AI systems are transparent, fair, and responsible.By implementing audits, certifications, and ethical oversight, we can create AI systems that align with human values and societal expectations.

--- Slide 9 ---

Emerging Challenges in AI Governance
What is AI Governance?
AI governance refers to the rules, policies, and ethical guidelines that ensure AI is developed and used responsibly.
It covers:
Ethical considerations (bias, fairness, transparency)
Legal and regulatory compliance (global vs. local laws)
Responsible AI use in critical sectors
Example: AI in self-driving cars must follow safety standards, ethical policies, and government regulations to ensure road safety.

--- Slide 10 ---

Ethical Challenges in AI Deployment
Despite AI’s benefits, its deployment raises ethical concerns, including:
a) Bias and Fairness
AI models learn from historical data, which may contain biases.
If not addressed, AI can discriminate against certain groups.
Example: A hiring AI system prefers male candidates because it was trained on past hiring data that had gender bias.
b) Privacy and Security Risks
AI systems collect massive amounts of personal data.
If not protected, this data can be misused for identity theft or surveillance.
Example: Facial recognition AI in public spaces can track individuals without their consent, raising privacy concerns.
c) Transparency and Explainability
Many AI models, like deep learning, act as black boxes, making decisions that humans don’t understand.
Explainability is crucial, especially in healthcare and finance, where wrong decisions affect lives and livelihoods.
Example: A bank's AI denies a loan but doesn’t explain why, leaving the applicant helpless.

--- Slide 11 ---

Regulatory Challenges: Global vs. Local AI Laws
AI regulation is inconsistent across countries, leading to challenges in enforcement.

Lack of Global AI Standards

Some countries, like the EU, have strict AI laws (e.g., the EU AI Act), while others have loose regulations.

This makes it hard to standardize AI safety and ethics globally.

Example: 
A U.S. company deploying AI in Europe must comply with GDPR (data privacy laws), but the same AI might be used with fewer restrictions in other countries.

--- Slide 12 ---

AI and Legal Liability
Who is responsible when AI makes a harmful decision?

Should the developer, company, or AI itself be legally accountable?

Example: If an autonomous car causes an accident, who is responsible—the manufacturer, software developer, or car owner?

--- Slide 13 ---

Ethical AI vs. Business Profits
Companies may prioritize profitability over AI ethics, leading to unsafe or biased AI systems.

Governments struggle to balance AI innovation with consumer protection.

Example: Social media AI recommends harmful content because it increases user engagement, despite ethical concerns.

--- Slide 14 ---

Regulatory Approaches by Region
Point of Discussion:

Should all countries follow the same AI regulations? Why or why not?

Who should be held legally responsible for AI mistakes?

--- Slide 15 ---

AI in Critical Sectors: Risks & Challenges
a) AI in Healthcare
AI improves disease diagnosis, drug discovery, and surgery.Risks:

AI can misdiagnose diseases.
Patient data privacy concerns.
Case Study:

IBM Watson for Cancer Treatment made wrong treatment recommendations because it was trained on hypothetical cases, not real data.

Point of  Discussion :
Should AI make medical decisions without doctors?
How can we ensure AI is safe in healthcare?

--- Slide 16 ---

AI in Critical Sectors: Risks & Challenges
b. AI in Criminal Justice
AI helps analyze crime patterns and predict criminal behavior.Risks:
Racial bias: AI can unfairly target certain racial groups.
Lack of transparency: Courts may use AI recommendations without explaining them. 
Case Study:
The COMPAS AI system in the US wrongly predicted Black defendants as more likely to commit crimes again.
Point of  Discussion :
Should courts use AI to decide prison sentences?
How can AI be made fairer in justice systems?
This Photo by Unknown Author is licensed under CC BY

--- Slide 17 ---

AI in Critical Sectors: Risks & Challenges
AI in Finance
AI helps detect fraud, make investment decisions, and approve loans.
Risks:

AI can unfairly deny loans based on biased data.
AI-driven stock trading could cause market crashes.
Case Study:

AI-driven stock trading caused a "flash crash" in 2010, wiping out $1 trillion in minutes.
Point of  Discussion :

Should AI decide who gets a bank loan?
How can we prevent AI from damaging the economy?

--- Slide 18 ---

Future of AI Governance
AI governance is crucial for ensuring ethical, fair, and safe AI deployment.
Ethical issues like bias and privacy need stronger safeguards.
Global AI regulations should aim for a balance between innovation and responsibility.
AI in healthcare, justice, and finance must be closely monitored to avoid harmful consequences.
AI is powerful but needs ethical and legal oversight.
Bias, security, and fairness are key challenges.
Governments must balance innovation and public safety.

 "AI is only as fair as the data and rules we give it. To create trustworthy AI, we must ensure accountability, transparency, and fairness."

--- Slide 19 ---

الشراكات العالمية

--- Slide 20 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 03

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

AI Accountability & Transparency
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand the importance of AI accountability and transparency.
Explore explainability tools and governance mechanisms.
Learn about real-world case studies.
Identify future directions and challenges.

--- Slide 4 ---

Foundations of AI Accountability
AI accountability refers to the mechanisms and principles that ensure individuals or organizations are answerable for AI systems' behavior and outcomes.
Core Concepts
Accountability: Traceability of AI decisions to responsible entities
Transparency: Visibility into AI system operations and decision logic
Explainability: Ability to interpret and justify AI outputs
Why It Matters
Prevents harm from biased/algorithms
Builds trust with users and regulators
Ensures compliance with evolving regulations (GDPR, EU AI Act)

--- Slide 5 ---

Key Stakeholders

--- Slide 6 ---

Explainability in AI Governance
Explainability ensures that AI models are transparent and understandable not only for developers, but also for stakeholders, regulators, and end-users.
It plays a critical role in AI governance, which is about making sure AI systems are ethical, fair, and accountable.
Technical Approaches to Explainability
There are two main levels of explainability:
1. Global Explanations
Goal: Understand the overall behavior of a model.
Examples:
Feature importance: Which features influence the model the most?
Decision rules: If using decision trees or rule-based systems.
Use case: For developers, auditors, and data scientists to evaluate the model as a whole.

--- Slide 7 ---

Explainability in AI Governance
2. Local Explanations

Goal: Explain why a specific prediction was made.
Common methods:
LIME (Local Interpretable Model-Agnostic Explanations): Builds a simple model around a single prediction to explain it.
SHAP (SHapley Additive exPlanations): Uses game theory to assign importance to each feature in a prediction.
Counterfactuals: Show how a prediction would change if input features were different.
Use case: For explaining individual decisions to users, e.g., why a loan was denied.

--- Slide 8 ---

Implementation Checklist
When implementing explainable AI in practice, consider:
1. Document Model Purpose and Limitations
What is the model used for?
What are its known biases or limitations?

2. Choose Appropriate XAI Methods Based On:
Model complexity:
Simple models (e.g., decision trees) may not need SHAP/LIME.
Complex models (e.g., neural networks) often do.
Stakeholder needs:Data scientists vs business leaders vs customers.
Regulatory requirements:Some sectors (like finance or healthcare) require explanations by law.

3. Establish Explanation Protocols
Design different explanations for:
Technical users: detailed insights.
Non-technical users: simple summaries.
Regulators: documentation and audit trails.

--- Slide 9 ---

Explainability in AI Governance

--- Slide 10 ---

Tools for AI Transparency
These are specialized toolkits and platforms that help make AI models more transparent, fair, and explainable.
Transparency tools help users understand:
How a model works
Why it made a certain prediction
Whether it treats different groups fairly
Toolkits and Platforms
Here are some commonly used tools:

1. IBM AI Explainability 360 (AIX360)
Open-source library by IBM.
Provides algorithms to explain ML models.
Supports both global and local explainability.
Example: Use AIX360 to understand which features most influence a loan approval model.

--- Slide 11 ---

Tools for AI Transparency
2. Google What-If Tool
Interactive tool within TensorBoard.
Allows users to:
Test model predictions by changing inputs.
Explore counterfactuals (What happens if this input changes?).
Visualize decision boundaries.
Great for debugging and understanding models without writing code.
3. Microsoft InterpretML
Library for model interpretability.
Offers techniques like:
SHAP
LIME
GlassBox models (interpretable models by design like Explainable Boosting Machines)
Can be used with many scikit-learn-compatible models.

--- Slide 12 ---

Tools for AI Transparency
4. Fairlearn & AIF360

Fairlearn (by Microsoft): Focuses on fairness metrics and mitigation.
AIF360 (by IBM): Helps identify and mitigate bias in datasets and models.
Example: Check if your model treats male and female users equally.

5. Model Cards & Datasheets
Model cards: Summarize details about an AI model:
Intended use
Performance
Ethical considerations
Datasheets: Similar concept for datasets—explains where the data came from, its limitations, biases, etc.
Helps ensure responsible sharing and usage of models and data.

--- Slide 13 ---

Functionality of These Tools
Why Use These Tools?
Build trust with users and stakeholders.
Meet regulatory requirements (especially in sensitive sectors).
Help debug, improve, and document your models responsibly.

--- Slide 14 ---

Accountability Mechanisms in AI
Goal: Ensure that AI systems are responsible, ethical, and can be held accountable for their outcomes.

To achieve this, organizations use mechanisms at three key stages:

Design-time (Before deployment)

Run-time (During operation)

Post-deployment (After release)

--- Slide 15 ---

Accountability Mechanisms in AI
1. Design-time Mechanisms
These are practices used during the development phase to build responsibility into the system from the start.
Examples:
Documentation (Data Sheets, Model Cards)
Clearly explain:
What the model does
Who it’s for
Its limitations, biases, and performance
Helps reviewers and stakeholders understand the system.
Ethical Risk Assessments
Identify possible ethical issues or harms (e.g., discrimination, surveillance, manipulation) before they happen.
Evaluate the societal and legal risks of using the AI system.
Inclusive Design Processes
Involve diverse voices (ethnicities, genders, abilities, communities) in model design to reduce bias and improve fairness.

--- Slide 16 ---

Accountability Mechanisms in AI
2. Run-time Mechanisms
These are real-time tools and processes that monitor and manage the AI system while it's running.
Examples:
Logging and Audit Trails
Record what the model did, when, and why.
Critical for tracing back decisions if something goes wrong.
Human-in-the-Loop Oversight
Keep a human supervisor in the process for sensitive or high-impact decisions (e.g., medical diagnoses, loan approvals).
Allows humans to override or verify AI decisions.
Performance Monitoring and Anomaly Detection
Keep track of accuracy, fairness, drift, and unexpected behaviors.
Alerts when performance drops or data changes significantly.

--- Slide 17 ---

Accountability Mechanisms in AI
3. Post-deployment Mechanisms
These are actions taken after the AI system is live to ensure continuous accountability.
Examples:
Redressal Mechanisms
Allow users to challenge, report, or appeal decisions (e.g., if an AI system wrongly rejects a loan).
Ensures the system can be corrected or explained.
Feedback Loops
Collect user feedback and use it to refine the system.
Helps adapt to real-world usage and changing needs.
Continuous Improvement and Retraining
Regularly retrain the model with updated data to maintain fairness and performance.
Avoids issues like data drift and outdated behavior.

--- Slide 18 ---

Accountability Mechanisms in AI- summary

--- Slide 19 ---

Implementation Frameworks
These are guidelines, policies, and legal standards that organizations and governments use to ensure that AI systems are ethical, fair, transparent, and accountable.
They help answer:
How do we build AI responsibly?
How do we govern it during use?
How do we respond when things go wrong?
Framework Examples
1. OECD AI Principles
Developed by the Organisation for Economic Co-operation and Development.
Focuses on:
Inclusive growth
Human-centered values
Transparency & accountability
Robustness & security
International cooperation
These principles are adopted by 40+ countries and form a foundation for responsible AI development.

--- Slide 20 ---

Implementation Frameworks
2. EU AI Act (2024)
A landmark regulation by the European Union.
Classifies AI systems by risk level (unacceptable, high, limited, minimal).
Imposes strict requirements for high-risk AI:
Transparency
Risk assessments
Human oversight
Documentation and logging
First major legal framework in the world to regulate AI directly.
3. NIST AI Risk Management Framework
Created by the U.S. National Institute of Standards and Technology.
Helps organizations identify, assess, manage, and monitor AI risks.
Based on principles like:
Fairness
Explainability
Privacy
Trustworthiness
It’s voluntary but widely adopted by enterprises and governments to build responsible AI systems.

--- Slide 21 ---

Enterprise Adoption Strategies
Here’s how companies can put these frameworks into practice:
Integrate Accountability into ML Lifecycle
Embed ethical checks and documentation at each stage:
Data collection
Model training
Deployment
Monitoring
Helps ensure traceability and ethical decision-making throughout the pipeline.
Create Internal Ethics Review Boards
Teams made of:
AI researchers
Policy experts
Legal and ethical advisors
Review sensitive projects before they launch.
Ensures AI is aligned with company values and legal regulations.

--- Slide 22 ---

Enterprise Adoption Strategies
Conduct Impact Assessments
Evaluate how AI systems affect:
People's rights and freedoms
Marginalized communities
Business risks
Tools like Algorithmic Impact Assessments (AIAs) are used.
Helps prevent harm and build public trust.

--- Slide 23 ---

Challenges & Future Directions in AI Governance
Current Issues
These are the major obstacles faced today when building ethical, trustworthy, and explainable AI systems:
1. Trade-off Between Accuracy and Interpretability
Problem: Highly accurate models (like deep neural networks) are often complex and hard to explain.
Example: A deep learning model might diagnose diseases better than a human but can't easily explain why it made a certain decision.
Challenge: How do we balance the need for performance with the need for transparency and user trust?
2. Proprietary Algorithms and Black-Box Models
Many AI systems are built by private companies using closed-source or black-box algorithms.
Users and even regulators often don’t know how the model works or what data it uses. Concern: Lack of transparency can lead to unfair, biased, or unaccountable decision-making (e.g., in hiring, credit, or justice systems).

--- Slide 24 ---

Challenges & Future Directions in AI Governance
3. Lack of Universal Standards
Different countries and companies follow different AI ethics guidelines.
Some follow OECD principles, others NIST, some none at all.
No global framework exists to guide everyone consistently.

Result: Makes it hard to regulate AI across borders, especially for international applications (like social media, healthcare platforms).

--- Slide 25 ---

Future Directions
Here’s where AI governance is heading — these are key areas of development to make AI safer and more trustworthy:
1. Regulatory Harmonization
Goal: Align AI laws and standards across countries and regions.
Efforts like:
EU AI Act
OECD collaborations
UNESCO AI ethics guidance
Benefit: Encourages safe innovation, reduces compliance confusion, and builds global trust.
2.  Interdisciplinary Governance
Combine technology, law, and ethics in decision-making.
Teams should include:
AI Engineers
Legal experts
Social scientists
Ethicists
Purpose: Ensure that AI solutions are not just technically feasible, but also legally compliant and socially responsible.

--- Slide 26 ---

Future Directions
3. Public Engagement in AI Development

Involve citizens and communities in AI design, deployment, and evaluation.

Examples:
Public consultations for national AI policies
Participatory design workshops
Open forums for feedback on AI systems

Outcome: Builds trust, accountability, and inclusiveness in how AI impacts society.

--- Slide 27 ---

Future Directions

--- Slide 28 ---

RECAP
AI Accountability ensures responsible use of AI through principles like responsibility, traceability, and auditability.
Explainability helps stakeholders understand AI decisions, supporting ethical governance and legal compliance (e.g., GDPR).
Transparency Tools like SHAP, LIME, AIF360, and model cards visualize, audit, and explain AI behavior.
Accountability Mechanisms span design-time (risk assessments), run-time (logging, HITL), and post-deployment (feedback, retraining).
Implementation Frameworks such as the EU AI Act, OECD Principles, and NIST RMF guide responsible AI practices.
Case Studies highlight real-world challenges (e.g., COMPAS bias, Amazon hiring tool, healthcare diagnostics).
Current Challenges include interpretability trade-offs, black-box models, and regulatory gaps.

--- Slide 29 ---

Resources for Further Study
The AI Now Institute Reports
OECD Principles on AI
NIST AI Risk Management Framework
"Weapons of Math Destruction" by Cathy O'Neil
Partnership on AI Guidelines

--- Slide 30 ---

الشراكات العالمية

--- Slide 31 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 04

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

AI Regulations and Legal Frameworks
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand the global landscape of AI regulations
Explain the role of GDPR in regulating AI
Identify legal and ethical challenges 
Analyze industry-specific regulatory requirements
Evaluate the impact of AI laws on innovation, accountability, and human rights.
Develop strategies for aligning AI systems with current legal frameworks

--- Slide 4 ---

Overview of Global AI Regulations
Artificial Intelligence (AI) has become a transformative force across industries, raising critical legal and ethical concerns. Governments and international organizations are actively working to establish regulatory frameworks to ensure responsible and safe development and deployment of AI technologies.

--- Slide 5 ---

a. EU AI Act
The EU AI Act is a landmark legislative proposal by the European Union that aims to regulate Artificial Intelligence across its member states. Introduced in April 2021, it is the first major legal framework globally that sets rules for how AI systems should be designed, developed, and used to ensure safety, transparency, and respect for fundamental rights.
Key Elements :
Risk-based approach: AI systems are categorized by the potential risk they pose:
Unacceptable risk (e.g., social scoring by governments) – banned.
High-risk (e.g., AI in medical devices, hiring tools) – subject to strict obligations.
Limited risk – must meet transparency requirements.
Minimal risk – free to operate with no specific regulation.
High-risk systems require:
Detailed documentation
Clear transparency procedures
Human oversight to prevent harmful outcomes.
Prohibited AI practices: Includes systems that manipulate human behavior or exploit vulnerabilities (e.g., scoring systems that evaluate trustworthiness of individuals).

--- Slide 6 ---

a. EU AI Act overview
Status: First comprehensive legal framework on AI proposed by the European Commission in April 2021.
Purpose: To ensure AI systems used in the EU are safe, respect fundamental rights, and are trustworthy.
Key Features:
Risk-based approach: AI systems categorized as unacceptable risk, high risk, limited risk, and minimal risk.
High-risk systems (e.g., biometric ID, critical infrastructure) require strict compliance and transparency.
Obligations for providers and users: documentation, transparency, human oversight.
Prohibits certain AI uses (e.g., social scoring by governments).
Why It Matters:
This Act sets a global precedent for AI regulation. It seeks to balance innovation and safety by ensuring AI is used responsibly, without hindering technological progress. The Act affects developers, providers, and users of AI both within and outside the EU, if their systems impact EU citizens.

--- Slide 7 ---

b. US Executive Orders and Initiatives
The United States takes a sector-specific approach to AI regulation rather than having a single unified AI law like the EU. Instead of one all-encompassing framework, the U.S. uses executive orders, agency-level guidelines, and voluntary frameworks to guide responsible AI development.
Executive Order on Safe, Secure, and Trustworthy AI (2023)
This is a significant policy move by the U.S. government to address the rapid growth and risks of AI. Key highlights include:
Aligning AI with national goals such as economic growth, national security, and civil rights protection.
Establishing protocols for testing, red-teaming, and risk evaluation before deploying AI models—especially those used by the government.
Mandating federal agencies to assess and mitigate harms like bias, misuse, and discrimination in AI systems.
Supporting Initiatives:
NIST AI Risk Management Framework: Offers tools for companies to manage and reduce AI-related risks (accuracy, robustness, fairness).
OSTP Blueprint for an AI Bill of Rights: Suggests principles like data privacy, transparency, and freedom from algorithmic bias.

--- Slide 8 ---

b. US Executive Orders and Initiatives- overview
The United States does not have a unified AI regulation but follows a sectoral approach.
Executive Order on Safe, Secure, and Trustworthy AI (2023):
Ensures AI development aligns with national security, economic competitiveness, and civil rights.
Establishes guidelines for AI testing, risk assessments, and federal use of AI.
Promotes innovation while protecting privacy, civil liberties, and public safety.
Other frameworks: NIST AI Risk Management Framework, OSTP Blueprint for an AI Bill of Rights.

Supporting Initiatives:

NIST AI Risk Management Framework: Offers tools for companies to manage and reduce AI-related risks (accuracy, robustness, fairness).
OSTP Blueprint for an AI Bill of Rights: Suggests principles like data privacy, transparency, and freedom from algorithmic bias.

--- Slide 9 ---

c. Other Countries – AI Regulations Overview
This section highlights how countries outside the EU and US are approaching AI governance. While they may not yet have comprehensive AI laws like the EU AI Act, they are actively shaping their regulatory landscapes.

--- Slide 10 ---

CHINA AI Regulations
Focus: Emphasis on algorithmic transparency and content control.
China has introduced specific rules for recommendation algorithms and generative AI models.
Platforms must ensure their algorithms do not promote harmful content or misinformation.
Providers are also required to register algorithms and provide user control features.

--- Slide 11 ---

Canada AI Regulations
Canada has proposed the Artificial Intelligence and Data Act (AIDA), under Bill C-27.

AIDA aims to regulate high-impact AI systems and promote responsible AI development.

It emphasizes transparency, fairness, and accountability, with enforcement powers granted to a new AI and Data Commissioner.

--- Slide 12 ---

OECD (Organisation for Economic Co-operation and Development) AI Regulations
Not a country, but an international organization with over 30 member nations.
It developed the OECD Principles on AI, a widely adopted framework promoting:
Transparency
Accountability
Fairness
Human-centered values
These principles serve as non-binding global standards influencing national policies.

--- Slide 13 ---

Comparison Table: Global Approaches to AI Regulation

--- Slide 14 ---

GDPR and AI: Privacy and Data Protection Regulations
The General Data Protection Regulation (GDPR), enforced in the European Union since May 2018, has significant implications for AI systems, especially those that rely on personal data.
GDPR’s Relevance to AI
Since many AI systems use personal data (like user profiles, medical records, or facial images), GDPR plays a crucial role in shaping how AI is designed and deployed in the EU.
Key Provisions Impacting AI Systems:
Lawful Basis for ProcessingAI systems must have a legal reason to process data—like user consent or legitimate interest. You can’t just scrape personal data and use it for training without legal grounds.
Data Minimization and Purpose LimitationOnly the minimum data needed should be collected, and only used for clearly stated purposes—no vague or unexpected secondary uses.

--- Slide 15 ---

GDPR and AI: Privacy and Data Protection Regulations
Right to Object and Opt-Out (Article 22)People can opt out of being subjected to decisions made only by AI—especially decisions that significantly affect them (e.g., rejections for jobs or insurance).
Data Protection Impact Assessments (DPIAs)If the AI system is high-risk (e.g., surveillance or profiling), a DPIA is required to assess and mitigate privacy risks before deployment.
Anonymization and PseudonymizationThese are recommended practices to protect identity while still allowing AI to learn from the data.
Importance of Compliance
Violating GDPR can lead to hefty fines (up to €20 million or 4% of global turnover). So AI developers must build privacy into AI systems from the start—a concept known as Privacy by Design.

--- Slide 16 ---

Industry-Specific AI Regulations?
While general AI laws like the EU AI Act or GDPR apply across sectors, industry-specific AI regulations address the unique risks, use cases, and ethical concerns of particular domains. Each sector has specialized rules to ensure that AI systems are safe, ethical, and legally compliant within that context.

--- Slide 17 ---

a. Healthcare
AI is used for diagnostics, personalized medicine, and treatment recommendations. Since health data is extremely sensitive:
Medical Devices: AI-based diagnostic tools often require regulatory approval:
US: Must be approved by the FDA.
EU: Must have CE marking under the Medical Device Regulation.
HIPAA (US): Controls how AI systems handle protected health information (PHI).
Ethical Issues:
Bias in AI models could lead to misdiagnosis.
Patients should give informed consent if AI is used in their treatment.
Explainability is crucial—doctors and patients need to understand AI recommendations.

--- Slide 18 ---

b. Finance
AI is used in fraud detection, algorithmic trading, and credit scoring. It must meet strict governance and transparency standards:
Basel Committee (BCBS): Provides guidance on AI risk management in banking.
DORA (EU): Ensures AI systems are resilient and well-tested.
US regulators: Require model validation and auditability of AI in financial services.
Fair Lending Laws:
Prevent bias or discrimination in automated decisions (e.g., AI denying loans based on race or ZIP code).
Explainability is vital to justify decisions.

--- Slide 19 ---

c. Autonomous Vehicles (AVs)
AI powers self-driving cars, which raises issues about public safety, accountability, and ethics:
UNECE WP.29 (a UN working group): Sets international rules for cybersecurity and software updates in AVs.
National Guidelines:
US (California DMV): Provides rules for AV testing and reporting of crashes.
UK’s AV Bill: Defines liability, insurance, and conditions for autonomous driving.
Key Concerns:
Who is responsible in a crash? The driver, manufacturer, or software developer?
AI must make ethical decisions in complex situations (e.g., crash scenarios).

--- Slide 20 ---

AI Regulation Summary
Helps developers ensure AI applications comply with laws and ethical standards.
Enables businesses to avoid legal risks and penalties through proper compliance.
Supports policymakers in creating robust frameworks that balance innovation and safety.
Promotes transparency and trust among users and the public.
Ensures responsible and fair use of AI technologies across sectors.
Encourages continuous monitoring and adaptation to evolving AI regulations worldwide.

--- Slide 21 ---

Resources for Further Study
EU AI Act – Full Text: https://artificialintelligenceact.eu
Executive Order on Safe, Secure, and Trustworthy AI (2023): https://www.whitehouse.gov
NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
GDPR Text and Resources: https://gdpr.eu
OECD AI Principles: https://oecd.ai
Healthcare AI Regulations (FDA Guidelines): https://www.fda.gov
UNECE Autonomous Vehicle Regulations: https://unece.org

--- Slide 22 ---

الشراكات العالمية

--- Slide 23 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 05

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Building Accountable AI Systems
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Understand the concept of accountable AI 
Identify key components of an AI accountability framework
Explain the role of tracking and auditing mechanisms 
Evaluate human-in-the-loop (HITL) approaches.
Analyze real-world case studies 
Apply best practices.

--- Slide 4 ---

Introduction to Accountable AI Systems
Accountability in AI refers to the ability to assign responsibility for AI-driven decisions and actions. As AI systems become more autonomous, ensuring accountability is crucial to prevent harm, maintain trust, and comply with regulations.
Key Objectives:
Ensure transparency in AI decision-making.
Establish clear responsibility for AI outcomes.
Enable auditing and oversight mechanisms.
Maintain human control where necessary.
Why is it Important?
Prevents misuse or unethical outcomes.
Ensures compliance with laws and regulations (e.g., GDPR, AI Act).
Builds public trust and acceptance.
Enables fair, unbiased, and just AI decision-making.

--- Slide 5 ---

Designing AI Systems with Clear Accountability Frameworks
What is an Accountability Framework?
An accountability framework in the context of AI refers to a structured approach for defining and managing responsibility, transparency, and oversight within the design, deployment, and operation of AI systems.
It ensures that the AI system is not a black box, but rather a well-documented, traceable, and fair system where decisions can be explained, challenged, and improved.
Key Elements of an AI Accountability Framework:
1. Transparency
Ensure that how the AI system works is clear.
Includes documentation of:
Algorithms used
Data sources and preprocessing steps
Model decision-making logic
Helps build trust with stakeholders and regulators.

--- Slide 6 ---

Designing AI Systems with Clear Accountability Frameworks
Key Elements of an AI Accountability Framework:
2. Documentation
Maintain detailed records of:
Design decisions
Training data characteristics
Model updates or tuning
Validation metrics
Acts as a reference for audits, debugging, and future improvements.
3. Attribution
Clearly identify:
Who developed the model?
Who is responsible for monitoring?
Which department owns the system?
Ensures that accountability lies with a team or person, not just the "AI."

--- Slide 7 ---

Designing AI Systems with Clear Accountability Frameworks
Key Elements of an AI Accountability Framework:

4. Evaluation & Monitoring

Continuous performance checks:
Is the model fair to all groups?
Is it making biased or incorrect predictions?

Regular audits using tools like:
Fairness dashboards
Drift detection tools
Explainability methods (e.g., LIME, SHAP)

--- Slide 8 ---

Designing AI Systems with Clear Accountability Frameworks
Why Is It Important?

Regulatory Compliance: Many regions now mandate explainable and fair AI (e.g., GDPR in the EU).
Ethical Assurance: Helps avoid harm due to bias or unexplainable errors.
Organizational Trust: Promotes confidence among users, stakeholders, and clients.
Operational Continuity: Ensures issues can be traced and resolved efficiently.
Tools & Practices for Building Accountable AI:

Documentation: Model cards, data sheets for datasets
Explainability: SHAP, LIME
Governance Platforms: IBM AI Factsheets, Google’s Model Monitoring
Ethical Frameworks: OECD AI Principles, EU’s AI Act

--- Slide 9 ---

Key Components of an Accountability Framework:
Example:
In a loan approval system, the framework should:
Log who approved the training dataset.
Track decisions made by the AI.
Allow customers to appeal and get explanations.

--- Slide 10 ---

Mechanisms for Tracking and Auditing AI Decision-Making
As AI systems become more influential in areas like finance, healthcare, education, and justice, it's essential that every decision they make can be tracked, understood, and justified. This is where auditing mechanisms come into play.
Below are five core mechanisms used to ensure accountability, transparency, and fairness in AI.

--- Slide 11 ---

A. Logging and Monitoring
Model Inputs & OutputsWhat it means: Every time an AI system makes a prediction, record the data it received (input) and the prediction it made (output).Why it matters: Helps in tracing back to see why the model made a certain decision, especially in critical applications like fraud detection or medical diagnosis.Example:An AI model denies a loan application.Logs show the input features: age, credit score, income.Output: “Not eligible” with a confidence score of 0.85.
2. Metadata Tracking
What it includes:
Model version used
Date/time of prediction
Confidence score
Type of device or location (if relevant)
Who triggered the prediction (user/system)
Purpose: Ensures every action is traceable, allowing teams to audit behavior across versions and use contexts.

--- Slide 12 ---

B. Model Cards and Data Sheets
Inspired by food nutrition labels, these provide standardized documentation for AI systems and datasets.
 Model Cards:
Describe a trained model in terms of:
Purpose and use cases
Performance across various data segments
Limitations and known issues
Ethical and fairness considerations
Data Sheets:
Focus on the datasets used in training/testing:
How the data was collected
Intended use of the data
Potential biases
Preprocessing steps
Why Use These?
They communicate model behavior clearly to developers, reviewers, and non-technical stakeholders.
Encourages transparency and ethical thinking during model development.

--- Slide 13 ---

C. Explainability Tools
Tools like:
SHAP (SHapley Additive exPlanations)
LIME (Local Interpretable Model-Agnostic Explanations)
Purpose:
These tools explain why a model made a specific prediction by highlighting the most influential features.
They break the “black-box” nature of many ML models like deep neural networks and ensemble trees.
 Example:
A SHAP graph might show that for a patient diagnosed with diabetes risk, the most influential factors were age, BMI, and glucose level.

--- Slide 14 ---

D. Audit Trails
What are they?
Digital logs that chronologically record each action, change, or decision the AI system makes.

Why important?
Allow internal or external parties to review the historical performance of the system.
Especially useful for:
Legal investigations
Security breaches
Regulatory compliance

Example:
A healthcare audit reveals that an AI model made several misdiagnoses on a certain population group. The trail shows a recent model update introduced a bias.

--- Slide 15 ---

E. Bias & Fairness Audits
Purpose:
To test if the AI model unintentionally discriminates against any group based on age, gender, ethnicity, etc.
Tools:
Fairlearn (by Microsoft)
AI Fairness 360 (by IBM)
These tools quantify bias and help retrain models to reduce it.
Example:
In a job recruitment AI, if it selects fewer female candidates despite similar qualifications, a fairness audit can uncover and fix the bias.

--- Slide 16 ---

Real-Life Example: AI in Healthcare
Let’s say an AI system recommends treatments based on patient data:
Logging captures input symptoms, history, and suggested treatment.
Metadata includes which version of the model was used.
SHAP explains that “low white blood cell count” was the main reason behind the recommendation.
Model Card outlines that this model performs less accurately on children under 12.
Audit Trail shows a doctor overrode the AI suggestion twice that week.
Bias Audit highlights that the system underperforms on patients from certain ethnic backgrounds.

--- Slide 17 ---

Human-in-the-Loop (HITL) Approaches in AI
Human-in-the-loop (HITL) is a strategy in AI system design where humans are actively involved in the model lifecycle  from training and testing to deployment and monitoring to provide oversight, guidance, and corrections.
This approach is especially important in sensitive or high-stakes domains, where automated systems must be auditable, ethical, and aligned with human values.

--- Slide 18 ---

Human-in-the-Loop (HITL) Approaches in AI
A. Types of HITL Models
These models ensure ethical governance and retain human judgment,
 especially where errors could have significant consequences.

--- Slide 19 ---

B. Benefits of HITL
1. Ethical and Responsible AI
Prevents AI from making fully autonomous decisions that may be biased or incorrect.
Ensures decisions are aligned with human norms, values, and regulations.
2. Improved Decision-Making
Combines AI's speed and pattern recognition with human judgment and context-awareness.
Especially critical in healthcare, law enforcement, finance, and recruitment.
3. Transparent and Traceable AI
Enables documentation and justification of decisions, boosting trust and accountability.
4. Continuous Learning
Human feedback can be used to fine-tune or retrain models, improving their accuracy and fairness over time.

--- Slide 20 ---

C. Challenges of HITL
1. Slower Workflow
Involving humans at each stage may slow down operations compared to fully automated systems.
Example: Reviewing hundreds of AI-generated resumes takes time.

2. Need for Skilled Personnel
Personnel must understand how to interpret AI outputs, identify biases, and provide meaningful feedback.
This often requires training and awareness programs.

3. Risk of Overreliance on AI
Even with human oversight, people may blindly follow AI suggestions, especially when AI is perceived as highly accurate.
This can lead to rubber-stamping behavior without critical evaluation.

--- Slide 21 ---

Real-World Use Cases
Healthcare
Pre-decision: Medical experts curate and validate training data for radiology models.
Mid-decision: A radiologist uses an AI tool to detect tumors but makes the final call.
Post-decision: Hospital reviews treatment recommendations after patient feedback or outcomes.
HR and Recruitment
AI scores resumes → Human checks for bias or missing nuances → Final list sent to interviewers.
Finance
AI detects potentially fraudulent transactions → Human analysts verify and take action.

--- Slide 22 ---

Google Photos Tagging Incident — A Case Study in AI Accountability
Problem: AI Mislabeled African-Americans as “Gorillas”
In 2015, Google Photos’ AI-based image recognition system automatically tagged African-American individuals in photos as “gorillas.”This was not only a technical failure but also a deeply offensive and harmful mistake, sparking widespread public outrage.
Accountability Issue
1. Inadequate and Biased Training Data
The model was likely trained on a dataset not representative of diverse racial groups.
Underrepresentation of people of color in the training set led to misclassification due to lack of feature differentiation.
2. Lack of Human Review and Testing
The system went live without thorough Human-in-the-Loop testing, especially for sensitive and socially impactful labels.
There was no safety mechanism or human audit to detect and correct this harmful classification before deployment.

--- Slide 23 ---

Google Photos Tagging Incident — A Case Study in AI Accountability
Solution: Human-in-the-Loop and Dataset Audits
To address the problem, Google implemented several measures, including:
1. Stricter HITL Testing
Introduced human review checkpoints during AI training and testing.
Now, sensitive labels (like race, gender, religion) undergo manual verification and are often disabled by default to avoid offensive outputs.
2. Improved Dataset Curation and Auditing
Conducted bias audits on training datasets to ensure diverse and representative samples.
Applied data augmentation and rebalancing techniques to reduce bias.
3. Limiting Sensitive Categories
For example, Google removed the ability to tag images as “gorillas” altogether to prevent similar incidents until the technology improves.

--- Slide 24 ---

Best Practices Checklist for Building Accountable AI
Assign clear roles (e.g., Data Steward, Ethics Officer)
Maintain detailed documentation (Model cards, Data sheets)
Use explainable AI tools (SHAP, LIME)
Conduct regular bias and fairness audits
Build feedback loops and appeal mechanisms
Involve humans in sensitive decisions
Monitor performance post-deployment
Ensure compliance with relevant legal frameworks (GDPR, AI Act)

--- Slide 25 ---

Summary
Accountable AI ensures transparency, fairness, and ethical responsibility in AI systems, especially in sensitive applications like healthcare and justice.
Accountability frameworks define roles, responsibilities, ethical guidelines, and documentation processes to govern AI lifecycle and decision-making.
Tracking and auditing mechanisms—including logging, model cards, explainability tools (like SHAP, LIME), and bias audits—help monitor and understand AI decisions.
Human-in-the-loop (HITL) approaches involve human oversight during AI input, decision-making, or post-decision review, ensuring control and reliability.
Case studies reveal the risks of lacking accountability (e.g., COMPAS bias, Google Photos mislabeling) and stress the need for ethical checks.
Best practices include using explainable AI, regular audits, stakeholder involvement, proper documentation, and compliance with legal regulations.

--- Slide 26 ---

Resources for Further Study
EU AI Act (Regulation on AI accountability)
Google’s Responsible AI Practices
IBM’s AI Fairness 360 Toolkit
Ethics of AI – Stanford Encyclopedia
Microsoft Responsible AI
Google Responsible AI

--- Slide 27 ---

الشراكات العالمية

--- Slide 28 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 06

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Case Studies on Bias and Fairness &Practical Approaches to Fair AI Development
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Recognize the ethical implications of AI in decision-making and its impact on society.
Learn about risks such as bias, privacy violations, and unintended consequences in AI models.
Explore frameworks and techniques for ensuring fairness, transparency, and accountability in AI systems.

--- Slide 4 ---

Case Studies on Bias and Fairness
Bias in AI systems can have significant real-world consequences, particularly in high-stakes applications like hiring, law enforcement, finance, and facial recognition. Below are some well-documented case studies demonstrating these biases:
Facial Recognition and Racial Bias
 Gender Bias in Hiring Algorithms
Predictive Policing and Criminal Justice AI
Discrimination in Credit Scoring and Lending AI

--- Slide 5 ---

Facial Recognition and Racial Bias
🔹 Issue: Facial recognition models have been found to have higher error rates for people with darker skin tones compared to lighter-skinned individuals.🔹 Example: A 2018 study by MIT Media Lab showed that commercial facial recognition systems from major tech companies had misclassification rates of up to 34% for darker-skinned women but less than 1% for lighter-skinned men.🔹 Impact: This bias has led to wrongful arrests, misidentification, and racial profiling in law enforcement.🔹 Solution: Improving diversity in training datasets, using debiasing techniques, and implementing human oversight in decision-making.

--- Slide 6 ---

Gender Bias in Hiring Algorithms
🔹 Issue: AI-based hiring tools have exhibited gender discrimination, often favoring male candidates over female candidates.🔹 Example: In 2018, Amazon’s hiring algorithm was found to downgrade resumes containing the word “women”(e.g., "women’s chess club") because it was trained on historical hiring data, which had male dominance.🔹 Impact: Women were unfairly filtered out from job opportunities, reinforcing existing workplace inequality.🔹 Solution: Using gender-neutral language, fairness constraints in model training, and regular audits of AI decisions.

--- Slide 7 ---

Predictive Policing and Criminal Justice AI
🔹 Issue: Predictive policing AI, which aims to predict where crimes will occur or assess the likelihood of individuals committing crimes, has been shown to reinforce systemic racial biases.🔹 Example: COMPAS (Correctional Offender Management Profiling for Alternative Sanctions), a criminal risk assessment tool, was found to incorrectly classify Black defendants as "high risk" at almost twice the rate of white defendants.🔹 Impact: Unfair sentencing, over-policing of minority communities, and disproportionate imprisonment rates.🔹 Solution: Implementing transparency in AI decision-making, removing racially biased historical data, and using fairness-aware models.

--- Slide 8 ---

Discrimination in Credit Scoring and Lending AI
🔹 Issue: AI-driven credit scoring models have been found to discriminate against minority groups, leading to unfair denials of loans and higher interest rates.🔹 Example: A 2019 study found that Black and Hispanic borrowers were charged higher interest rates for home loans compared to white borrowers with similar financial backgrounds.🔹 Impact: Economic inequality, reduced financial opportunities for marginalized groups, and long-term wealth disparity.🔹 Solution: Implementing fairness-aware machine learning models, using explainable AI (XAI) techniques to detect bias, and ensuring regulatory compliance.

--- Slide 9 ---

Practical Approaches to Fair AI Development
To mitigate bias and build fair AI systems, organizations should adopt ethical and inclusive AI development strategies.

Ethical AI Principles in Model Design

Ensuring AI systems align with human values and promote fairness, transparency, and accountability.

Adopting frameworks like Fairness, Accountability, and Transparency in Machine Learning (FAT/ML) to guide ethical decision-making.

Regularly conducting AI audits to check for unintended biases.

--- Slide 10 ---

Inclusive Data Collection and Bias-Aware Algorithms
Ensuring datasets represent diverse populations to prevent bias.
Applying bias mitigation techniques at different stages of the ML pipeline:
Pre-processing: Rebalancing datasets to reduce bias before training.

In-processing: Modifying the learning algorithm to ensure fairness.

Post-processing: Adjusting model outputs to correct biases after training.

--- Slide 11 ---

Human-in-the-Loop Approaches for Fairness Evaluation
Combining AI decision-making with human oversight to reduce errors and biases.

Involving domain experts, ethicists, and affected communities in AI evaluation and policy-making.

Using explainable AI (XAI) tools like SHAP and LIME to ensure transparency and accountability.

--- Slide 12 ---

RECAP
1️⃣ AI Bias in Critical Areas – Bias in AI affects high-stakes domains such as facial recognition, hiring, criminal justice, and credit scoring, leading to unfair outcomes.
2️⃣ Facial Recognition Bias – AI models have higher error rates for darker-skinned individuals, resulting in misidentification and racial profiling in law enforcement.
3️⃣ Gender Bias in Hiring – AI-driven hiring tools have favored male candidates due to biased historical data, reinforcing workplace inequalities.
4️⃣ Predictive Policing Issues – AI models like COMPAS have wrongly classified Black defendants as high-risk, leading to racial discrimination in criminal justice.
5️⃣ Discrimination in Credit Scoring – AI-based loan approval systems have unfairly assigned higher interest rates to minority groups, widening economic disparities.
6️⃣ Ethical AI Development – Fair AI requires inclusive data collection, fairness-aware algorithms, and bias mitigation techniques at different stages of model development.
7️⃣ Human-in-the-Loop Approaches – AI systems should integrate human oversight, fairness evaluations, and explainability techniques like SHAP and LIME to enhance transparency.
8️⃣ Accountability & Regulation – Organizations must regularly audit AI models, ensure compliance with ethical standards, and adopt fairness frameworks for responsible AI deployment.

--- Slide 13 ---

الشراكات العالمية

--- Slide 14 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 07

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Data protection strategies and technologies
By: Dr. Afshan Hashmi
Privacy and Security by Design

--- Slide 3 ---

Course Objectives:

Explain encryption techniques and secure data storage methods.
Differentiate between anonymization and pseudonymization.
Understand secure multi-party computation and homomorphic encryption. 
Apply secure software development practices to prevent vulnerabilities

--- Slide 4 ---

Encryption Techniques and Secure Data Storage
Encryption is the process of converting data into a coded format to prevent unauthorized access. Secure data storage ensures that encrypted data is stored safely.
How it works:
Symmetric Encryption: Uses a single key for both encryption and decryption (e.g., AES).
Asymmetric Encryption: Uses a pair of keys (public and private) for encryption and decryption (e.g., RSA).
Secure Storage: Encrypted data is stored in secure environments like encrypted databases, hardware security modules (HSMs), or cloud storage with encryption at rest.
Why it’s important:
Protects sensitive data from breaches and unauthorized access.
Ensures compliance with data protection regulations (e.g., GDPR, HIPAA

--- Slide 5 ---

Anonymization and Pseudonymization of Personal Data
Anonymization: Irreversibly removing personally identifiable information (PII) so that the data cannot be linked back to an individual.
Pseudonymization: Replacing PII with pseudonyms (e.g., unique identifiers) so that the data can only be re-identified with additional information.
How it works:
Anonymization: Techniques include data masking, generalization, and noise addition.
Pseudonymization: Techniques include tokenization and encryption with key management.
Why it’s important:
Reduces the risk of data breaches and misuse.
Helps comply with privacy laws like GDPR, which encourage pseudonymization as a best practice.

--- Slide 6 ---

Anonymization of Personal Data
Anonymization involves removing personally identifiable information from data, making it impossible to trace back to an individual. 

Anonymized data cannot be re-identified, ensuring privacy protection. 

This is often used in research or when sharing data publicly for analysis.

--- Slide 7 ---

Pseudonymization of Personal Data
Pseudonymization replaces identifiable data elements (e.g., names or addresses) with artificial identifiers or pseudonyms, allowing the data to be processed without directly identifying individuals. 

Unlike anonymization, pseudonymized data can potentially be re-identified if the pseudonymization key is available.

--- Slide 8 ---

Secure Multi-Party Computation (SMPC)
What it is:A cryptographic technique that allows multiple parties to jointly compute a function over their inputs while keeping those inputs private.How it works:Data is split into shares and distributed among parties.Computations are performed on the shares without revealing the actual data.The final result is reconstructed without exposing individual inputs.Why it’s important:Enables collaboration on sensitive data without sharing raw data (e.g., financial institutions analyzing fraud patterns).Enhances privacy in distributed systems.

--- Slide 9 ---

Homomorphic Encryption
What it is:A form of encryption that allows computations to be performed on encrypted data without decrypting it first.
How it works:
Data remains encrypted during processing.
The result of the computation is also encrypted and can only be decrypted by the authorized party.
Why it’s important:
Enables secure outsourcing of data processing (e.g., cloud computing).
Protects sensitive data during analysis (e.g., healthcare data).

--- Slide 10 ---

Building Privacy and Security into AI Systems from the Start
AI systems often process sensitive data, making it crucial to embed privacy and security measures from the early design phase.
Key principles include:

Data Minimization: Collect only the data necessary for the task.
Differential Privacy: Introduce controlled noise into datasets to protect individual privacy.
Federated Learning: Train models on decentralized data to prevent unnecessary data sharing.
Explainability & Transparency: Ensure AI decisions are interpretable and bias-free.
Secure Data Handling: Encrypt sensitive data and apply strict access controls.

--- Slide 11 ---

Privacy-Enhancing Technologies (PETs)
Privacy-enhancing technologies (PETs) help protect user data and minimize privacy risks while allowing organizations to derive insights from data. Examples include:

Homomorphic Encryption: Enables computations on encrypted data without decrypting it.

Secure Multi-party Computation (SMPC): Allows multiple parties to compute on combined data without revealing their inputs

Differential Privacy: Adds noise to datasets to prevent re-identification of individuals.

Zero-Knowledge Proofs (ZKPs): Allow verification of data without revealing the actual data.

Synthetic Data: Generates artificial datasets with similar statistical properties to real data, ensuring privacy.

--- Slide 12 ---

Implementing Secure Software Development Practices
Secure software development ensures that applications and AI models are resistant to security threats from the ground up. Best practices include:
Secure Coding: Follow secure coding guidelines (e.g., OWASP Top 10) to prevent vulnerabilities like SQL injection and cross-site scripting (XSS).

Regular Security Testing:
Static Application Security Testing (SAST): Identifies vulnerabilities in source code.
Dynamic Application Security Testing (DAST): Tests running applications for security flaws.
Penetration Testing: Simulates real-world attacks to find weaknesses.

Code Reviews and Threat Modeling: Identify potential threats early in the development cycle.

Access Control and Authentication: Use multi-factor authentication (MFA), role-based access control (RBAC), and secure APIs.

--- Slide 13 ---

Summary Table

--- Slide 14 ---

الشراكات العالمية

--- Slide 15 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 08

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Explainable AI and its Techniques
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Understand the importance of explainability in AI for trust, accountability, and adoption.
Differentiate between explainability (post-hoc) and interpretability (inherent simplicity).
Identify challenges in explaining complex models like deep learning and ensemble methods.
Compare local (individual predictions) and global (overall behavior) explanations.
Apply post-hoc explainability methods like LIME, SHAP, and Partial Dependence Plots.

--- Slide 4 ---

Importance of Explainability
Why Explainability Matters:
Builds trust in AI systems by making their decisions transparent.
Ensures accountability for decisions made by AI models.
Facilitates adoption in regulated industries (e.g., healthcare, finance).
Helps identify and mitigate biases in AI models.
Example:
In healthcare, an AI model predicting diseases must explain why it flagged a patient as high-risk to gain the trust of doctors and patients.

--- Slide 5 ---

Difference Between Explainability and Interpretability
Explainability:
Refers to the ability to describe how a model makes decisions, often using post-hoc methods.
Example: Using SHAP values to explain a black-box model’s predictions.
Interpretability:
Refers to the inherent simplicity of a model, making its decisions easy to understand.
Example: A linear regression model is interpretable because its coefficients directly show the impact of features.

--- Slide 6 ---

Challenges in Explaining Complex AI Models	Deep Learning Models:Highly complex architectures (e.g., neural networks) make it hard to trace decision-making processes.Ensemble Methods:Models like Random Forests or Gradient Boosting combine multiple weak learners, making it difficult to explain the overall behavior.Trade-offs:Simpler models are more interpretable but may sacrifice accuracy.Complex models are more accurate but harder to explain.

--- Slide 7 ---

Techniques for Explainable AI (XAI)
Local vs. Global Explanations

Local Explanations:
Explain individual predictions (e.g., why a specific loan application was rejected).
Example: LIME (Local Interpretable Model-agnostic Explanations).
Global Explanations:
Explain the overall behavior of the model (e.g., which features are most important across all predictions).
Example: Feature importance in Random Forests.

--- Slide 8 ---

Advanced Tools and Libraries
SHAP: Unified framework for explainability.
LIME: Local interpretability for any model.
ELI5: Debugging and inspecting machine learning models.
Alibi: Advanced explainability for black-box models.

--- Slide 9 ---

Post-Hoc Explainability Methods
LIME (Local Interpretable Model-agnostic Explanations)
Insights:
LIME approximates a complex model locally with a simpler model (e.g., linear regression).
It works by perturbing the input data and observing changes in predictions.
Limitations:
Sensitive to the choice of perturbation method.
May produce inconsistent explanations for similar inputs.

--- Slide 10 ---

Post-Hoc Explainability Methods
LIME (Local Interpretable Model-agnostic Explanations)
Note : That LIME is able to explain the importance of each Feature responsible for a particular Predictions

--- Slide 11 ---

SHAP (SHapley Additive exPlanations)
Insights:
SHAP values are based on cooperative game theory and provide a unified measure of feature importance.
They satisfy properties like efficiency, symmetry, and additivity.
Limitations:
Computationally expensive for large datasets or complex models.
May not capture interactions between features well.

--- Slide 12 ---

SHAP (SHapley Additive exPlanations)
Note: SHAP is representing each features value from low to high and positive to negative

--- Slide 13 ---

Partial Dependence Plots (PDP)
Insights:
PDP shows the marginal effect of a feature on the predicted outcome.
It helps understand feature interactions and non-linear relationships
Limitations:
Assumes features are independent.
May be misleading if features are highly correlated.

--- Slide 14 ---

Partial Dependence Plots (PDP)

--- Slide 15 ---

ELI5 (Explain Like I’m 5) - Debugging and Inspecting ML Models
ELI5 is a python package that is used to inspect ML classifiers and explain their predictions. 

It is popularly used to debug algorithms such as sklearn regressors and classifiers, XGBoost, CatBoost, Keras, etc. 

ELI5 helps inspect machine learning models by showing feature importance and explaining predictions in an interpretable way. 

It works with scikit-learn, XGBoost, and deep learning models.

--- Slide 16 ---

ELI5 (Explain Like I’m 5) - Debugging and Inspecting ML Models
Trains a RandomForestClassifier on the Iris dataset.
Uses Permutation Importance to determine how much each feature contributes to predictions. 

Displays feature importance using eli5.show_weights().

--- Slide 17 ---

Alibi - Explainability for Black-Box Models
Alibi Explain is a freely available Python toolkit designed to shed light on how machine learning models arrive at their predictions. 
It provides a collection of advanced explainability techniques suitable for both classification and regression tasks.
 These techniques can be applied regardless of whether you have detailed knowledge of the model's inner workings (black-box) or complete access (white-box). 
The library handles diverse data formats, including tables, text, and images, and offers explanations at both the individual prediction level and the overall model behavior. 
To ensure ease of use, Alibi Explain features a consistent programming interface. 
The project emphasizes robust development practices, with comprehensive testing implemented to guarantee code reliability and algorithm accuracy.

--- Slide 18 ---

Alibi - Explainability for Black-Box Models
Uses AnchorTabular from Alibi to generate interpretable rule-based explanations.
Finds anchors (conditions in the input) that strongly influence the model’s prediction.
Prints a simple rule explaining why a decision was made.

--- Slide 19 ---

Surrogate Models and Rule-Based Approximations
Surrogate Models:
Train a simpler model (e.g., decision tree) to approximate the behavior of a complex model.
Example: Use a decision tree to explain a neural network’s predictions.
Rule-Based Approximations:
Extract human-readable rules from a model (e.g., using RuleFit or SkopeRules).
Example: "If age > 30 and income < $50,000, then reject loan application."

--- Slide 20 ---

Advanced Applications of XAI
3.1 Model Debugging
Use SHAP or LIME to identify why a model is making incorrect predictions.
Example: Diagnosing why a medical diagnosis model is failing for certain patient groups.
3.2 Feature Engineering
Use feature importance from SHAP or PDP to identify the most impactful features.
Example: Removing irrelevant features to improve model performance.
3.3 Bias Detection
Use XAI techniques to detect and mitigate biases in AI models.
Example: Identifying gender bias in a hiring algorithm.

--- Slide 21 ---

Hands-On Activity
Activity: Explain a Model Using SHAP and LIME

Train a complex model (e.g., Random Forest or Neural Network) on a dataset (e.g., Iris or Titanic).

Use SHAP to explain global feature importance.

Use LIME to explain individual predictions.

Compare the explanations and discuss their strengths and limitations.

--- Slide 22 ---

Summary
Explainability is crucial for building trust, ensuring accountability, and facilitating adoption of AI systems.

Techniques like LIME, SHAP, and PDP provide insights into model behavior at both local and global levels.

Surrogate models and rule-based approximations simplify complex models for better understanding.

--- Slide 23 ---

Practice with Google COLAB
Click here 
https://colab.research.google.com/drive/14ZWbmJ4GeT4PPLjuz3kLV2tIWoMVz0z-

--- Slide 24 ---

الشراكات العالمية

--- Slide 25 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 09

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Ethical and Legal Considerations in AI
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Analyze AI’s Impact on Human Rights
Assess Liability Frameworks for AI Decisions
Apply Legal and Ethical AI Principles
Interpret Global AI Regulations
Conduct Algorithmic Impact AssessmentsDebate Emerging Challenges in AI Ethics

--- Slide 4 ---

Introduction to AI Ethics & Law
Why Ethics & Law Matter in AI
AI impacts privacy, employment, justice, and democracy
Risks: Bias, discrimination, surveillance, loss of autonomy
Need for legally compliant, fair, and accountable AI
Key Definitions

--- Slide 5 ---

Core Ethical Principles in AI
Fairness (Avoid bias in training data & decisions)
Transparency (Explainable & auditable AI)
Accountability (Clear responsibility for AI outcomes)
Privacy (Compliance with data protection laws)
Human Oversight (No fully autonomous high-stakes decisions)

--- Slide 6 ---

AI and Human Rights
1. Privacy Rights & AI

Mass surveillance risks (e.g., facial recognition misuse)
Data protection laws:
GDPR (EU): Requires consent, data minimization, and right to erasure
CCPA (US): Gives users control over personal data

AI Privacy Risks:
Re-identification from anonymized data
Invasive profiling (e.g., targeted ads based on sensitive data)

--- Slide 7 ---

2. Freedom & Autonomy
AI technologies can impact individual freedom and autonomy, which are fundamental human rights. Let’s break down how:
AI in Social Media: Filter Bubbles, Misinformation, and Manipulation
Filter Bubbles: Algorithms personalize content based on your behavior, likes, and clicks. This means you only see content that agrees with your views — limiting exposure to diverse perspectives.
Impact: Reduces critical thinking and can polarize society.
Misinformation: AI-driven bots or poorly regulated content recommendation systems can spread false information rapidly.
Ethical Concern: Users are manipulated into forming opinions or beliefs based on inaccurate data.
Manipulation: AI can be used to manipulate emotions, voting decisions, or purchasing behavior (e.g., Cambridge Analytica scandal).
Freedom at Risk: People may make choices influenced by hidden AI nudges, rather than true free will.

--- Slide 8 ---

Autonomous Weapons: Ethical Concerns Over AI-Driven Warfare
These are weapons systems that can select and attack targets without human intervention.
Key Ethical Issues:
Who is responsible if an AI weapon makes a mistake?
Can machines ethically decide to take a life?
Lack of transparency and accountability in lethal decisions.
Autonomy vs. Control: When machines have the power to kill without human judgment, we risk undermining human dignity and international law.

--- Slide 9 ---

Job Displacement: Ethical Responsibility in Workforce Automation
AI is replacing jobs in manufacturing, customer service, driving, etc.
Example: Self-driving trucks replacing truck drivers.
Concerns:
Loss of livelihood for many workers.
Increased inequality if reskilling programs or safety nets are not provided.
Ethical Duty: Companies and governments have a responsibility to ensure:
Fair transitions
Access to retraining and education
Protection of workers' rights

--- Slide 10 ---

Non-Discrimination & Bias Mitigation
AI systems must be fair, just, and non-discriminatory. Unfortunately, many real-world systems unintentionally reinforce or even amplify biases. This section explores where bias comes from and how we can address it.
Sources of AI Bias
AI bias doesn't just happen — it’s often the result of decisions made during development. Let’s break it down:
 1. Biased Training Data
What it means: If the historical data used to train the AI is biased, the AI learns those same patterns.
Example:
A hiring algorithm trained on past data that favored men over women might learn to prefer male candidates.
Facial recognition systems that perform poorly on people with darker skin tones because the training data lacked diversity.
Result: Discrimination in predictions or decisions — even if unintentional.

--- Slide 11 ---

2. Flawed Model Design
What it means: Sometimes, models indirectly learn sensitive attributes through proxies.

Example:
A loan approval model may not use race explicitly but uses ZIP code — which can correlate with race or socioeconomic status.
Ethical Risk: Even if sensitive features aren’t used, indirect bias can still creep in.

--- Slide 12 ---

Mitigation Strategies
Now let’s look at how we can prevent or reduce bias in AI systems.
1. Fairness-Aware Machine Learning
These are ML frameworks designed to measure and reduce bias in predictions.
Popular Tools:
IBM’s AIF360 (AI Fairness 360):
Open-source library that helps detect and mitigate bias.
Provides fairness metrics and bias mitigation algorithms.
Google’s Fairness Indicators:
Tools for TensorFlow that track performance across different subgroups.
Use Case: Monitor whether your model treats all groups fairly before deployment.

--- Slide 13 ---

Mitigation Strategies
2. Bias Audits (Pre- and Post-Deployment)
What it means: Regular checks to see if bias exists before launching the AI system (pre-deployment) and while it is running (post-deployment).
Why important:
Systems may become biased over time as they adapt to new data.
Ethical & legal accountability requires ongoing monitoring.

--- Slide 14 ---

Liability & Accountability in AI Decisions
Who is Responsible When AI Fails?
As AI systems make increasingly impactful decisions — from medical diagnoses to loan approvals to driving vehicles — the question of liability becomes critical:Who should be held accountable when things go wrong?
Scenario-Based Accountability

--- Slide 15 ---

Explanation:
Developer: Poor model design, inadequate testing, or known flaws.
Organization (Hospital/Company): Responsible for deploying and relying on the AI system.
Regulatory Bodies: May share blame if oversight was insufficient.
Vendors/Manufacturers: Liability for faulty hardware/software used in the AI system.
End Users: When human override is possible but neglected.

--- Slide 16 ---

Legal Theories of AI Liability
1. Product Liability
Concept: If an AI system is sold as a product, and it's defective, it can be treated like a faulty product.
Example: A medical device powered by AI gives a wrong dosage recommendation due to a bug.
2. Negligence
Concept: Failure to take reasonable care during AI development or deployment.
Example: Ignoring testing warnings or skipping safety evaluations before launching an AI-powered feature.
3. Strict Liability
Concept: Applies to high-risk AI systems  liability is assigned even if no fault is proven.
Example: An autonomous drone crashes into private property the owner/developer is liable regardless of intent.

--- Slide 17 ---

Accountability Mechanisms in AI Systems
To address and prevent failures, organizations can implement the following:
1. Audit Trails
What: Logging each decision the AI makes and the data it used.
Why: Enables post-incident analysis and compliance checks.
Example: If a patient is denied care, logs can show why the AI decided so.
2. Human-in-the-Loop (HITL)
What: Human oversight on critical decisions (especially life-altering or high-risk ones).
Example: An AI recommends surgery, but the final decision is reviewed by a doctor.
3. Explainability Tools
Tools:
SHAP (SHapley Additive exPlanations) – Shows feature contribution to decisions.
LIME (Local Interpretable Model-agnostic Explanations) – Explains predictions locally.
Why: Helps justify and audit decisions, important for legal defense and public trust.

--- Slide 18 ---

Accountability Mechanisms in AI Systems
As AI becomes more autonomous, shared responsibility between developers, deployers, and regulators becomes essential. Clear documentation, transparent models, and human oversight are key pillars of AI accountability.

--- Slide 19 ---

Key Global AI Regulations
As AI becomes integrated into critical sectors like healthcare, finance, and transportation, governments are establishing regulations to protect citizens' rights, promote fairness, and reduce risks. Below is an overview of major global and industry-specific regulations.

--- Slide 20 ---

Industry-Specific AI Regulations

--- Slide 21 ---

RECAP
Understand AI’s impact on privacy, freedom, and non-discrimination
Learn legal liability models for AI-caused harm
Compare global AI regulations (EU AI Act, GDPR, US proposals)
Analyze real-world AI legal cases (Clearview AI, Tesla Autopilot)
Implement bias detection & compliance strategies
Track emerging AI laws (UN, ISO standards)

--- Slide 22 ---

Resources for Further Study
Further Resources
EU AI Act Documentation
OECD AI Principles
IBM AIF360 Toolkit
SHAP Documentation

--- Slide 23 ---

الشراكات العالمية

--- Slide 24 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 10

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Foundations of AI  Ethics
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Introduce ethical principles and their role in AI and data science. Differentiate between ethical and legal considerations in AI. 
Course Learning Outcomes:
Understand the importance of ethics in responsible AI development.
Identify key ethical challenges, including bias and accountability.

--- Slide 4 ---

Introduction to Ethics in AI
Ethics in AI refers to the principles and guidelines that ensure artificial intelligence systems are developed and used responsibly, fairly, and safely. 

As AI becomes more integrated into various aspects of society, ethical considerations help prevent biases, discrimination, privacy violations, and other unintended consequences.

--- Slide 5 ---

Definition and Importance of Ethics in AI and Data Science
Definition: AI ethics involves moral principles guiding the design, development, and deployment of AI systems to ensure fairness, transparency, accountability, and inclusivity.
Importance:
Prevents biases and discrimination in AI models.
Ensures user privacy and data security.
Promotes transparency and accountability in decision-making.
Builds trust among users, businesses, and governments.
This Photo by Unknown Author is licensed under CC BY

--- Slide 6 ---

Ethical Considerations in AI Development
Ethical Considerations: Moral guidelines that determine what is right or wrong in AI usage, even if there are no laws governing them. 
Examples:
Should AI systems make decisions that impact human lives (e.g., autonomous vehicles, healthcare diagnostics)?
How can we ensure AI respects human dignity and fairness?

--- Slide 7 ---

Legal Considerations in AI Development
Legal Considerations: Regulations and laws that govern AI usage to protect individuals and organizations. Examples:
GDPR (General Data Protection Regulation) for data privacy in AI.
Laws against AI-driven discrimination in hiring or lending.
Compliance with copyright and intellectual property laws in AI-generated content.

--- Slide 8 ---

The Role of Ethics in Responsible AI and Data-Driven Decision-Making
Ethical AI ensures that machine learning models and data-driven decisions align with human values.

Fairness & Bias Reduction: Ensuring AI does not favor one group over another.
Transparency & Explainability: Making AI decisions understandable to users.
Accountability: Holding AI developers and organizations responsible for AI-driven decisions.
Privacy & Security: Protecting user data and ensuring informed consent.

By integrating ethics into AI development, we can create systems that benefit society while minimizing harm and misuse.

--- Slide 9 ---

Moral Responsibility and AI Development
Who is Responsible for AI Decisions? Developers, Organizations, or Users?
AI systems do not operate independently; they are created, trained, and deployed by humans. Therefore, responsibility for AI decisions can be divided among:

Developers:
Responsible for designing ethical algorithms and ensuring data fairness.
Must mitigate biases and ensure transparency in AI models.
Organizations:
Should establish ethical AI policies and governance frameworks.
Need to ensure AI is used responsibly in real-world applications.
Users:
Need awareness of AI limitations and potential biases.
Must use AI responsibly and understand its ethical implications.

Since AI lacks moral reasoning, responsibility ultimately lies with human stakeholders, including policymakers and regulators.

--- Slide 10 ---

The Ethics of AI Autonomy and Decision-Making
AI systems can make decisions without direct human intervention, raising ethical concerns.
Key ethical issues:
Accountability: If an autonomous AI makes a harmful decision (e.g., an accident caused by a self-driving car), who is responsible?
Transparency: Can AI decisions be explained and understood?
Fairness: Does AI treat all individuals equally, without bias?
Control: Should AI have full autonomy in critical areas like criminal justice, hiring, or healthcare?

--- Slide 11 ---

Ethical Considerations in AI for Social Good
AI can be used to solve societal challenges, but ethical issues must be addressed:

Healthcare AI: Improves diagnostics but must ensure patient privacy and avoid bias.
Education AI: Enhances learning but should not reinforce inequalities.
AI in Humanitarian Aid: Helps in disaster response, but must avoid misuse of sensitive data.

--- Slide 12 ---

Case Studies on AI Ethics Violations
AI in Predictive Policing: Racial Bias in Algorithms

Some AI models used for predicting crime (e.g., COMPAS) have been found to unfairly target minority communities.
Bias in training data leads to racial profiling and discrimination.
Ethical concern: Reinforcing systemic biases and unfair law enforcement practices.
(Correctional Offender Management Profiling for Alternative Sanctions) is a risk assessment algorithm used in the U.S. criminal justice system to predict the likelihood of a defendant reoffending (recidivism). It helps judges make decisions on bail, sentencing, and parole.

--- Slide 13 ---

Case Studies on AI Ethics Violations
2. Ethical Concerns in Facial Recognition Technology

Facial recognition systems (e.g., Clearview AI) have been criticized for violating privacy.

Studies show these systems often misidentify minorities at higher rates.

Ethical concern: Mass surveillance, privacy invasion, and racial bias.

--- Slide 14 ---

Case Studies on AI Ethics Violations
3. The Cambridge Analytica Scandal: Data Misuse and Privacy Breaches

In 2018, Cambridge Analytica improperly harvested Facebook user data to influence elections.

It raised concerns about data privacy and manipulation in political campaigns.

Ethical concern: Lack of user consent, exploitation of personal data, and political interference.

--- Slide 15 ---

Case Studies on AI Ethics Violations
4. Bias in Hiring Algorithms: Case Studies from Industry

AI-driven hiring tools (e.g., Amazon’s hiring algorithm) showed bias against women due to past hiring data.

AI learned historical biases and discriminated against female applicants.

Ethical concern: Unfair hiring practices and discrimination.

--- Slide 16 ---

RECAP
Ethics in AI ensures fairness, transparency, and accountability in decision-making.  
AI ethics go beyond legal compliance to address moral responsibilities.  
Developers, organizations, and users share responsibility for AI decisions.  
AI autonomy raises concerns about accountability and unintended biases.  
Ethical AI can drive social good but must avoid discrimination and misuse.  
Case studies highlight issues like bias in predictive policing and hiring algorithms.  
The Cambridge Analytica scandal exposed data misuse and privacy violations.  
Responsible AI development requires transparency, fairness, and ethical guidelines.

--- Slide 17 ---

الشراكات العالمية

--- Slide 18 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 11

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Future Trends and Opportunities in AI GovernanceNavigating Ethics, Regulation, and Innovation
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Define AI governance and explain its necessity
Identify and describe the foundational pillars of AI governance
Compare current global AI governance models and regulatory strategies
Analyze governance challenges and ethical implications in autonomous AI systems
Assess the impact of AI regulation on innovation and societal well-being
Examine real-world case studies to understand governance failures and successes

--- Slide 4 ---

Introduction to AI Governance
What is AI Governance?
AI governance refers to the creation and implementation of policies, laws, frameworks, and best practices that guide the responsible development, deployment, and use of artificial intelligence systems. It aims to ensure that AI technologies are aligned with human rights, ethical norms, and societal values, preventing misuse while enabling innovation.

--- Slide 5 ---

Why AI Governance Matters
AI systems increasingly influence decisions in vital sectors such as healthcare, criminal justice, finance, and education. Without proper governance, these systems can reinforce biases, create unfair outcomes, and cause harm. Governance provides oversight, builds public trust, and ensures AI systems operate transparently and ethically.

--- Slide 6 ---

Pillars of AI Governance
Transparency & Explainability: AI models should provide clear, understandable reasoning for their decisions to ensure accountability and foster user trust.
Fairness & Non-discrimination: Systems should avoid perpetuating societal biases and ensure equal treatment across demographics.
Accountability & Responsibility: Clear attribution of responsibility is crucial when AI causes harm, whether it's the developer, deployer, or data provider.
Privacy & Data Protection: AI systems must comply with data protection laws and respect user privacy through anonymization and informed consent.
Safety & Robustness: AI should function reliably in diverse conditions and be resilient to errors, cyber-attacks, and unexpected inputs.

--- Slide 7 ---

Current Governance Models
Governance models vary globally:

EU AI Act emphasizes a risk-based approach with strict obligations for high-risk systems.

US approach leans toward voluntary guidelines promoting innovation and self-regulation.

China focuses on strong state control and alignment of AI with national goals. 

International frameworks like the OECD AI Principles and UNESCO guidelines aim to provide globally accepted standards.

--- Slide 8 ---

AI Governance in Autonomous Systems
Autonomous systems such as drones, self-driving vehicles, and robotic surgeons challenge conventional governance models. These systems make decisions in real time, often without human intervention. Governance must ensure their decisions are safe, ethical, and legally compliant, even in unpredictable situations.
Challenges with Autonomous Systems:

Decision-making accountability: Determining liability is complex when a machine makes the final decision.

Testing and certification: It’s difficult to simulate every real-world scenario; regulatory bodies struggle to define standards.

Dynamic environments: Systems must adapt to evolving contexts while maintaining safety and compliance with regulations.

--- Slide 9 ---

Real-world Example: Tesla AutopilotTesla’s Autopilot has been involved in several controversial incidents. Investigations revealed overreliance by users, limitations in the technology, and unclear safety communication. This case illustrates the risks of deploying partially autonomous systems without clear governance.

--- Slide 10 ---

Real-world Example: Tesla AutopilotTesla’s Autopilot Controversies: This refers to real-world incidents where Tesla vehicles operating under the Autopilot mode were involved in crashes or near-misses. These events raised public and regulatory concern because they highlighted gaps between what the system can actually do and how users perceive it.User Overreliance: Many drivers treated Autopilot as a fully autonomous system, taking their attention away from the road. However, Tesla’s system is a Level 2 automation (driver-assist), which still requires full driver attention. This mismatch between perception and reality contributed to unsafe situations.Technological Limitations: Despite being advanced, the system has flaws—such as misinterpreting objects, failing to recognize lane changes, or struggling in complex driving environments. These limitations are not always clearly communicated to users.

--- Slide 11 ---

Real-world Example: Tesla AutopilotUnclear Safety Communication: Tesla's marketing, terminology (like "Autopilot" or "Full Self-Driving"), and lack of consistent safety reminders have been criticized for misleading users about the actual capabilities and limits of the system.Governance Implications: This example shows that deploying AI-based systems, especially those affecting public safety, without strict rules, transparent communication, and regulatory oversight can lead to harm. It underscores the importance of comprehensive AI governance in autonomous technologies.

--- Slide 12 ---

The Future of AI Regulation
As artificial intelligence continues to evolve at a rapid pace, traditional regulatory approaches often struggle to keep up that future AI regulation must be agile, adaptive, and supportive of innovation, while also protecting individuals and society.
Adaptive and Flexible Regulation
AI technologies change and improve quickly, so regulations can't be static. Future frameworks need to adapt in real time to new developments, such as generative AI, synthetic media, and autonomous decision-making.
This requires continuous learning by regulatory bodies and frequent updates to laws based on feedback from researchers, developers, and users.
Regulatory Sandboxes
These are controlled environments where AI companies can test new technologies under the supervision of regulators.
Sandboxes allow experimentation with less risk while ensuring basic safety and ethical guidelines are followed. For example, the UK and Singapore have already launched AI sandboxes to support innovation in healthcare and finance.

--- Slide 13 ---

The Future of AI Regulation
4. Risk-Based Approaches
Not all AI systems need the same level of oversight. A risk-based framework evaluates systems based on their potential to cause harm.
For instance, a chatbot used for entertainment is low-risk, while an AI system making medical diagnoses is high-risk and requires more scrutiny.
This approach prevents overregulation, which can stifle innovation, while ensuring safety for high-impact use cases.
5. Balancing Innovation and Safety
The future of regulation must find a middle path: enabling startups and tech companies to develop new AI solutions, while ensuring those solutions are safe, fair, and respect human rights.
This balance can be achieved through mechanisms like pre-deployment impact assessments, post-market monitoring, and collaborative development of AI standards between government, industry, and academia.

--- Slide 14 ---

International Cooperation in AI Governance
Artificial intelligence does not recognize national borders—its development, deployment, and impact are global in nature. For instance, an AI system trained in one country can easily be deployed across the world via cloud platforms or integrated into multinational products and services. This necessitates international cooperation to ensure AI is governed effectively and ethically across jurisdictions.

Global data flows, digital trade, and cybersecurity risks make it essential for countries to establish harmonized rules and interoperable standards. Without alignment, inconsistent regulations may lead to confusion, compliance burdens, or loopholes that allow unethical practices to flourish.

--- Slide 15 ---

International Cooperation in AI Governance contd..
Organizations like the United Nations (UN), Organisation for Economic Co-operation and Development (OECD), and G7 are spearheading efforts to create shared frameworks. For example, the OECD’s AI Principles advocate for inclusive growth, transparency, and human-centered values. These efforts aim to foster trust, accountability, and innovation globally.

However, challenges remain. Different countries have divergent priorities, some emphasize national security, others economic competitiveness, and some focus on protecting civil liberties. Reconciling these differences while ensuring effective oversight and innovation is one of the biggest hurdles in building a truly global AI governance framework.

--- Slide 16 ---

Evolving Standards and Guidelines
Governments and industries are creating dynamic, interoperable standards to regulate AI effectively. Examples include ISO standards for AI, NIST’s risk management framework, and regulatory sandboxes. These help stakeholders test AI systems safely while fostering innovation.

--- Slide 17 ---

Evolving Standards and Guidelines contd..
Dynamic and interoperable standards mean the rules are not only evolving as technology changes (dynamic) but also designed to work across different industries and countries (interoperable), reducing fragmentation in global AI governance.

ISO standards: The International Organization for Standardization (ISO) is developing international AI standards for areas like safety, transparency, and risk management. These standards help companies design AI systems that meet global expectations and build trust with users.

--- Slide 18 ---

Evolving Standards and Guidelines contd..
NIST’s Risk Management Framework: The U.S. National Institute of Standards and Technology (NIST) created a framework that guides organizations in identifying, evaluating, and mitigating risks associated with AI, such as bias, lack of explainability, or misuse.

Regulatory sandboxes: These are safe, controlled environments where companies and regulators collaborate to test new AI systems under regulatory supervision. This allows innovation without the fear of immediate legal penalties, and helps governments understand how to update or create appropriate laws.

In short, these tools and frameworks help balance innovation and safety letting AI grow responsibly without being recklessly unregulated or overly restricted

--- Slide 19 ---

Ethical Frameworks and Global Ethics
Ethical norms vary across cultures, complicating global governance.Different societies have different values-what's considered ethical in one country might not be in another. 

For example, Western nations like those in the EU often prioritize privacy and individual rights, while other regions may emphasize collective benefits or economic development. This diversity makes it hard to create a single global ethical framework for AI.
While the EU prioritizes privacy, other regions focus more on economic growth.

This highlights the trade-off in governance priorities. The EU’s General Data Protection Regulation (GDPR) strictly regulates data usage to protect individuals, whereas countries like China or some in Southeast Asia may adopt a more permissive stance to foster rapid AI innovation and economic competitiveness.

--- Slide 20 ---

Ethical Frameworks and Global Ethics contd..
UNESCO and IEEE are working toward unified ethical principles like accountability, inclusiveness, and human-centric AI.

Despite these differences, international bodies like UNESCO (a UN agency) and the IEEE (a global engineering organization) are trying to build common ground by promoting universal values. 

Their efforts include publishing frameworks that advocate for AI systems that are transparent, inclusive of all populations, and prioritize human well-being over efficiency or profit.

--- Slide 21 ---

AI and Human Rights
AI technologies increasingly influence our fundamental human rights, raising concerns about how these rights are preserved or violated during AI development and deployment. 

For instance, facial recognition tools and predictive policing algorithms can infringe on privacy and freedom of movement. 
Additionally, biased training data may result in discrimination against certain groups in areas like hiring, lending, and law enforcement.

--- Slide 22 ---

AI and Human Rights contd..
Systems used for mass surveillance - like those implemented in authoritarian regimes, may stifle freedom of expression and assembly, chilling political participation. Moreover, AI decisions are often made without human transparency, leaving individuals unable to challenge decisions that affect their lives.

Therefore, AI governance must explicitly align with international human rights frameworks, such as the Universal Declaration of Human Rights and the International Covenant on Civil and Political Rights. Embedding these values ensures technologies serve people equitably and preserve dignity, freedom, and justice in an AI-powered future.

--- Slide 23 ---

Governance’s Dual Impact on Innovation
Good AI governance fosters innovation by building trust, ensuring transparency, and setting clear expectations for developers and companies. 

When rules are well-defined and stable, investors and stakeholders feel more confident putting money and effort into AI projects, knowing there’s a predictable environment. It also encourages developers to create ethically aligned technologies that meet social and legal expectations, which can expand market acceptance and adoption.

However, overly strict or ambiguous regulations can have the opposite effect. If rules are too rigid, unclear, or burdensome, organizations may be discouraged from experimenting or launching new AI technologies due to high compliance costs or fear of legal consequences. This can stifle creativity, delay product releases, and ultimately hinder technological progress, especially in fast-moving sectors.

--- Slide 24 ---

Governance and Societal Well-being
Artificial Intelligence (AI) holds the power to revolutionize critical sectors in society.

 For instance, in personalized healthcare, AI can analyze patient data to offer tailored treatment plans, predict disease outbreaks, or assist in early diagnosis.

 In environmental monitoring, AI can track pollution levels, detect deforestation through satellite imagery, or optimize energy consumption. 

It also aids in disaster prediction, by processing weather patterns and geological data to anticipate events like floods or earthquakes, enabling quicker responses and potentially saving lives.

--- Slide 25 ---

Governance and Societal Well-being & Challenges
AI also brings serious challenges. 

Job displacement is a growing concern as automation replaces human labour in industries like manufacturing, customer service, and logistics.

 Moreover, the rapid deployment of AI technologies can deepen digital inequality, where those with access to AI tools thrive, while underserved populations fall further behind.

To address this duality, AI governance policies must be designed to promote fairness and accessibility. This includes expanding access to AI education, supporting underserved communities, and ensuring AI systems are designed with inclusivity in mind. 

The overarching goal is to guide AI development in a way that delivers positive, widespread societal benefits, rather than exacerbating existing disparities.

--- Slide 26 ---

Case Study 1: EU AI Act
The EU AI Act is a landmark legal proposal classifying AI systems by risk level. High-risk systems must meet stringent transparency, accuracy, and human oversight requirements. This approach balances safety and innovation, serving as a model for other nations.

The EU AI Act introduces a risk-based classification system for AI technologies. This means AI systems are evaluated and categorized based on the potential harm they could cause to people’s safety or fundamental rights. For example, applications in healthcare or law enforcement might be considered high-risk, while entertainment-related AI might fall into a lower-risk category.

--- Slide 27 ---

Case Study 1: EU AI Act contd..
For high-risk systems, the Act imposes strict requirements to ensure trust and accountability. These include:

Transparency: Users must be informed when they are interacting with an AI system.
Accuracy: The system must be thoroughly tested to perform reliably.
Human oversight: There must be provisions to allow humans to monitor and intervene if necessary.

This approach is designed to balance innovation with public safety, allowing Europe to benefit from AI advancements while minimizing potential harm. Because of its structured and comprehensive nature, the EU AI Act is often viewed as a model for other countries exploring how to govern AI effectively.

--- Slide 28 ---

Case Study 2: Clearview AI
Clearview AI collected billions of online photos to power its facial recognition. Privacy watchdogs raised concerns over consent and legality. Several countries banned the app. This case sparked international debates on biometric data governance and ethical boundaries.

It  is a U.S.-based facial recognition company that created a massive database by scraping over 3 billion images from public websites like Facebook, LinkedIn, and Instagram without obtaining user consent. This action raised serious concerns among privacy advocates and regulatory authorities, as it violated data protection and privacy norms in several jurisdictions.

--- Slide 29 ---

Case Study 2: Clearview AI contd..
Governments and watchdog agencies in countries like Canada, Australia, and across the EU challenged the legality of Clearview’s data collection, resulting in fines, regulatory orders, and in some cases, outright bans of the application. 
These controversies sparked global debates about the ethical boundaries of using biometric data, especially in law enforcement. 
The Clearview case has become a landmark example highlighting the urgent need for stricter AI governance, especially for facial recognition and surveillance technologies. 
It underscores how unchecked AI deployment can lead to mass surveillance, loss of individual privacy, and erosion of civil liberties.

--- Slide 30 ---

Case Study 3: OpenAI GPT-4
Large language models like GPT-4 raise concerns over misinformation, copyright infringement, and biased outputs. OpenAI adopted a gradual deployment strategy, incorporating safety research and user feedback. This case illustrates governance in powerful generative AI systems.
Large language models (LLMs) like GPT-4 have the potential to revolutionize various industries, but they also introduce several significant challenges.

Misinformation: LLMs can generate text that appears credible but may contain inaccuracies, misleading information, or outright falsehoods. Since these models are trained on vast amounts of internet data, they may inadvertently propagate harmful content or unverified facts, potentially exacerbating issues related to fake news and disinformation.

Copyright Infringement: LLMs like GPT-4 can generate text based on patterns and data derived from existing works, raising concerns over whether these models are inadvertently replicating or infringing upon copyrighted content. This creates legal and ethical dilemmas regarding ownership and intellectual property rights.

--- Slide 31 ---

Case Study 3: OpenAI GPT-4
3. Biased Outputs: Despite efforts to reduce bias in training data, LLMs still carry the risk of generating biased, discriminatory, or harmful content. This is because they are trained on historical and societal data, which often contains inherent biases. These models may reinforce stereotypes or produce outputs that disproportionately harm certain groups.

OpenAI's Approach: To mitigate these risks, OpenAI adopted a gradual deployment strategy. This means that rather than releasing GPT-4 to the public all at once, the company rolled it out progressively, allowing for ongoing testing, feedback, and safety research. This approach helps ensure that any issues with the model can be addressed before full-scale deployment, incorporating user feedback and conducting additional safety checks.

This case highlights the importance of governance in powerful AI systems like GPT-4. Proper governance frameworks are crucial for overseeing the ethical use of AI, ensuring it operates responsibly, and balancing its vast potential with the need for accountability and fairness.

--- Slide 32 ---

AI Governance: Industry Perspectives
Industry players often push for self-regulation but also invest in internal ethics teams. While some companies actively contribute to policy, others resist external oversight. The balance between corporate autonomy and regulatory enforcement remains a central debate.

The industry's viewpoint is shaped by several factors:

Self-regulation: Many companies in the AI industry advocate for self-regulation rather than strict government-imposed rules. They argue that businesses are better equipped to understand the nuances of AI technologies and that industry-driven guidelines allow for more flexibility and quicker adaptation to technological advancements. This can also foster innovation by reducing bureaucratic delays associated with regulatory bodies.

Internal Ethics Committees: Larger companies often establish internal ethics teams that work to ensure AI systems are being developed and deployed in a manner consistent with ethical principles. These teams are responsible for reviewing AI models, identifying potential risks, and recommending safeguards to prevent harm, bias, or misuse.

--- Slide 33 ---

AI Governance: Industry Perspectives contd..
3. Resistance to External Oversight: While some companies are proactive in promoting ethical AI, others might resist external oversight due to concerns about how regulation could impact profit margins or limit creative freedom. There’s often a fear that government-imposed regulations could slow down innovation, increase compliance costs, or limit the scope of certain AI applications.

4. Balancing Innovation with Regulation: The debate between fostering innovation and ensuring public safety and trust remains central to AI governance. Striking the right balance is crucial for the industry. Without sufficient regulation, there’s a risk of harmful outcomes like algorithmic bias, discrimination, or privacy violations. Conversely, too much regulation could stifle innovation or lead to overly cautious approaches that hinder technological progress.

Ultimately, this slide highlights the complexity of AI governance from the industry’s perspective, where autonomy and innovation are important, but ethical considerations and public accountability cannot be overlooked. The role of governance should allow for innovation while ensuring ethical standards, transparency, and accountability are maintained.

--- Slide 34 ---

The Role of Academia and Civil SocietyAcademics explore algorithmic fairness and bias detection, while civil society groups advocate for rights and transparency. These actors shape public discourse and influence legislation by publishing research, filing lawsuits, and engaging in public awareness campaigns.Here’s a breakdown of their roles:Academia's Role:1. Research & Knowledge Creation: Universities and research institutions play a pivotal role in advancing AI ethics, fairness, and transparency. Scholars conduct studies on algorithmic bias, fairness, and AI's social impact, providing evidence-based frameworks that help shape policy and governance models.

--- Slide 35 ---

The Role of Academia and Civil Society2. Innovation: Academics are at the forefront of developing new AI technologies. Their research often challenges the status quo, proposing new methods for building ethical AI, improving model interpretability, and addressing safety concerns.3. Ethical Training: Academia also trains the next generation of AI professionals, embedding ethical thinking into their training. This ensures that future technologists, engineers, and policymakers understand the social and ethical implications of their work.

--- Slide 36 ---

The Role of Academia and Civil SocietyCivil Society's Role:1. Advocacy & Public Awareness: Civil society organizations, including NGOs, activists, and social movements, advocate for the rights and interests of the public in AI policy discussions. They push for regulations that protect privacy, equality, and human rights.2. Monitoring and Accountability: Civil society organizations often act as watchdogs, holding corporations and governments accountable for how AI systems are deployed and ensuring these systems don’t exacerbate inequalities or violate rights.3. Public Engagement: They engage with the general public, increasing awareness of AI’s potential risks and benefits. Through campaigns, debates, and consultations, civil society ensures that AI governance is inclusive and reflects the diverse needs of society.Together, academia and civil society provide a checks-and-balances system that helps shape AI governance. While academia pushes for ethical frameworks and rigorous research, civil society ensures that AI technologies are aligned with the public good and advocates for the voices of marginalized groups. Their contributions are crucial in creating a balanced, fair, and accountable AI ecosystem.

--- Slide 37 ---

Challenges in AI GovernanceThe major challenges that hinder the effective governance of AI systems. AI governance aims to regulate and control the development and deployment of AI technologies in a way that is ethical, fair, and transparent. However, several complex issues need to be addressed to ensure proper governance:Technical Opacity: Many AI models, particularly deep learning models, are often described as "black boxes." This means their decision-making process is not easily interpretable by humans. It is difficult to understand how these models arrive at their conclusions, which raises concerns about accountability and trust in their outputs. In governance, this opacity creates a problem because regulators and stakeholders may struggle to assess whether AI systems are working ethically, fairly, and in compliance with regulations. Transparent models or the development of techniques for explainable AI (XAI) are essential to overcoming this challenge.Regulatory Lag: AI technology evolves at a rapid pace, often faster than legislative bodies can enact new laws or regulations. This creates a situation where regulations may be outdated or ineffective in addressing current AI developments. For instance, by the time a regulatory body creates guidelines for an emerging technology, that technology may have already surpassed the initial regulatory framework. This lag makes it difficult to establish rules that can keep pace with innovation while maintaining control over the risks posed by AI.

--- Slide 38 ---

Challenges in AI GovernanceCross-border Enforcement: AI technologies and their impact are often global. AI systems can be deployed across multiple countries, but enforcing national laws on AI is difficult when the technology operates across borders. Different countries may have different laws and standards governing AI, and jurisdictional challenges make it hard to hold companies accountable or ensure that AI systems adhere to all applicable rules. This calls for international cooperation and standardized governance frameworks that can address these cross-border challenges and create cohesive, harmonized policies.In Summary:These three challenges-technical opacity, regulatory lag, and cross-border enforcement highlight the difficulties in establishing robust and comprehensive AI governance. Solving these issues requires innovative solutions such as the development of more transparent AI models, faster regulatory adaptation processes, and global collaboration in governance efforts.

--- Slide 39 ---

Opportunities AheadAs AI technologies continue to evolve, new possibilities arise for strengthening governance frameworks. These opportunities focus on collaboration, innovation, and improving the global approach to AI regulation:Global AI Treaties to Harmonize Ethics and Risk Management:As AI technologies are not confined to any one country, international cooperation is essential. The idea behind global AI treaties is to create a unified legal framework across borders, ensuring that AI systems adhere to ethical principles and that risk management approaches are consistent worldwide. These treaties would aim to set common guidelines and standards for AI ethics, privacy, and safety, reducing the risks posed by differences in national regulations. Harmonizing these rules helps create a level playing field for countries and corporations, while promoting responsible AI development globally.

--- Slide 40 ---

Opportunities Ahead contd..Collaborative R&D among Governments, Academia, and Industry:Innovation in AI governance will likely flourish through collaborative research and development. Governments, universities, and private industry can pool their resources and expertise to advance AI regulation. By working together, they can share knowledge, develop new frameworks, and test regulations in real-world scenarios. Such collaboration can lead to the creation of more adaptable, forward-thinking governance models that take into account the latest AI advancements and challenges. This collaborative effort can also help ensure that AI is developed in a way that benefits all sectors of society.

--- Slide 41 ---

Opportunities Ahead contd..Careers in AI Policy:As AI governance continues to evolve, there will be an increasing demand for AI policy professionals. These experts will bridge the gap between the technical world of AI and the legal, ethical, and regulatory frameworks that are needed to manage its impact. AI policy professionals will have the opportunity to shape the future of AI by crafting policies that balance innovation with public safety, fairness, and human rights. This field offers an exciting career path for individuals interested in both technology and governance.In Summary: By pursuing these opportunities, stakeholders can create a more coherent, ethical, and effective AI governance framework that fosters

--- Slide 42 ---

RECAP
Governance is essential for ethical, trustworthy AI.
Future trends include flexible regulation and international cooperation.
Society must balance innovation with public interest. 
Reflection prompt: What would your ideal AI governance framework look like in your country?

--- Slide 43 ---

Resources for Further Study
EU AI Act: europa.eu/ai-act
OECD Principles: oecd.ai
UNESCO AI Ethics: unesco.org
Books: "The Alignment Problem" by Brian Christian, "Atlas of AI" by Kate Crawford
Journals: AI & Society, Journal of AI Research

--- Slide 44 ---

الشراكات العالمية

--- Slide 45 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 12

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Model Transparency and Ethics in Law
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Understand the concept of model transparency and why it is important.Identify different types of interpretable (transparent) models.Recognize the trade-offs between model interpretability and performance.Understand the importance of transparency in AI from an ethical and legal perspective.Identify key legal frameworks governing AI transparency, including GDPR and AI-specific regulations.Discuss the ethical responsibilities of AI developers in ensuring model interpretability.Evaluate real-world case studies where transparency (or lack of it) had ethical and legal consequences.

--- Slide 4 ---

Model Transparency
What is Model Transparency?
Model transparency refers to how easily a human can understand the inner workings of a machine learning model. A transparent model allows users to see how input features influence predictions in a clear and intuitive way.
Why is Model Transparency Important?
In many real-world applications, machine learning models make decisions that significantly impact people’s lives. Consider these examples:
Healthcare: A model predicting disease risk must be interpretable so that doctors can trust and explain its predictions.
Finance: Loan approval systems must be transparent to ensure fairness and avoid discrimination.
Legal Compliance: Regulations like GDPR require that AI decisions be explainable, especially in high-risk scenarios.
Thus, ensuring transparency helps with trust, fairness, debugging, and regulatory compliance.

--- Slide 5 ---

Transparent Models
Some machine learning models are naturally interpretable. These models provide direct insight into how they make predictions and why certain features are important.

A. Decision Trees: A Step-by-Step Breakdown
Decision Trees are one of the most interpretable machine learning models. They work by splitting data based on feature values in a stepwise fashion, forming a tree-like structure.
Advantages:

Easy to visualize and explain.
Captures non-linear relationships.
Limitations:
❌ Can become too complex (deep trees).❌ Prone to overfitting without pruning.

--- Slide 6 ---

Example: A Simple Decision Tree for Loan Approval
Consider a bank deciding whether to approve a loan based on income and credit score.
This tree is easy to understand:
If a person has a credit score > 700 and income > 50k, they get a loan.
Otherwise, they are rejected.

--- Slide 7 ---

Python Implementation: A Simple Decision Tree for Loan Approval
Consider a bank deciding whether to approve a loan based on income and credit score.

--- Slide 8 ---

Linear Regression: A Transparent Model for Continuous Data
Linear Regression is one of the simplest and most interpretable models for predicting a continuous output.

Example: Predicting House PricesSuppose we want to predict the price of a house based on its square footage.
Formula:
Price=β0​+β1​×Square Footage
where:
β0 is the intercept (base price).
β1 is the coefficient (price per square foot).
Interpretation:
1. If the coefficient is 200, it means each additional square foot increases the house price by $200.
2. The model is fully transparent since each input directly affects the prediction.

--- Slide 9 ---

Trade-offs Between Transparency and Performance
While transparent models are interpretable, they may not always perform well in complex tasks.
When to Use Transparent Models?
When interpretability is a priority (e.g., healthcare, finance).
When debugging and explaining predictions is necessary.
When to Use Black-Box Models?
When high accuracy is needed (e.g., image recognition, NLP).
When relationships between features are highly complex.

--- Slide 10 ---

Introduction to AI Transparency in Ethics and Law
What is AI Transparency?
AI transparency refers to the ability to explain how and why an AI system makes decisions. This includes:
Understanding how data is processed
Knowing which features impact decisions
Ensuring stakeholders can interpret and trust the model
Transparency is essential because AI systems increasingly affect human lives in critical areas such as finance, healthcare, criminal justice, and employment.
Why is AI Transparency Important?
Trust and Accountability – Users and stakeholders must trust AI decisions.Fairness and Bias Prevention – Lack of transparency can lead to discriminatory outcomes.Legal Compliance – Regulations require AI to be explainable in high-stakes areas.Security and Safety – Transparency helps detect unintended behavior in AI models.

--- Slide 11 ---

Legal Requirements for Transparency in AI
A. General Data Protection Regulation (GDPR)
The GDPR (enforced in the European Union) is one of the most influential laws regulating AI transparency. It has specific rules that AI systems must follow:
 Right to Explanation (Article 22)
Individuals have the right to receive an explanation of AI-based decisions, especially in automated decision-making (e.g., loan approvals, hiring).
Data Protection (Article 5)
AI must process personal data in a fair, transparent, and accountable manner.
Consent and Data Rights
Users must be informed about how their data is used, and they can request access, corrections, or deletion of their personal information.
 Example of GDPR Violation In 2021, Clearview AI, a facial recognition company, was fined by GDPR regulators for illegally collecting personal images from the internet without consent. This highlighted the importance of data transparency and consent.

--- Slide 12 ---

AI Act (European Union)
The AI Act (expected to be one of the most significant AI laws) classifies AI systems into four risk categories:
Example: High-Risk AIAn AI used in hiring decisions must explain why a candidate was rejected to avoid unfair bias.

--- Slide 13 ---

Other Global AI Regulations

--- Slide 14 ---

Ethical Responsibility in AI Transparency
A. The Ethical Principles of AI Transparency
AI ethics is based on five key principles that guide responsible AI development:

--- Slide 15 ---

B. Ensuring User Understanding of AI Models
For AI to be truly transparent, users must understand how it works. Developers must:
Provide clear explanations – Avoid complex AI jargon and simplify outputs.
Use visualizations – Tools like SHAP, LIME, and ELI5 help explain model decisions.
Educate stakeholders – Training sessions for employees using AI systems.
Allow feedback – AI should adapt based on user concerns and errors.
Example: Transparent AI in HealthcareIBM’s AI model for diagnosing diabetes risk uses SHAP values to show doctors which factors influenced the prediction (e.g., blood sugar, weight).This builds trust and user understanding in AI-powered medical tools.

--- Slide 16 ---

Case Studies: Ethics and Legal Transparency in AI
Case Study 1: Google’s AI Ethics Controversy
 What happened?
In 2020, Google fired two AI ethics researchers (Timnit Gebru & Margaret Mitchell) after they published a paper on bias in AI models.
 Ethical Issues
Lack of transparency in Google's AI research decisions.
Ethical concerns about bias in large AI models (e.g., GPT-3).
Impact
Sparked a global conversation on AI ethics and corporate responsibility.
Many tech companies now have AI ethics committees to ensure transparency.

--- Slide 17 ---

Case Study 2: Facebook’s Algorithm and Misinformation
What happened?
Facebook’s AI prioritized engagement over truth, leading to the spread of misinformation during elections.
 Legal and Ethical Issues
Lack of transparency about how the algorithm promoted fake news.
Ethical failure in prioritizing profits over public safety.
Impact
Increased regulation of AI-powered social media algorithms.
Push for explainable AI models in content moderation.

--- Slide 18 ---

Summary
Transparent models (decision trees, linear regression) are easy to understand but may lack performance.
Black-box models (neural networks, ensembles) perform well but require interpretation tools.
 SHAP, LIME, and ELI5 help explain complex models. AI transparency is both an ethical and legal necessity for fairness, accountability, and trust.
Regulations like GDPR and AI Act ensure AI models are explainable and protect user rights.
Developers must focus on fairness, explainability, and user education to make AI ethical.
Real-world failures (COMPAS bias, Facebook misinformation) highlight the risks of non-transparent AI.

--- Slide 19 ---

Practice with Google COLAB
Click here 
https://colab.research.google.com/drive/1wPguJV1vy_D496JXyEVLOzZCW49OiDhM

--- Slide 20 ---

الشراكات العالمية

--- Slide 21 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 13

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Privacy and Security in Data Science
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

1. Understand the Importance of Data Privacy and Security.
2. Analyze the Role of AI in Enhancing Privacy and Security
3. Understand Legal and Regulatory Compliance

--- Slide 4 ---

Privacy and Security in Data Science:
In today's data-driven world, privacy and security are critical concerns in data science, as organizations collect, store, and analyze vast amounts of personal and sensitive data. Ensuring the protection of this data is essential for compliance, trust, and ethical AI development.

Data Privacy refers to controlling access to personal information and ensuring individuals have rights over their data.
Data Security involves protecting data from unauthorized access, breaches, and cyber threats.

Why is this important?
Prevents data breaches that can lead to financial losses and reputational damage.
Ensures legal compliance with global regulations.
Builds trust with users, customers, and stakeholders.

--- Slide 5 ---

Key Principles of Data Protection: The CIA Triad
The CIA Triad (Confidentiality, Integrity, and Availability) is the foundation of data security.
 Confidentiality – Ensuring that sensitive data is only accessible to authorized users.
Example:
Confidentiality: Encrypting user passwords in a database.

Integrity – Maintaining accuracy and consistency of data, preventing unauthorized modifications.
Example:
Integrity: Using checksums to verify data accuracy during transmission.

Availability – Ensuring data is accessible when needed, without disruption.
Example: 
Availability: Implementing backup solutions to prevent data loss in case of cyberattacks.

--- Slide 6 ---

The Role of AI and Data Science in Securing Personal Data
Data science and AI play a crucial role in protecting privacy through:
Anomaly detection – AI models identify suspicious activities (e.g., fraud detection).Data anonymization – Masking or encrypting personal identifiers in datasets.Access control – Machine learning helps in dynamic user authentication.Automated compliance – AI-powered tools monitor regulatory compliance in real time.

Example: AI in cybersecurity detects phishing attacks by analyzing email content and sender behavior.

--- Slide 7 ---

Privacy Regulations and Legal FrameworksOrganizations must comply with various global privacy laws to avoid legal consequences.General Data Protection Regulation (GDPR)The GDPR is the European Union’s (EU) strictest privacy law, ensuring:User consent before data collection.Right to be forgotten – Users can request data deletion.Data breach notification within 72 hours.Example: If a company tracks website visitors, it must inform users and obtain explicit consent.

--- Slide 8 ---

California Consumer Privacy Act (CCPA)
The CCPA is a U.S. law that grants California residents:

Right to know what data is collected.

Right to opt out of data sales.

Right to delete personal information.

Example: Social media platforms must allow users to opt out of targeted advertising.

--- Slide 9 ---

Data Protection Act and Other International Privacy Laws
Several countries enforce strict data privacy laws, including:

India's Digital Personal Data Protection Act (DPDP)

Brazil's LGPD (Lei Geral de Proteção de Dados)

Canada’s PIPEDA (Personal Information Protection and Electronic Documents Act)

--- Slide 10 ---

Legal Responsibilities of AI Developers and Organizations
AI developers and companies handling personal data must:

Ensure transparency in AI decision-making.Use privacy-enhancing technologies (PETs) like differential privacy.

Conduct regular security audits to detect vulnerabilities.

Example: A healthcare AI system must anonymize patient data before training a model.

--- Slide 11 ---

Threats to Data Privacy and SecurityIn today’s digital era, data privacy and security face numerous challenges due to evolving cyber threats, increasing data collection, and growing reliance on AI-driven technologies. Organizations must understand these threats to implement effective risk mitigation strategies.

--- Slide 12 ---

Data Breaches, Unauthorized Access, and Malicious Attacks
What is a Data Breach?

A data breach occurs when sensitive information is exposed due to cyberattacks, accidental leaks, or internal security failures.
Common causes of data breaches:
Weak passwords – Easy-to-guess passwords can be exploited by hackers.Phishing attacks – Attackers trick users into revealing credentials.Unpatched software vulnerabilities – Hackers exploit outdated systems.Insider threats – Employees or third-party vendors leaking data.

Examples of data breaches:
Facebook (2019): 540 million records of users' data were exposed.
Equifax (2017): 147 million people’s financial data was stolen.

--- Slide 13 ---

Unauthorized Access and Malicious Attacks
Cybercriminals use various techniques to gain unauthorized access to sensitive data:

Types of attacks:Ransomware – Hackers encrypt data and demand payment for its release.DDoS (Distributed Denial-of-Service) attacks – Overloading servers to crash a system.SQL injection – Attackers insert malicious SQL queries to access databases.Man-in-the-middle (MITM) attacks – Hackers intercept communication between two parties.

Example:A ransomware attack on a hospital can encrypt patient records, preventing doctors from accessing critical data.

--- Slide 14 ---

Risks in Cloud Computing
Risks in Cloud Computing
Cloud services store vast amounts of personal and business data, making them prime targets for cyberattacks.

Key threats in cloud computing:
Data leakage – Unauthorized users access stored data.Misconfigured cloud settings – Poor security settings expose sensitive files.Insider threats – Employees or contractors may misuse cloud data.
Lack of encryption – Storing data without proper encryption increases risk.

Example: An improperly secured Amazon S3 bucket can expose millions of user records to public access.

--- Slide 15 ---

Risks in IoT Systems
Risks in IoT (Internet of Things)
IoT devices (smartphones, home assistants, wearables) collect and transmit large amounts of data, making them vulnerable to cyber threats.
IoT security challenges:Weak authentication – Many IoT devices lack strong passwords.Unpatched vulnerabilities – Devices may not receive regular security updates.Data interception – Hackers can eavesdrop on device communications.Botnets – Hackers hijack IoT devices to launch cyberattacks (e.g., Mirai botnet).
Example:A hacked smart security camera can be used to spy on individuals or businesses.

--- Slide 16 ---

Risks in AI Systems
As technology advances, cloud computing, Internet of Things (IoT), and AI introduce new privacy and security challenges.
Risks in Cloud Computing
Cloud services store vast amounts of personal and business data, making them prime targets for cyberattacks.
Key threats in cloud computing:Data leakage – Unauthorized users access stored data.Misconfigured cloud settings – Poor security settings expose sensitive files.Insider threats – Employees or contractors may misuse cloud data.Lack of encryption – Storing data without proper encryption increases risk.
Example:An improperly secured Amazon S3 bucket can expose millions of user records to public access.

--- Slide 17 ---

Privacy Concerns in Sensitive Sectors (Healthcare, Finance, Government)Certain industries handle extremely sensitive data, making them high-risk targets for cyberattacks and privacy violations.
Healthcare
Electronic Health Records (EHRs) contain highly personal patient data.

HIPAA violations can result in fines for mishandling medical data.

Medical IoT devices (e.g., pacemakers, insulin pumps) are vulnerable to hacking.
 Example:A ransomware attack on a hospital disrupts medical services, endangering patients.

--- Slide 18 ---

Privacy Concerns in Sensitive Sectors-Finance
Banks and financial institutions store credit card numbers, SSNs, and transaction data.

Online banking fraud and cryptocurrency hacks are increasing.

Identity theft allows cybercriminals to access financial accounts.

Example:The JP Morgan Chase data breach (2014) exposed 76 million bank accounts.
This Photo by Unknown Author is licensed under CC BY

--- Slide 19 ---

Privacy Concerns in Sensitive Sectors-Government
Governments store classified information on citizens, defense, and infrastructure.

Cyberattacks can disrupt national security and public services.

Surveillance concerns arise from excessive data collection.

Example:The 2020 SolarWinds cyberattack compromised multiple U.S. government agencies.

--- Slide 20 ---

RECAP
Data privacy and security are essential for ethical AI development.
The CIA Triad (Confidentiality, Integrity, Availability) guides data protection strategies.
AI enhances privacy through encryption, authentication, and anomaly detection.
Organizations must comply with GDPR, CCPA, and other regulations to avoid legal risks.
Data breaches and unauthorized access are major threats to data security.
Cloud computing, IoT, and AI introduce new security vulnerabilities.
Healthcare, finance, and government sectors are prime targets for cyberattacks
Strong encryption, authentication, and AI-driven security can help mitigate risks.

--- Slide 21 ---

الشراكات العالمية

--- Slide 22 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 14

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Artificial Intelligence Ethics

--- Slide 2 ---

Discrimination and Ethical Implications in AI
Understanding BIAS and Implications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
To understand the ethical implications of AI in decision-making, particularly in areas like hiring, healthcare, and law enforcement.
To explore regulatory frameworks such as GDPR, AI Act, and ECOA that address AI discrimination and promote fairness.
Course Learning Outcomes:
1.Students will be able to identify and analyze sources of bias in AI systems and their impact on fairness.
2. Students will demonstrate knowledge of legal and ethical frameworks that mitigate AI discrimination and ensure responsible AI development.

--- Slide 4 ---

Understanding Bias in AI
Definition and Types of Bias:Bias in AI refers to systematic errors in machine learning models that lead to unfair outcomes. It can be classified into:
Data Bias: Occurs when training data is unrepresentative or imbalanced (e.g., facial recognition systems failing to recognize certain demographics).
Algorithmic Bias: Results from the way models process data and make decisions, often amplifying existing biases.
Human Bias: Introduced by the developers, researchers, or data annotators through subjective decisions.

--- Slide 5 ---

Sources of Bias in AI Models:
Data Collection: Skewed or non-diverse datasets can lead to biased predictions.

Feature Selection: Choosing inappropriate or sensitive features (e.g., race or gender) can create biased outcomes.

Model Training: Biases in the learning process can reinforce disparities, especially if optimization prioritizes accuracy over fairness.

--- Slide 6 ---

Real-World Examples:
Hiring Algorithms: Some AI-based hiring tools have discriminated against women due to biased training data.

Predictive Policing: AI systems predicting crime hotspots have reinforced racial biases due to historically biased police data.

Loan Approval Systems: AI models have unfairly denied loans to minority groups due to biased credit history data.

--- Slide 7 ---

Fairness in AI Decision-Making
Fairness in AI refers to ensuring equitable outcomes across different groups. Two key perspectives include:

Group Fairness: Ensures that different demographic groups (e.g., gender, race) receive similar treatment.

Individual Fairness: Ensures that similar individuals are treated equally regardless of their group identity.

--- Slide 8 ---

Fairness Criteria:
Demographic Parity: Ensures that the same proportion of each group receives a positive outcome.

Equal Opportunity: Requires that qualified individuals across different groups have the same chance of a positive outcome.

Equalized Odds: Ensures that different groups have similar false positive and false negative rates.

--- Slide 9 ---

Trade-offs Between Accuracy and Fairness:
This Photo by Unknown Author is licensed under CC BY
Increasing fairness might slightly reduce model accuracy since fairness constraints modify predictions.

Balancing accuracy and fairness is crucial in high-stakes applications like healthcare, hiring, and criminal justice.

--- Slide 10 ---

Discriminatory Outcomes in AI
AI systems can unintentionally produce discriminatory outcomes in various domains due to biases in training data, model design, or decision-making processes.

Hiring: AI-driven recruitment tools may favor certain demographics over others, as seen in Amazon’s hiring algorithm, which showed bias against women.

Lending: Credit scoring algorithms may systematically disadvantage minority groups due to biased historical data.

Healthcare: AI models trained on limited demographic data may misdiagnose conditions in underrepresented groups.

Policing: Predictive policing models have been criticized for reinforcing racial bias by over-policing certain communities based on biased historical crime data.

--- Slide 11 ---

Legal and Ethical Frameworks for Preventing AI Discrimination
To mitigate discrimination, governments and organizations have developed ethical and legal frameworks. These frameworks ensure AI systems are transparent, accountable, and fair.
Ethical Guidelines: Encourage fairness, transparency, and accountability in AI decision-making.
Bias Audits: Regularly testing AI models for discriminatory patterns before deployment.

--- Slide 12 ---

Regulatory Guidelines
Several regulations have been introduced to prevent AI-related discrimination:
General Data Protection Regulation (GDPR): Enforces transparency in AI decisions and grants users the right to explanation and data protection.
AI Act (EU): Proposes stricter regulations on high-risk AI applications to prevent bias and discrimination.
Equal Credit Opportunity Act (ECOA - US): Ensures fair lending practices by prohibiting discrimination based on race, gender, or age in credit decisions.
These frameworks help establish fairness, reduce harm, and hold AI developers accountable for ethical AI deployment.

--- Slide 13 ---

RECAP
AI systems can lead to discriminatory outcomes in hiring, lending, healthcare, and policing due to biased training data and flawed algorithms.
Bias in AI can arise from multiple sources, including data collection, feature selection, and model training.
Fairness in AI decision-making is crucial and involves balancing accuracy with ethical considerations.
Legal and ethical frameworks help prevent AI discrimination by promoting transparency and accountability.
Regulatory guidelines like GDPR, AI Act, and ECOA enforce fairness and protect individuals from biased AI-driven decisions.
Bias audits and fairness metrics are essential for evaluating and mitigating discrimination in AI models.
Developers and organizations hold responsibility for ensuring ethical AI deployment and minimizing harmful societal impacts.

--- Slide 14 ---

Check your Knowledge
Click Here

--- Slide 15 ---

الشراكات العالمية

--- Slide 16 ---

شــــــكــــرًا لكــــــم
THANK YOU

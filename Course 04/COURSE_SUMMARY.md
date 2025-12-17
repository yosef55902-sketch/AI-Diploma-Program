# Course 04 - Course Summary
## ملخص الدورة

This document provides a comprehensive text summary of all course materials.
هذا المستند يوفر ملخص نصي شامل لجميع مواد الدورة.

---


## Pdfs


### 01

--- Page 1 ---

© SuperDataScienceMachine Learning A-Z
ClassificationClassification ModelProsConsLogistic RegressionProbabilistic approach, gives informations about statistical significance of featuresThe Logistic Regression AssumptionsK-NNSimple to understand, fast and efficientNeed to choose the number of neighbours kSVMPerformant, not biased by outliers,not sensitive to overfittingNot appropriate for non linear problems, not the best choice for large number of featuresKernel SVMHigh performance on nonlinear problems, not biased by outliers, not sensitive to overfittingNot the best choice for large number of features, more complexNaive BayesEfficient, not biased by outliers, works on nonlinear problems, probabilistic approachBased on the assumption that features have same statistical relevanceDecision Tree ClassificationInterpretability, no need for feature scaling, works on both linear / nonlinear problemsPoor results on too small datasets, overfitting can easily occurRandom Forest ClassificationPowerful and accurate, good performance on many problems, including non linearNo interpretability, overfitting can easily occur, need to choose the number of trees

---


### 02

--- Page 1 ---

Hierarchical
CLustering

--- Page 2 ---

Hierarchical CLustering
Image source: mdpi.com/2073-8994/10/12/73What HC does ?

--- Page 3 ---

Hierarchical CLustering
Image source: mdpi.com/2073-8994/10/12/73Two types of HC:
Agglomerative & Divisive 
Bottom-Up Approach

--- Page 4 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC
STEP 1: Make each data point a single-point cluster -> That forms N clusters
STEP 2: Take the two closest data points and make them one cluster  -> That forms N-1 clusters
STEP 3: Take the two closest clusters and make them one cluster -> That forms N - 2 clusters
  
 STEP 4: Repeat STEP 3 until there is only one cluster

--- Page 5 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC
Euclidean Distance is
basically more natural 
What is actually Distance between clusters  ? shortest ? largest ? average ? or distance between centroids ? 
You need to find that based on business usecase !! choosing distance is important !!

--- Page 6 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 7 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 8 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 9 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 10 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 11 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC

--- Page 12 ---

Hierarchical Clustering
Image source: mdpi.com/2073-8994/10/12/73Agglomerative HC
it maintains like memory of each
steps , saving the steps taken with
the distances.

--- Page 13 ---

Hierarchical Clustering
How Do Dendograms Work ?
once we defied first closest two points and made clusters, we can now assign p2 and p3 with the
distance (Euclidean), and it is the similarity of these clusters

--- Page 14 ---

Hierarchical Clustering
How Do Dendograms Work ?
Next step , the next two closest clusters and plot them as Dendograms  

--- Page 15 ---

Hierarchical Clustering
How Do Dendograms Work ?
Repeat the process until you get one cluster

--- Page 16 ---

Hierarchical Clustering
How Do Dendograms Work ?
Final Dendograms with clusters and distances (Memory on how clusters are formed)

--- Page 17 ---

Hierarchical Clustering
Using Dendograms ?
We can set threshold (distance threshold or dissimilarities) which help in making better clusters by
increasing similarity of these clusters // by vertical lines, we can see how many clusters we have.

--- Page 18 ---

Hierarchical Clustering
Using Dendograms ?
Another threshold 

--- Page 19 ---

Hierarchical Clustering
Using Dendograms ?
Threshold below our first clusters

--- Page 20 ---

Hierarchical Clustering
Using Dendograms | Optimal Number of clusters:
By using vertical distance that n o t cross any horiztional line and should be l o n g e s t line 

--- Page 21 ---

? ? ?Hierarchical Clustering
Dendograms | Knowledge Test

--- Page 22 ---

Hierarchical Clustering
Dendograms | Knowledge Test

--- Page 23 ---

Clustering
Difference Between Clustering Models

--- Page 24 ---

Hands-On Code
Clustering Implementation

---


### 03

--- Page 1 ---

Support Vector
Machine

--- Page 2 ---

Support Vector Machine
What is SVR ? 
The SVM (Support Vector Machines) is a supervised learning model used for classification or
regression analysis. 
In regression problems the SVM is called SVR (Support Vector Regression), and it is used to estimate
the relationships between a dependent variable (often called the outcome variable) and one or more
independent variables (often called predictors, covariates, or features) .
Examples:
Predicting disease progression.
Engineering data (e.g., stress-strain curves).
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 3 ---

Support Vector Machine
What is SVR ? 
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 4 ---

Support Vector Machine
What is SVR ? 
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 5 ---

Support Vector Machine
Support Vector Regression
It finds a separating hyperplane with a margin of ±𝜀, making
it less sensitive to outliers than traditional regression
methods.
Support Vectors:
These are key data points that define the hyperplane's
position and help maximize the margin between boundary
hyperplanes.
Why Use SVR?
Handles non-linear data using the Kernel Trick
Uses quadratic programming to efficiently find solutions
Fewer constraints make it computationally efficient
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRhttps://spotintelligence.com/2024/05/08/support-vector-regression-svr/

--- Page 6 ---

Support Vector Machine
Hyperparameters in SVR
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHyperplane:
Hyperplanes are decision boundaries that is used to predict the continuous output. 
The data points on either side of the hyperplane that are closest to the hyperplane are called
Support Vectors. 
These are used to plot the required line that shows the predicted output of the algorithm.

--- Page 7 ---

Support Vector Machine
Hyperparameters in SVR
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRKernel:
A kernel is a set of mathematical functions that takes data as input and transform it into the required
form. These are generally used for finding a hyperplane in the higher dimensional space.

--- Page 8 ---

Support Vector Machine
Hyperparameters in SVR
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe image compares the decision boundaries of Support Vector Machines (SVM) with different kernels.
SVC with Linear Kernel (Top Left):
Uses a straight-line decision boundary.
Suitable for linearly separable data.
May not perform well with complex data.
LinearSVC (Linear Kernel) (Top Right):
Another implementation of SVM using a linear kernel.
Similar decision boundary to SVC with a linear kernel.
May differ slightly in optimization techniques.

--- Page 9 ---

Support Vector Machine
Hyperparameters in SVR
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe image compares the decision boundaries of Support Vector Machines (SVM) with different kernels.
SVC with RBF Kernel (Bottom Left):
Uses a Radial Basis Function (RBF) kernel to create a nonlinear
decision boundary.
More flexible in handling complex patterns.
Can separate non-linearly distributed data better.
SVC with Polynomial (Degree 3) Kernel (Bottom Right):
Uses a polynomial function to create a nonlinear decision boundary.
Can model more complex relationships than a linear kernel.
May be more sensitive to parameter tuning.

--- Page 10 ---

Support Vector Machine
Hyperparameters in SVR
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRBoundary Lines:
These are the two lines that are drawn around the
hyperplane at a distance of ε (epsilon). 
It is used to create a margin between the data
points.

--- Page 11 ---

Support Vector Machine
Support Vector Regression (SVR) vs. Traditional Regression:
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnlike ordinary regression models that minimize the error between real and predicted values, SVR
fits the best line within a threshold margin (epsilon tube).
Only data points outside the margin contribute to model training, making it robust against
outliers.
The computational complexity of SVR is more than quadratic in the number of samples, making it
inefficient for large datasets.

--- Page 12 ---

Hands-On Code
SVR Implementation

--- Page 13 ---

Decision Tree
Regression

--- Page 14 ---

CART
Classification
TreesRegression
Trees

--- Page 15 ---

Decision Tree Regression
What is Decision Tree Regressors? 
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRDecision Tree Regressors are a powerful,
interpretable, and non-linear method used widely
for regression tasks in machine learning. 
Unlike linear regression, decision trees partition
the feature space in a hierarchical, rule-based way
that enables them to capture complex, non-linear
relationships.
https://farshadabdulazeez.medium.com/understanding-decision-tree-regressor-an-in-depth-intuition-a1d3af182efd

--- Page 16 ---

Decision Tree Regression
Core Concept of Decision Tree Regressor
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRA Decision Tree Regressor is a type of supervised learning algorithm that uses a flowchart-like structure to
predict a continuous target variable based on decision rules inferred from the data features. The model
continuously splits data into subsets, based on the features that result in the lowest prediction error,
forming a tree-like structure where:
Each internal node represents a decision rule on a feature.
Each branch represents the outcome of a decision.
Each leaf node provides the predicted value (usually the average of values in that subset of data).
This structure allows the model to capture non-linear relationships in the data by focusing on minimizing
errors through the splits.

--- Page 17 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 18 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 19 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 20 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 21 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 22 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 23 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 24 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 25 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 26 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 27 ---

Decision Tree Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 28 ---

Decision Tree Regression
How Splitting Happens:
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe most critical step in decision tree regression is determining where to split the data at each node. Here’s how it
works:
a. Mean Squared Error (MSE) as the Splitting Criterion:
To evaluate potential splits, Decision Tree Regressors typically use Mean Squared Error (MSE) as the criterion for
minimizing error. When considering a split at a node, the model aims to reduce the MSE of the target variable,
calculated as:

--- Page 29 ---

Decision Tree Regression
How Splitting Happens:
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRStart at a node with all data points
The tree considers different possible values to split the data into
two parts (left & right).
For each possible split, calculate MSE for both child nodes:
MSE_L → Mean Squared Error for the left child (points below
the split).
MSE_R → Mean Squared Error for the right child (points above
the split).
Compute the weighted average of MSE for both child nodes:
Find the split that minimizes MSE_split
The tree chooses the split where MSE_split is the smallest,
meaning the data is best divided into two groups.NL  = Number of points in the left child.
NR  = Number of points in the right child.
N = Total number of points at the current node.

--- Page 30 ---

Hands-On Code
Decision Tree Implementation

--- Page 31 ---

Random  Forest
Regression

--- Page 32 ---

Random Forest Regression
Algorithm
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRSTEP 1: Pick at random K data points from the Training set. 
STEP 2: Build the Decision Tree associated to these K data points. 
STEP 3: Choose the number N tree of trees you want to build and repeat STEPS 1 & 2 
STEP 4: For a new data point, make each one of your Ntree trees predict the value of Y to for the
data point in question, and assign the new data point the average across all of the predicted Y values

--- Page 33 ---

Feature Decision Tree 🌳 Random Forest 🌲🌲🌲
DefinitionA single tree that splits data using MSE
(for regression).An ensemble of multiple Decision Trees
that work together.
How it WorksFinds the best splits in data to minimize
MSE.Picks random subsets of data and builds
multiple trees, then averages their
predictions.
Overfitting Risk High risk ⚠  (memorizes data).Low risk ✅  (averages multiple models for
better generalization).
Accuracy & StabilityLess stable, small changes in data can
change the tree.More stable & accurate, reduces variance
by averaging predictions.
Final Prediction The output of one tree.The average of multiple tree outputs (for
regression).Random Forest Regression
Random Forest Regression Vs. Decision Tree
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 34 ---

Hands-On Code
Random Forest Implemenration

---


### 04

--- Page 1 ---

Evaluation Regression Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVR

--- Page 2 ---

Regularization
Methods

--- Page 3 ---

Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRA  curve perfectly fitting all data points 
The model captures noise instead of the real
pattern.
Key Points:
Overfitting: The model is too complex, learning
noise instead of trends.
Effects: High training accuracy but poor test
performance.
Indicators: High variance, unstable predictions,
poor generalization.The Problem of Overfitting

--- Page 4 ---

Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRSmall changes in input lead to big prediction shifts.The Problem of Overfitting

--- Page 5 ---

Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRExamples of Regularization
Regularization is a technique in regression that adds a penalty to the model to prevent overfitting and improve generalization.

--- Page 6 ---

Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWithout Regularization
This is the standard Mean Squared Error (MSE)
minimization in linear regression.
The model aims to minimize the sum of squared
differences between actual values yi and predicted
values.
Key Points:
No Penalty on Coefficients: The model freely adjusts
parameters b0 ,b1 ,...bm .
Risk of Overfitting: If there are too many features, the
model may fit noise instead of patterns.

--- Page 7 ---

Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRRidge Regression
Ridge regression adds a penalty ( λ  * sum of squared coefficients) to the
standard loss function.
This penalty shrinks coefficients but does not force them to zero.
Key Points:
Controls Overfitting by reducing coefficient magnitudes.
Smooths model predictions and improves generalization.
λ (lambda) controls regularization strength – higher λ  shrinks coefficients more.

--- Page 8 ---

Lasso adds a penalty on the absolute values of coefficients 
(∣b1 ∣ + ∣ b2 ∣ +...+ ∣ bm ∣ ).
Encourages sparsity by forcing some coefficients to exactly zero.
Key Points:
Feature Selection: Automatically removes less important features.
Sparse Models: Useful when only a few features matter.
λ (lambda) controls regularization strength – higher λ  forces more coefficients to zero.
Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRLasso Regression

--- Page 9 ---

Elastic Net combines Lasso (L1) and Ridge (L2) penalties.
The penalty includes both absolute values and squared values of coefficients.
Key Points:
Best of Both Worlds: Shrinks coefficients like Ridge and performs feature selection like
Lasso.
Useful when features are correlated: Lasso alone may arbitrarily drop one feature, but
Elastic Net keeps important ones.
Two Hyperparameters ( λ ₁, λ ₂): Control the balance between L1 and L2 regularization.
Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRElastic Net

--- Page 10 ---

Regularization prevents overfitting by
simplifying the model.
Better generalization: The model performs
well on both training and new data.
Less variance: Predictions are more stable and
robust.
Regularization Methods
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRAs a Result,

---


### 05

--- Page 1 ---

Naive Bayes

--- Page 2 ---

P(A∣ B) → Probability of A happe ning given B is true.
P(B∣ A) → Probability of B happe ning given A is true.
P(A) → Prior probability of A happening.
P(B) → Total probability of B happening.
Example: Diagnosing a Disease:
P(Disease ∣ Symptom) → Probabi lity of having a disease given the symptom.
P(Symptom ∣ Disease) → Probabi lity of the symptom if the person has the disease.
Why is Bayes' Theorem Important?
Updates beliefs as new evidence comes in.
Forms the foundation of Naïve Bayes Classifier for making predictions.
Used in spam filtering, medical diagnosis, and machine learning.Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhat Is Bayes Therom About?

--- Page 3 ---

When a  new data point is introduced, we need to classify whether this new individual is more likely to walk
or drive based on given data.
Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ?

--- Page 4 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRStep #1
The probability of a person walking given their data point P(Walks|X) is computed using
Bayes' Theorem.Prior Probability P(Walks): Initial belief about the probability of walking.
Marginal Likelihood P(X): The overall probability of observing a data point like X.
Likelihood P(X ∣ Walks): The probability of observing XX given that the person walks.
Posterior Probability P(Walks ∣ X): The final probability that the person belongs to the "Walks" category.

--- Page 5 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRStep #2
Similarly, the probability of a person driving given their data point P(Drives|X) is
computed using the same formula.

--- Page 6 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRStep #3
The classification decision is made by comparing P(Walks ∣ X) vs. P(Drives ∣ X).
The category with the higher probability is chosen.

--- Page 7 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action >> Step #1

--- Page 8 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action >> Step #1

--- Page 9 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action >> Step #1

--- Page 10 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action >> Step #1

--- Page 11 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action >> Step #1

--- Page 12 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action  >> Step #2

--- Page 13 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRNaive bayes | In Action  >> Step #2

--- Page 14 ---

Naive Bayes
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhy is it called "Naive"?
Because it assumes independence between features, meaning each feature
contributes to the classification independently.
Why Can We Ignore P(X)?
Since P(X) is the same for all classes, it cancels out when comparing probabilities.
More than Two Classes?
The method extends to multiple classes by computing the probability for each
and picking the highest.

--- Page 15 ---

QUIZ
Naive Bayes

--- Page 16 ---

Hands-On Code
Naive Bayes

--- Page 17 ---

Decision Tree
Classification

--- Page 18 ---

Decision Tree Classification
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCART

--- Page 19 ---

Decision Tree Classification
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRDifference Between Decision Tree Regression and Classification:
Decision Tree Regression: Predicts a continuous numerical value based on input features.
The tree is built using splits that minimize variance within groups.
Decision Tree Classification: Assigns an input to a specific category (class) by recursively
splitting the data based on features that best separate different classes.

--- Page 20 ---

Decision Tree Classification
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRExplanation of Decision Tree Classification:
The images illustrate how a decision tree classifier
works by recursively splitting the data into smaller
regions.
Each split is made based on a feature that best
separates the classes (red and green points).
The first split (Split 1) separates based on X₂ > 60,
dividing the data into two main groups.
The second split (Split 2) further divides one of these
groups based on X₁ < 50.
Additional splits (Split 3, Split 4) continue until pure
or nearly pure regions are formed.

--- Page 21 ---

The tree chooses splits based on feature values that maximize class
separation. This is done using:
Gini Impurity (default in CART trees):
Measures how mixed a group is.
A lower Gini value means a purer split.
Entropy & Information Gain 
Entropy measures uncertainty in data:
Information Gain calculates how much uncertainty is reduced by a split:
The split that maximizes Information Gain is chosen.
Decision Tree Classification
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRExplanation of Decision Tree Classification:

--- Page 22 ---

Hands-On Code
Decision Tree Classification

--- Page 23 ---

Random  Forest
Classification

--- Page 24 ---

STEP 1: Pick at random K data points from the Training set.
STEP 2: Build the Decision Tree associated to these K data points.
STEP 3: Choose the number Ntree of trees you want to build and repeat STEPS 1 & 2
STEP 4: For a new data point, make each one of your Ntree trees predict the category to
which the data points belongs, and assign the new data point to the category that wins
the majority vote.Random Forest Classification
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does Random Forest do Classification?
Ensemble Learning 

--- Page 25 ---

Hands-On Code
Random Forest Classification

---


### 06

--- Page 1 ---

Principal Component
Analysis
PCA

--- Page 2 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73PCA - USE CASES
A powerful dimensionality reduction
technique in machine learning
Key Points:
PCA is an unsupervised learning algorithm
Used for dimensionality reduction, feature extraction,
visualization, and noise filtering
Common applications: Stock market prediction, gene analysis,
image processing
The original 3-dimensional data set. The red, blue, green arrows are the direction of the first,
second, and third principal components, respectively. 

--- Page 3 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73PCA - USE CASES
The original 3-dimensional data set. The red, blue, green arrows are the direction of the first,
second, and third principal components, respectively. Scatterplot after PCA reduced from 3-dimensions to 2-dimensions. 

--- Page 4 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73PCA - USE CASES
PCA is extremely useful when working with data sets that have a lot of features. 
Common applications such as image processing, genome research always have to deal with
thousands-, if not tens of thousands of columns.
Sometimes, less is more.More Data So much information Long Model TrainingCurse of
DimensionalityProblem

--- Page 5 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73Sim ply,
Finding the time to read a 1000-pages book is a luxury that few can afford. 
Wouldn’t it be nice if we can summarize the most important points in just 2 or 3 pages so
that the information is easily received even by the busiest person?
 We may lose some information in the process, but hey, at least we get the big picture.

--- Page 6 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73How does PCA work?
It’s a two-step process. We can’t write a book summary if we haven’t read or understood
the content of the book.
PCA works the same way – understand, then summarize.

--- Page 7 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Understanding data: The PCA Way
Human understands the meaning of a storybook through the use of expressive language.
Unfortunately, PCA doesn’t speak English. It has to find meaning within our data through its
preferred language, mathematics.
Can PCA understand which part of our data is important?
Can we mathematically quantify the amount of information embedded within the data?
Well, variance can.
The greater the variance, the more the information. Vice versa.

--- Page 8 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73So, where does this association comes from?
Our friends would cover their faces and we need to guess who’s who based solely on their height. 
Without a doubt, I am going to say that Person A is
Chris, Person B is Alex, and Person C is Ben.Can you guess who’s who? It’s tough when they are
very similar in height.
In the same way, when our data has a higher variance, it holds more information. This is why we keep hearing P C A and maximum
variance in the same sentence.

--- Page 9 ---

PCA is defined as an orthogonal linear transformation that transforms the data to a new
coordinate system such that the greatest variance by some scalar projection of the data
comes to lie on the first coordinate (called the first principal component), the second greatest
variance on the second coordinate, and so on.Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Therefore,

--- Page 10 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Summarizing data with PCA
In this case, it’s very difficult to choose the variables we want to delete. If I throw away either one of the variables, we are throwing
away half of the information.All the features are standardized to the same scale for a fair comparison. 

--- Page 11 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Can we keep both? -Perhaps, with a different perspective.
Instead of limiting ourselves to choose just one or the other, why not combine them? 
When we look closer at our data,
the maximum amount of variance
lies not in the x-axis, not in the y-
axis, but a diagonal line across. 
The second-largest variance
would be a line 90 degrees
that cuts through the first.
The dotted line shows the direction of maximum variance.

--- Page 12 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Can we keep both? -Perhaps, with a different perspective.
To represent these 2 lines, PCA combines both height and weight to create two brand new variables. 
It could be 30% height and 70% weight, or 87.2% height and 13.8% weight, or any other combinations depending on the data that
we have.
These two new variables are called the first principal component (PC1) and the second principal component (PC2). Rather than
using height and weight on the two axes, we can use PC1 and PC2 respectively.
(Left) The red and green arrows are the principal axes in the original data. Image by the author. | (Right) The direction of the principal axes have been rotated to become the new x- and y-axis. 

--- Page 13 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73let’s take a look at the variances again.
(Left) The variance of height and weight are similar in the original data. Image by the author. | (Right) After PCA transformation, all of the variances are shown in the PC1 axis. 
All the variables are standardized to the same scale for a fair comparison.PC1 alone can capture the total variance of
Height and Weight combined. 
Since PC1 has all the information – we can be very
comfortable in removing PC2 and know that our
new data is still representative of the original
data.

--- Page 14 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73let’s take a look at the variances again.
When it comes to real data, more often than not, we won’t
get a principal component that captures 100% of the
variances. 
Performing a PCA will give us N number of principal
components, where N is equal to the dimensionality of
our original data. 
From this list of principal components, we generally
choose the least number of principal components that
would explain the most amount of our original data.
The bar chart tells us the proportion of variance explained
by each of the principal components. 
On the other hand, the  line chart gives us the cumulative
sum of explained variance up until N-th principal
component. Ideally, we want to get at least 90% variance
with just 2- to 3-components so that enough information
is retained while we can still visualize our data on a chart.Looking at the chart, I would feel comfortable using 2 principal
components.

--- Page 15 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73The PC That Got Away
Since we’re n o t choosing all the principal components, we inevitably l o s e
some information. But we haven’t exactly described what we are losing. 
If we feed our data through the PCA model, it would start by drawing the
First Principal Component followed by the Second Principal Component. 
When we transform our original data from 2-dimensions to 2-
dimensions, everything stays the same except the orientation. 
We just rotated our data so that the maximum variance is in PC1.
Nothing new here.

--- Page 16 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73The PC That Got Away
However, suppose that we have decided to keep only the First
Principal Component, we would have to project all our data points
onto the First Principal Component because we no longer have the
y-axis.
What we would lose is the distance in the Second Principal
Component, highlighted with the red color line below.

--- Page 17 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73The PC That Got Away
This has implications on the perceived distance of each data point.
If we look at the Euclidean distance between two specific points
(a.k.a pairwise distance), you will notice that some points are much
farther in the original data than in the transformed data.
The PCA is a linear transformation so in and of itself does not alter
distances, but when we start removing dimensions, the distances
get distorted.
It gets trickier— not all pairwise distance gets affected equally.
If we take the two furthest points, you will see that they are almost
parallel to the principal axes. Although their Euclidean distance is
still distorted, it is to a much lesser degree.

--- Page 18 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73The PC That Got Away
The reason is that principal component axes are drawn in the
direction where we have the largest variance. 
By definition, variance increases when the data points are further
apart. So naturally, the points furthest apart would align
themselves better with the principal axes.
To sum it all up, reducing dimensions with PCA changes the
distances of our data. 
It does so in a way that preserves large pairwise distance better
than small pairwise distance.
This is one of the few drawbacks of reducing dimensions with PCA
and we need to be aware of that, especially when working with
Euclidean distance-based algorithm.

--- Page 19 ---

Principal Component Analysis
Image source: mdpi.com/2073-8994/10/12/73Steps in PCA Algorithm
Standardize the data (Mean = 0, Variance = 1)
Compute eigenvectors & eigenvalues from the covariance matrix
Eigenvectors represent the directions (axes) of maximum variance.
Eigenvalues tell us the magnitude of variance in those directions.
Sort eigenvalues in descending order to determine importance
Construct projection matrix (W) from selected K eigenvectors
Transform original dataset into a new feature space

--- Page 20 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73PCA vs. Linear Regression
PCA is NOT the same as linear regression
Linear Regression: Predicts Y values from X values
PCA: Finds principal axes that best describe the data (not predicting values)

--- Page 21 ---

Principal Com ponent Analysis
Image source: mdpi.com/2073-8994/10/12/73W eakness of PCA
Sensitive to Outliers
Large deviations can skew principal components
Preprocessing techniques like removing outliers or scaling data help improve performance

--- Page 22 ---

Hands-On Code
PCA Implementation

---


### 07

--- Page 1 ---

Logistic
Regression

--- Page 2 ---

Logistic regression is defined as a supervised machine learning algorithm that accomplishes binary
classification tasks by predicting the probability of an outcome, event, or observation. 
The model delivers a binary or discrete outcome limited to two possible outcomes: yes/no, 0/1, or
true/false.
Logical regression analyzes the relationship between one or more independent variables and
classifies data into discrete classes. 
It is extensively used in predictive modeling, where the model estimates the mathematical
probability of whether an instance belongs to a specific category or not.Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRDefinition

--- Page 3 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression

--- Page 4 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression
Linear Regression Fails for Classification – It
predicts continuous values instead of clear 0
or 1 labels.
Invalid Probability Outputs – Predictions can
go below 0 or above 1, which makes no sense
for binary outcomes.
No Clear Decision Boundary – It lacks a
proper mechanism to classify points, unlike
logistic regression, which uses a sigmoid
function.

--- Page 5 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression
Makes Sense – Some points in the middle could
lean toward 0 or 1 but aren't strictly one or the
other.
Those in-between cases should have a probability,
not a fixed value.Doesn’t Make Sense – Probabilities must stay
between 0 and 1.
Invalid Outputs – Values above 1 should be 1, and
below 0 should be 0.So we kind of saying this modeling works 

--- Page 6 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression
s l o p e
best fitting line

--- Page 7 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression
This could represent probabilities since it is
between 0 and 1 
Projecting blue values to each probabilities based
on the training data 
The line represents the logistic regression fitting
line ( slope)

--- Page 8 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRUnderstanding Logistic Regression
Threshold at 0.5 – Anything below 0.5 is predicted
as 0, and anything above is 1.
Mismatch with Data – Predictions fall on 0 and 1,
but not exactly where the data points are.
Loss Optimization – The model tries to find the
best-fitting line with minimal loss.

--- Page 9 ---

Variance Inflation Factor
(VIF), which determines
the correlation strength
between the
independent variables in
a regression model.Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRKey Assumptions For Applying Logistic Reg.
Log odds express probabilities in terms
of the ratio of success to failure, while
probability measures success out of
total events. For example, if you win 5
out of 12 tennis games, your probability
of winning is 5/12, but your odds of
winning are 5 to 7 (wins to losses).
Observations should be
independent, meaning they
shouldn’t be influenced by or
repeated from other observations
in the dataset.

--- Page 10 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRLog Odds in Logistic Regression
Odds represent the ratio of success to failure. It is calculated as:
where:
p is the probability of success (event happening).
1−p is the probability of failure (event not happening).

--- Page 11 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMaximum Likelihood
Logistic regression calculates likelihood by assigning probabilities
to observations and maximizing the likelihood of correct
classification.
The logistic curve (yellow) aligns well with the actual data points.
Each observation has an assigned probability based on the curve.
Since the probabilities for correct classifications are higher, the
overall likelihood is higher.
With  (Lower Likelihood Model)
The logistic curve does not fit the data as well.
Incorrect probabilities are assigned to observations, resulting in a lower likelihood value.
The likelihood is much smaller (0.00019939) compared to the left model.

--- Page 12 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMaximum Likelihood
The process of optimizing the logistic regression model to
find the best-fit curve.
Different logistic curves are tested, each corresponding to a
different likelihood value.
The goal is to find the curve with the highest likelihood.
The highlighted likelihood 0.00019939 represents the best
model, meaning this curve best separates the data into
"YES" and "NO" categories.
Maximum Likelihood Estimation (MLE) selects the best
logistic regression model by finding the curve that
maximizes the likelihood of correct classification.

--- Page 13 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRLogistic Regression: Strengths and Limitations
Strength: Interpretability:
Logistic regression is easy to understand because its coefficients directly show how each feature affects the log odds of
the outcome.
Each coefficient represents the change in log odds for a one-unit change in the feature.
This makes it useful for domains like healthcare, finance, and social sciences, where explainability is crucial.
In a model predicting heart disease risk:
A coefficient of +0.5 for cholesterol level means higher cholesterol increases the odds of heart disease.
A coefficient of -0.3 for exercise frequency means more exercise decreases the odds.

--- Page 14 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRLogistic Regression: Strengths and Limitations
Limitation: Struggles with Non-Linear Relationships
Logistic regression assumes a linear relationship between features and log odds, which means it can't easily capture
complex patterns in the data
If the relationship between input variables and the outcome is non-linear, logistic regression won't perform well.
------
Logistic regression performs poorly when classes are overlapping or not easily separable.
If the data points of two classes mix heavily, logistic regression struggles to find a clear decision boundary.

--- Page 15 ---

Logistic Regression
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHandling Multiple Categories in Logistic Regression
Logistic regression is primarily designed for binary classification (0 or 1). However, when dealing with multiple
classes(e.g., classifying emails as Primary, Social, or Promotions), we need extensions of logistic regression. 
There are two main approaches:
Multinomial Logistic Regression (Softmax Regression)
This method directly extends logistic regression to multiple classes.
Instead of using a single sigmoid function, it uses the softmax function to calculate the probability of each class.
The model predicts one class out of many based on the highest probability.
One-vs-All (OvA) Approach
Instead of using a single model, OvA trains multiple binary logistic regression models.
Each model separates one class from the rest.
The final prediction is made by choosing the model with the highest probability.

--- Page 16 ---

Hands-On Code
Logistic Regression
Implementation

--- Page 17 ---

K-Nearest
Neighbors (K-NN)

--- Page 18 ---

K-Nearest Neighbors (K-NN) is a non-parametric, instance-based learning algorithm used for
classification. It’s simple, intuitive, and often works surprisingly well for many datasets.K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRDefinition

--- Page 19 ---

K-NN makes predictions based on similarity. Instead of learning explicit patterns from the training
data, it stores all the training data and makes decisions based on the most similar examples when a
new data point arrives.
🔹 Steps for Classification:
Choose a value for K (the number of neighbors to consider). 1.
Calculate the distance between the new data point and all existing data points. 2.
Select the K closest points based on the chosen distance metric. 3.
Assign the most common class (majority vote) among these K neighbors to the new data point. 4.K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ! 

--- Page 20 ---

K-NN makes predictions based on similarity. Instead of learning explicit patterns from the training
data, it stores all the training data and makes decisions based on the most similar examples when a
new data point arrives.
🔹 Steps for Classification:
Choose a value for K (the number of neighbors to consider). 1.
Calculate the distance between the new data point and all existing data points. 2.
Select the K closest points based on the chosen distance metric. 3.
Assign the most common class (majority vote) among these K neighbors to the new data point. 4.K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ! 

--- Page 21 ---

Choosing the Value of K:
Small K (e.g., 1 or 3):
More sensitive to noise.
High variance, meaning it can change significantly
with small dataset variations.
Large K (e.g., 10 or 20):
More generalized but may ignore local patterns.
Reduces overfitting but can smooth out important
details.
A common approach is to try different K values and use
cross-validation to find the best one.
K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ! 

--- Page 22 ---

Since K-NN finds the "nearest" neighbors, we need a way to measure distance. 
🔹 Euclidean Distance (Most Common)
Used for continuous numerical data.
🔹 Manhattan Distance
Used when movement is restricted to horizontal and vertical paths.
🔹 Hamming Distance
Used for categorical data (e.g., DNA sequences or text classification).
Choosing the right distance metric depends on the type of data.
K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ! 

--- Page 23 ---

3. Find the Nearest Neighbors (K Closest Points):
We are using K = 5 (since we see 5 nearest neighbors
considered).
The algorithm selects the 5 closest points to the new data
point.
Majority Voting (Classification Decision):
Among the 5 neighbors:
3 belong to Category 1 (red crosses).
2 belong to Category 2 (green plus signs).
Since Category 1 has the majority (3 out of 5), the new data
point is classified as Category 1 (red cross).K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does it work ! 

--- Page 24 ---

Simple & Easy to Understand – No training phase, just storing data and comparing distances.
Works Well with Small Data – Effective for datasets with clear separation.
Non-Parametric – Makes no assumptions about the data distribution.
Can Handle Multi-Class Problems – Works for problems with multiple categories.K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRStrengths of K-NN

--- Page 25 ---

Computationally Expensive for Large Datasets
Since K-NN stores all data, it can become slow for large datasets.
Requires calculating distances for all points at prediction time.
Sensitive to Irrelevant Features
If some features are not useful, they can mislead K-NN.
Feature selection and normalization (scaling data properly) are important.
 Struggles with Imbalanced Data
If one class is much larger than another, K-NN may always favor the majority class.
Not Good for High-Dimensional Data
In high-dimensional spaces, all points start looking equally distant (Curse of
Dimensionality).K-Nearest Neighbors (K-NN)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRLimitations of K-NN

--- Page 26 ---

Hands-On Code
K-Nearest Neighbors

---


### 08

--- Page 1 ---

Support Vector
Machine (SVM)

--- Page 2 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRAgain , How to separate these points? 

--- Page 3 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does SVM Work ? 
Finding the Best Decision Boundary (Hyperplane)
The black line represents the optimal hyperplane, which separates the
two categories (red crosses and green pluses).
SVM selects this hyperplane to maximize the distance between the
closest points from each class.
Support Vectors (Critical Boundary Points)
The circled points (one from each class) are called support vectors.
These are the closest points to the decision boundary and directly
influence its position.
Other points do not matter in defining the boundary; only support
vectors affect it.
Maximizing the Margin
The blue lines represent the margin boundaries, showing the maximum
distance the decision boundary can maintain from both classes
The wider the margin, the better the model generalizes to new data

--- Page 4 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does SVM Work ? 
Hard vs. Soft Margin
If all points can be separated perfectly, it's a hard margin SVM (strict rule).
If some misclassification is allowed (overlapping points), it's a soft margin SVM (allows flexibility).
How Classification Works:
New data points are classified based on which side of the hyperplane they fall on.
If a point falls left of the black line, it is classified as Category 1 (red cross).
If a point falls right of the black line, it is classified as Category 2 (green plus).

--- Page 5 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow does SVM Work ? 
Margin:
The distance between the hyperplane and the
nearest support vectors.
SVM tries to maximize this margin, ensuring
better generalization.
Support Vector:
These are the data points
closest to the hyperplane.
They play a critical role in
defining the boundary.

--- Page 6 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhat Is So Special About SVMs? 
Finds the Optimal Decision Boundary:
Unlike other classification models that just find any separating boundary, SVM finds the best one.
It maximizes the margin (distance) between the closest data points (support vectors) from each class.
A larger margin means better generalization to new data.
 Why is this important?
It makes SVM more robust to small changes in data.
Other models, like logistic regression, may find multiple boundaries, but SVM ensures the best possible separation.

--- Page 7 ---

Handles Non-Linearly Separable Data with the Kernel
Trick:
If the data is not linearly separable, SVM applies the
Kernel Trick to map it into a higher-dimensional
spacewhere separation is possible.
This makes SVM highly flexible and capable of solving
complex classification problems.
Example:
Suppose we have data forming a circular pattern that
cannot be separated with a straight line.
Using the Radial Basis Function (RBF) Kernel, SVM
maps the data to a higher dimension where a clear
linear boundary exists.
Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhat Is So Special About SVMs? 

--- Page 8 ---

Works Well in High-Dimensional Spaces
SVM performs exceptionally well when data has
many features (high-dimensional data).
Many machine learning models struggle with high-
dimensional spaces, but SVM remains effective by
finding a clear hyperplane.
Examples: 
Text classification (Spam vs. Non-Spam), where
each word is a feature.
Image recognition, where each pixel can be a
feature.Support Vector Machine (SVM)
What Is So Special About SVMs? 

--- Page 9 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhen To Use / When NOT ? 
✅ When Should You Use SVM?
When data is high-dimensional (e.g., text, images).
When classes are well-separated.
When the dataset is small to medium-sized.
When you need a robust model against outliers.
When a non-linear decision boundary is required (using kernels).
🚀 When NOT to use SVM?
When the dataset is huge, as SVM can be slow.
When there is too much noise, as SVM might struggle to find a clear boundary.
When the number of features is too large, leading to longer training times.

--- Page 10 ---

Feature SVM Logistic Regression K-NN
Type Classification/regression Classification Classification
Best forComplex, high-dimensional
dataSimple, linearly separable
dataSmall datasets, intuitive
classification
Computational CostHigh (especially for large
datasets)Low High (for large datasets)
Handles Non-Linearity? Yes, with kernel trick No Yes (implicitly)Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRComparison With Other Models

--- Page 11 ---

Support Vector Machine (SVM)
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRBUT WAIT !! 
Mapping to a Higher Dimensional Space can be highly compute-intensive
As the number of dimensions increases, the computational complexity grows exponentially.
If a dataset has 10 features, mapping it to a quadratic kernel results in (10² = 100 dimensions).
If mapped to a cubic kernel, it results in (10³ = 1,000 dimensions).
The Kernel Trick involves computing a Gram matrix (Kernel matrix) that stores the similarity
between every pair of data points.
This requires computing a dot product for every pair, leading to a complexity of O(n²) or worse.
For 1,000 data points, an RBF kernel requires computing a 1,000 × 1,000 matrix.
SVM’s optimization problem (finding the optimal hyperplane) depends on solving quadratic
programming problems.

--- Page 12 ---

Hands-On Code
Support Vector Machine 

--- Page 13 ---

KERNAL
SVM

--- Page 14 ---

The Gaussian RBF Kernel transforms data into a higher-dimensional space to make it linearly
separable.
x → A data point
li → A landmark (reference point in the dataset)
σ (sigma) → A parameter controlling the width of the transformation
If x is close to li →K(x,li) is close to 1 (high similarity).
If x is far from li → K(x,li) is close to 0 (low similarity).KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe Gaussian RBF Kernel Formula

--- Page 15 ---

The kernel function maps data points into a
higher-dimensional space.
The 3D plot shows a Gaussian bump centered
at a landmark point.
Higher values (closer to 1) mean high similarity
to the landmark. 
Lower values (closer to 0) mean low similarity.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe Gaussian RBF Kernel Formula

--- Page 16 ---

The original dataset (left) is in a 2D space, where two
classes overlap.
The Gaussian RBF Kernel transforms the data into a higher-
dimensional space, where:
Points near the landmark (center green area) have high
values.
Points farther away (red points) have lower values.
Effect of the Transformation:
The decision boundary becomes circular, instead of linear.
This allows SVM to properly separate the two classes.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow the Gaussian RBF Kernel Maps Data

--- Page 17 ---

The parameter σ controls how far the
influence of a landmark spreads.
Increasing σ makes the kernel spread out,
meaning:
More points are considered similar.
The decision boundary becomes smoother.
Effect on Classification:
A larger σ  makes decision boundaries wider
and smoother.
Useful when classes are widely spread out.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe Effect of Increasing σ  (Sigma)

--- Page 18 ---

Reducing σ makes the influence of the
landmark smaller.
The decision boundary becomes tighter
around points.
The model focuses only on very close points.
Risk of Small σ :
If σ is too small, the decision boundary can
become too complex.
This leads to overfitting (memorizing training
data but performing poorly on new data).KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe Effect of Decreasing σ  (Sigma)

--- Page 19 ---

Instead of one landmark, we use multiple
landmarks across the dataset.
The final transformation is a sum of multiple
Gaussian functions.
Effect on the Decision Boundary:
The model creates a complex but smooth
decision boundary.
The boundary can capture non-linear patterns
in the data.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCombining Multiple Gaussian Kernels
>0
=0

--- Page 20 ---

Sigmoid Kernel
Based on the hyperbolic tangent (tanh)
function, similar to neural networks.
Transforms the data using a sigmoid-like
shape.
The parameters γ  (gamma) and r control the
shape of the transformation.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRTypes of Kernel Functions in SVM

--- Page 21 ---

Polynomial Kernel:
Maps the input space into a higher polynomial
degree space.
The degree (d) determines the complexity of
the decision boundary.
When to Use It:
When there is a polynomial relationship
between features.
When data is not too high-dimensional, as high
degrees can be computationally expensive.KERNAL SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRTypes of Kernel Functions in SVM

--- Page 22 ---

NON-Linear
SVM
(Advanced)

--- Page 23 ---

The scatter plot shows data that does not
follow a straight line.
A simple linear model will not be able to
capture this pattern.
We need a method to handle this non-
linearity.NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRThe Problem – Non-Linear Data

--- Page 24 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRAttem pting a Linear Fit
A linear SVR model tries to fit a straight-line regression with a margin (yellow band).
The margin represents the acceptable error (epsilon-tube), where points inside it are considered close enough to the prediction.
However, since the data follows a curved pattern, many points fall outside the margin (red circled points), indicating a poor fit.

--- Page 25 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMoving to a Higher-Dimensional Space
Instead of forcing a straight-line fit, we
use the Kernel Trick.
The idea is to map the data into a
higher dimension 
where it becomes easier to fit a curve.
In the new space, the pattern
becomes clearer.

--- Page 26 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMoving to a Higher-Dimensional Space
The Gaussian Radial Basis Function
(RBF) Kernel is used to map data into a
higher dimension.
In this new space, the data forms a
peak-like structure.
SVR can now fit a better regression
model by drawing a flat plane in the
transformed space.

--- Page 27 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMoving to a Higher-Dimensional Space
SVR finds the best-fitting surface in the
transformed space.
This ensures that the model captures
the curved pattern of the original data.

--- Page 28 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRMoving to a Higher-Dimensional Space
Once the model is trained in the
higher-dimensional space, we map it
back to the original space.
The result is a smooth, non-linear
regression curve that properly fits the
data.

--- Page 29 ---

NON-Linear SVM
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRSummary of SVMs 
Once the model is trained in the
higher-dimensional space, we map it
back to the original space.
The result is a smooth, non-linear
regression curve that properly fits the
data.

--- Page 30 ---

Hands-On Code
KERNAL SVM

---


### 09

--- Page 1 ---

Evaluating
Classification
Model

--- Page 2 ---

When evaluating a classification model, we often deal with prediction errors. Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRFalse Positives & False Negatives

--- Page 3 ---

False Positives (Type I Error)
The model incorrectly predicts a positive
outcome when the actual outcome is negative.
Example: A medical test predicts a patient has
a disease when they do not.
False Negatives (Type II Error)
The model incorrectly predicts a negative
outcome when the actual outcome is positive.
Example: A medical test predicts a patient
does not have a disease when they actually do.Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRFalse Positives & False Negatives

--- Page 4 ---

These errors are crucial for measuring model performance.
A good classification model should minimize both types of errors while maintaining high accuracy.
Depending on the application, one type of error may be more costly than the other (e.g., in fraud
detection, false negatives can be more dangerous).Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRHow This Relates to Model Evaluation

--- Page 5 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRConfusion Matrix & Accuracy
The confusion matrix is a fundamental tool for evaluating
classification models. 
It provides a summary of prediction results by comparing
actual and predicted values. 
The main components are:
True Positive (TP): The model correctly predicted the
positive class.
True Negative (TN): The model correctly predicted the
negative class.
False Positive (FP) (Type I Error): The model incorrectly
predicted positive when the actual class was negative.
False Negative (FN) (Type II Error): The model incorrectly
predicted negative when the actual class was positive.

--- Page 6 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRConfusion Matrix & Accuracy

--- Page 7 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRPrecision, Recall, and F1-Score Explanation
Precision (Positive Predictive Value):
Precision measures the accuracy of positive
predictions made by the model. 
It answers:
"Of all the instances predicted as positive, how
many were actually positive?"
High Precision: Few false positives, meaning when
the model predicts positive, it is often correct.
Low Precision: Many false positives, meaning the
model is often incorrect in predicting positives.

--- Page 8 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRPrecision, Recall, and F1-Score Explanation
Recall (Sensitivity or True Positive Rate):
Recall measures how well the model identifies all
actual positive cases. 
It answers:
"Of all the actual positive cases, how many did the
model correctly identify?"
High Recall: Few false negatives, meaning most
actual positives are correctly classified.
Low Recall: Many false negatives, meaning the
model misses many actual positives.

--- Page 9 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRPrecision, Recall, and F1-Score Explanation
F1-Score (Harmonic Mean of Precision & Recall)
The F1-score balances Precision and Recall. 
It is useful when we want a single metric that
considers both false positives and false negatives.

--- Page 10 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRPrecision, Recall, and F1-Score Explanation
Key Insights:
✅ Precision is important when false positives are costly (e.g., spam detection, where
incorrectly flagging an important email is bad).
✅ Recall is important when false negatives are costly (e.g., medical diagnoses, where
missing a disease is dangerous).
✅ F1-Score is a balanced metric, especially useful when the dataset is imbalanced.

--- Page 11 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRAccuracy Paradox - Scenario 1
Here isa confusion matrix with two classes (0 and 1).
The model achieves 98% accuracy, but it highlights a critical issue: imbalanced data.
While most negative cases (0s) are correctly predicted (9,700), the model fails to
correctly classify a significant number of positive cases (50 false negatives).
Accuracy alone does not tell the full story of model performance, especially in
imbalanced datasets.

--- Page 12 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRAccuracy Paradox -  Scenario #2
The model slightly improves, increasing
accuracy to 98.5%, but it completely ignores
class 1 (no correct positive predictions).
This highlights the accuracy paradox, where
accuracy increases while performance for an
important class worsens.
A high accuracy does not necessarily mean the
model is good. Other metrics like precision and
recall must be considered.

--- Page 13 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCAP (Cumulative Accuracy Profile) - Introduction
CAP is a visualization technique to evaluate classification models.
The x-axis represents total contacted (e.g., customers, patients, etc.), and the y-axis
represents the positive outcomes (e.g., purchases, disease detection).
The red curve shows the model's performance, while the blue diagonal represents
random selection.
A steeper curve indicates a better model.

--- Page 14 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCAP Curves - Performance Comparison
Compares different models:
Crystal Ball: A perfect model (ideal
case).
Good Model: A practical, effective
model.
Random Model: A model that performs
no better than random guessing.
The closer the curve is to the perfect
model, the better the classifier.

--- Page 15 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCAP Analysis - Model Evaluation
AR (Accuracy Ratio) Calculation:
AR = aR / aP, where:
aR is the area under the model’s
curve.
aP is the area under the perfect
model’s curve.
A higher AR value means a better model.
AP analysis provides a quantitative
measure of model quality.

--- Page 16 ---

Evaluating Classification Model
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRCAP Analysis - Model Evaluation

--- Page 17 ---

Hands-On Code
Evaluating Classification Model

---


### 10

--- Page 1 ---

Additional Topics
In Machine Learning

--- Page 2 ---

Association
Rule Learning

--- Page 3 ---

Additional Topics In Machine Learning
Association Rule Learning
Association Rule Learning is a machine learning technique used to discover relationships between
variables in large datasets. 
It is widely used in market basket analysis, recommendation systems, and fraud detection.
It is a rule-based approach that identifies frequent patterns, correlations, or associations in data.
Helps uncover hidden insights that may not be obvious through traditional analysis.
Typically expressed in IF-THEN rules:
Example: IF a customer buys bread, THEN they are likely to buy butter.

--- Page 4 ---

Additional Topics In Machine Learning
Association Rule Learning - Movie Recommendation

--- Page 5 ---

Additional Topics In Machine Learning
Association Rule Learning - Market Basket Optimization

--- Page 6 ---

Additional Topics In Machine Learning
Association Rule Learning models:
Apriori Algorithm
A popular association rule learning
algorithm.
Uses a breadth-first search and the "Apriori
property" (if an itemset is frequent, its
subsets must also be frequent).
Iteratively expands frequent itemsets to
find strong associations.
Efficient for large datasets but can be slow
due to multiple scans of the database.
Example: Finding frequent product
combinations in market basket analysis.ECLAT 
(Equivalence Class Clustering and Bottom-Up
Lattice Traversal)
A faster alternative to Apriori, using a
depth-first search approach.
Stores transactions in vertical format (lists
of item occurrences), reducing database
scans.
Works well with dense datasets but
struggles with very large itemsets.
Example: Used in recommendation systems
and fraud detection.

--- Page 7 ---

APriori - Support
Additional Topics In Machine Learning
Support: How frequently an itemset appears in the dataset.

--- Page 8 ---

APriori - Support
Additional Topics In Machine Learning

--- Page 9 ---

APriori - Confidence
Additional Topics In Machine Learning
Confidence: The probability that a rule is correct when applied.

--- Page 10 ---

APriori - Confidence
Additional Topics In Machine Learning

--- Page 11 ---

APriori - Lift
Additional Topics In Machine Learning
Lift: How much more likely items appear together than by random chance.

--- Page 12 ---

APriori - Lift
Additional Topics In Machine Learning

--- Page 13 ---

APriori - Algorithm Additional Topics In Machine Learning
Step 1: Set a minimum support and confidence
Step 2: Take all the subsets in transactions having higher support than
minimum support
Step 3: Take all the rules of these subsets having higher confidence than
minimum confidence
Step 4: Sort the rules by decreasing lift

--- Page 14 ---

ECLAT - Support
Additional Topics In Machine Learning

--- Page 15 ---

ECLAT - AlgorithmAdditional Topics In Machine Learning
Step 1: Set a minimum support
Step 2: Take all the subsets in transactions having higher support than minimum support
Step 3: Sort these subsets by decreasing support

--- Page 16 ---

Hands-On Code
 Boost Sales with Python Data
Mining

--- Page 17 ---

Dimensionality
Reduction
Techniques

--- Page 18 ---

Principal Component Analysis (PCA)Dimensionality Reduction Techniques
What is PCA?
A dimensionality reduction technique used in machine learning.
Converts high-dimensional data into fewer principal components while preserving variance.
Key Concepts:
Eigenvalues & Eigenvectors
Variance Maximization
Feature Transformation
Application:
Image compression
Reducing computation in ML models
Data visualization in lower dimensions

--- Page 19 ---

Linear Discriminant Analysis (LDA)
Dimensionality Reduction Techniques
A supervised dimensionality reduction technique used for classification.
Unlike PCA (which focuses on variance), LDA maximizes class separability.
Applications:
Face recognition
Text classification
Feature extraction

--- Page 20 ---

Kernel PCADimensionality Reduction Techniques
An advanced version of PCA that can handle nonlinear data.
Uses kernel trick to transform data into a higher-dimensional space before applying PCA.
Applications:
Image classification
Pattern recognition
Nonlinear feature extraction in ML

--- Page 21 ---

Clustering
Techniques

--- Page 22 ---

Clustering Techniques

--- Page 23 ---

Clustering Techniques
Centroid-Based Clustering:
Methodology: Groups data points around a central centroid.
Example Algorithms:
K-Means → Most common, requires a predefined number of clusters.
K-Means++ → Improves initialization in K-Means.
K-Medoids → Uses actual data points as cluster centers instead of averages.

--- Page 24 ---

Clustering Techniques
Connectivity-Based Clustering
Methodology: Forms clusters based on hierarchical relationships between points.
Example Algorithms:
Hierarchical Clustering (Agglomerative & Divisive):
Agglomerative: Starts with individual points and merges them into clusters.
Divisive: Starts with one large cluster and splits it into smaller ones.

--- Page 25 ---

Clustering Techniques
Density-Based Clustering:
Methodology: Groups data based on dense regions, allowing for irregularly shaped clusters.
Example Algorithms:
DBSCAN → Finds dense clusters and identifies noise as outliers.
OPTICS → Similar to DBSCAN but adjusts density thresholds dynamically.
HDBSCAN → Hierarchical version of DBSCAN, better at handling variable density.

--- Page 26 ---

Clustering Techniques
Graph-Based Clustering
Methodology: Uses graph distance (similarities between nodes) to form clusters.
Example Algorithms:
Affinity Propagation → Message-passing algorithm that finds cluster centers.
Spectral Clustering → Uses eigenvalues of similarity matrix for clustering.

--- Page 27 ---

Clustering Techniques
Distribution-Based Clustering
Methodology: Assigns probabilities to data points belonging to different distributions.
Example Algorithm:
Gaussian Mixture Models (GMMs) → Uses multiple Gaussian distributions to model data.
Compression-Based Clustering
Methodology: Reduces dimensionality before clustering.
Example Algorithm:
BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies) → Efficient for large datasets.

--- Page 28 ---

Clustering Techniques
Choosing the Right Clustering Algorithm
K-Means → Best for well-separated, spherical clusters.
Hierarchical → Good for small datasets with hierarchical relationships.
DBSCAN → Works well for arbitrary-shaped clusters and noisy data.
GMM → Ideal for clusters with overlapping distributions.
Spectral Clustering → Best for complex structures that traditional methods struggle with.

--- Page 29 ---

What is Missing in
This Course?

--- Page 30 ---

What is Missing in This Course?
PART -3 :Reinforcement Learning!
Reinforcement Learning is a powerful branch of Machine Learning. It is used to solve interacting problems where the data
observed up to time t is considered to decide which action to take at time t + 1. 
It is also used for Artificial Intelligence when training machines to perform tasks such as walking. 
Desired outcomes provide the AI with reward, undesired with punishment. Machines learn through trial and error.
Two Important Reinforcement Learning models in ML:
Upper Confidence Bound (UCB) 1.
Thompson Sampling 2.
Useful Resource : Click Here
In this book you will find the theory of Reinforcement Learning and Thompson Sampling clearly explained in text, as well as
many more practical activities.  You will also find other AI models such as Q-Learning, Deep Learning, Deep Q-Learning, Deep
Convolutional Q-Learning, and Convolutional Neural Networks.

--- Page 31 ---

What is Missing in This Course?
PART -3 :Reinforcement Learning!
Reinforcement Learning is a powerful branch of Machine Learning. It is used to solve interacting problems where the data
observed up to time t is considered to decide which action to take at time t + 1. 
It is also used for Artificial Intelligence when training machines to perform tasks such as walking. 
Desired outcomes provide the AI with reward, undesired with punishment. Machines learn through trial and error.
Two Important Reinforcement Learning models in ML:
Upper Confidence Bound (UCB) 1.
Thompson Sampling 2.
Useful Resource : Click Here
In this book you will find the theory of Reinforcement Learning and Thompson Sampling clearly explained in text, as well as
many more practical activities.  You will also find other AI models such as Q-Learning, Deep Learning, Deep Q-Learning, Deep
Convolutional Q-Learning, and Convolutional Neural Networks.

--- Page 32 ---

Congratulations

---


### 11

--- Page 1 ---

Model Selection

--- Page 2 ---

Model Selection | Validation
Concept of Validation:
An important decision when developing any machine learning model is how to evaluate its final performance.
 
To get an unbiased estimate of the model’s performance, we need to evaluate it on the data we didn’t use
for training.
The simplest way to split the data is to use the train-test split method. It randomly partitions the dataset into
two subsets (called training and test sets) so that the predefined percentage of the entire dataset is in the
training set.
Then, we train our machine learning model on the training set and evaluate its performance on the test set. 
In this way, we are always sure that the samples used for training are not used for evaluation and vice versa

--- Page 3 ---

Model Selection | Validation
Train-Test Split
Dividing a dataset in to two different complementary subsets. Then, use one subset for training and another
subset for testing. The testing subset is never getting trained over here.

--- Page 4 ---

Model Selection | Validation
Cross Validation
The train-split method has certain limitations. When the dataset is small, the method is prone to high variance.
Due to the random partition, the results can be entirely different for different test sets. Why? 
Because in some partitions, samples that are easy to classify get into the test set, while in others, the test set
receives the ‘difficult’ ones.
To deal with this issue, we use cross-validation to evaluate the performance of a machine learning model. 
In cross-validation, we don’t divide the dataset into training and test sets only once. 
Instead, we repeatedly partition the dataset into smaller groups and then average the performance in each group.
That way, we reduce the impact of partition randomness on the results.
Many cross-validation techniques define different ways to divide the dataset at hand. We’ll focus on the two most
frequently used: The k-fold & The leave-one-out methods.

--- Page 5 ---

Dividing a dataset into
k number of subsets.In one epoch, use k-1
subsets of data for
training and use the
remaining dataset for
testing. Like this, for every epoch testing dataset
will be different, but it will be out of those
k subsets of data. This is also called as k-
fold cross validation .
Model Selection | Validation
K-fold cross-validation
Example
Finally, the overall performance is the average of the model’s performance scores on those three test sets.

--- Page 6 ---

Model Selection | Validation
K-fold cross-validation

--- Page 7 ---

Model Selection | Validation
5-fold cross validation

--- Page 8 ---

Model Selection | Validation
Leave-One-Out Cross-Validation

--- Page 9 ---

Model Selection | Validation
Leave-One-Out Cross-Validation

--- Page 10 ---

Model Selection | Validation
K-fold vs LOO
When the size is small, LOO is more appropriate since it will use more training samples in each iteration. 
That will enable our model to learn better representations.
Coversely, we use K-fold method to train a model on large dataset since LOO trains n models, one per sample in the
data.
When our dataset contains a lot of samples, training so many models will take too long. So, the k-fold cross-validation
is more appropriate.
Also, in a large dataset, it is sufficient to use less than n folds since the test folds are large enough for the estimates to
be sufficiently precise.

--- Page 11 ---

Bias & Variance 
Trade-off

--- Page 12 ---

Bias & Variance Trade-off
Bias and Variance
Bias: It is the amount by which Machine Learning (ML) model predictions differ from
the actual value of the target.
e = yactual - ypred
Where e=Bias Error, yactual = Actual or Target Output and ypred= Predicted Output.
Variance: It is the amount by which the ML model prediction would change if we
estimate it using different training datasets.

--- Page 13 ---

Bias & Variance Trade-off
Bias and Variance
Suppose e1, e2, and e3 are the bias errors of the model with three different training
datasets.
Average Bias Error = b = (e1 + e2 + e3) / 3
Average Variance Error = [(e1 - b)2 + (e2 - b)2 + (e3 - b)2] / 3
Total Error = Bias + Variance

--- Page 14 ---

Bias & Variance Trade-off
Occam’s Razor Principle
Construct the simplest ML model which gives the acceptable accuracy on training
datasets and don’t complicate the model to over fit the training dataset.

--- Page 15 ---

Bias & Variance Trade-off
Under fitting and Overfitting
Under fitting: The ML model with the high bias pays very little attention to the training
dataset and leads to high error on training as well as testing datasets.
High bias tends to under fitting
Over fitting: The model with high variance pays a lot of attention to the training
dataset and does not generalize the unseen data.
High variance tends to over fitting

--- Page 16 ---

Bias & Variance Trade-off
Under fitting and Overfitting
Low Bias and Low Variance leads to Ideal ML model with 
acceptable performance.
Linear Regression, Logistic Regression, and Linear Discriminant Analysis are High Bias ML algorithms
Decision Tree, Support Vector Machine, and K-Nearest Neighbor are High Variance ML algorithms.

--- Page 17 ---

Bias & Variance Trade-off
Under fitting and Overfitting
Figure 1 shows that over fit model covers all training samples where as under fit model covers only very few samples. Good
balance model covers the samples with acceptable accuracy.

--- Page 18 ---

Bias & Variance Trade-off
Under fitting and Overfitting
Figure 1 shows that over fit model covers all training samples where as under fit model covers only very few samples. Good
balance model covers the samples with acceptable accuracy.

--- Page 19 ---

Bias & Variance Trade-off
Bull’s Eye for Bias and Variance Tradeoff
Figure 2 shows Bull’s Eye for Bias and
Variance tradeoff.
High Bias and Low Variance leads to
Under fitting.
Low Bias and High Variance leads to Over
fitting.
Low Bias and Low Variance leads to Ideal
Model or Good Model.

--- Page 20 ---

Hands-On Code
Implementing K-Fold CV in
Python

--- Page 21 ---

GRID SEARCH

--- Page 22 ---

GRID SEARCH
Concept of Grid Search
Grid search is a popular hyperparameter tuning technique used in machine
learning to find the optimal hyperparameters for a model.
Hyperparameters are parameters that are set by the user before training the model
and cannot be learned by the model during training.

--- Page 23 ---

GRID SEARCH
HOW TO USE GRID SEARCH
The grid search algorithm involves specifying a range of values for each
hyperparameter and then evaluating the performance of the model for all possible
combinations of these values.
The performance of the model is usually measured by a scoring metric such as
accuracy or F1 score.
The combination of hyperparameters that results in the best performance is
selected as the optimal set of hyperparameters for the model.

--- Page 24 ---

GRID SEARCH
ADVANTAGES OF GRID SEARCH
Exhaustive search: Grid search exhaustively searches through a hyperparameter
space, ensuring that the optimal set of hyperparameters is found.
Simple implementation: Grid search is simple to implement and does not require
any advanced optimization techniques.
Reproducible results: Grid search produces reproducible results, as the same
hyperparameters will always produce the same model.

--- Page 25 ---

GRID SEARCH
DISADVANTAGES OF GRID SEARCH
Computationally expensive: Grid search can be computationally expensive,
particularly when there are many hyperparameters or large datasets.
Limited search space: Grid search is limited to the hyperparameters and their
respective ranges specified by the user, which may not include the optimal set of
hyperparameters.

--- Page 26 ---

GRID SEARCH
GRID SEARCH USING PYTHON
Finding the values of the important parameters of a model (the ones that provide
the best generalization performance) is a tricky task, but necessary for almost all
models and datasets.
Because it is such a common task, there are standard methods in scikit-learn to
help you with it.
The most commonly used method is grid search, which basically means trying all
possible combinations of the parameters of interest.

--- Page 27 ---

Consider the case of a kernel SVM with an RBF (radial basis function) kernel, as
implemented in the SVC class.
There are two important parameters: the kernel bandwidth, gamma, and the
regularization parameter, C.
Say we want to try the values 0.001, 0.01, 0.1, 1, 10, and 100 for the parameter C,
and the same for gamma.
GRID SEARCH
Example

--- Page 28 ---

Involves creating a grid of hyperparameters and performing k-fold cross-validation
for each combination
The algorithm selects the hyperparameters that result in the best average cross-
validation score
Helps to avoid overfitting by evaluating the model on multiple validation setsGRID SEARCH
GRID SEARCH WITH CROSS VALIDATION

--- Page 29 ---

GRID SEARCH
GRID SEARCH WITH CROSS VALIDATION

--- Page 30 ---

GRID SEARCH
Overview of the process of parameter selection and model evaluation
with GridSearchCV

--- Page 31 ---

Hands-On Code
GridSearchCV
Implementation

--- Page 32 ---

Xgboost 

--- Page 33 ---

XgBoost is a powerful machine learning algorithm.
It is designed to optimize performance and computational speed
XGBoost (Extreme Gradient Boosting) is an optimized version of Gradient Boosting.
Used for structured data tasks like classification and regression.Xgboost 
What is Xgboost?

--- Page 34 ---

Fast and Efficient – Parallel computing & optimized execution
Handles Missing Data – Built-in techniques for handling NaN values
Prevents Overfitting – Regularization methods included
Scalable – Works on large datasets efficientlyXgboost 
W hy XGBoost?

--- Page 35 ---

From Decision Trees to XGBoost:
Decision Trees – Simple rule-based models
Bagging (Random Forest) – Combines multiple trees to reduce variance
Boosting (Gradient Boosting) – Sequential training to minimize errors
 XGBoost – Optimized Gradient Boosting with additional featuresXgboost 
Evolution of XGBoost

--- Page 36 ---

Xgboost 
Evolution of XGBoost

--- Page 37 ---

Xgboost 
How Gradient Boosting Works – Key Tips
 1. Starts with a Weak Model
The process begins with a simple decision tree (often called a "weak learner").
This model makes basic predictions but has errors (residuals).
 2. Focuses on Errors
Instead of learning from scratch, gradient boosting builds new trees to correct errors from the previous model.
It identifies where predictions are wrong and focuses on improving those areas.
3. Uses Gradient Descent
The algorithm minimizes the loss function by using gradient descent (step-by-step improvement).
Each new model moves in the direction of reducing error (like walking downhill).

--- Page 38 ---

Xgboost 
How Gradient Boosting Works – Key Tips
4. Adds Models Sequentially
Each new tree is added one at a time to refine predictions.
Models work together to create a strong final model.
5. Controls Overfitting
Learning rate controls how much each new model adjusts.
Tree pruning & regularization help prevent overfitting (memorizing training data).
6. Final Prediction = Sum of All Trees
The final result is a combination of all the models, leading to high accuracy and strong generalization.

--- Page 39 ---

Xgboost 
Important Notes about Xgboost
Loss Function in XGBoost
XGBoost minimizes the loss function (error) using gradient boosting.
Common loss functions:
Regression: Mean Squared Error (MSE)
Classification: Log Loss (for binary) / Softmax Loss (for multi-class)
Loss Function in XGBoost
XGBoost minimizes the loss function (error) using gradient boosting.
Common loss functions:
Regression: Mean Squared Error (MSE)
Classification: Log Loss (for binary) / Softmax Loss (for multi-class)

--- Page 40 ---

Xgboost 
Important Notes about Xgboost
Hyperparameters in XGBoost
Before running the code, you should understand key parameters:
n_estimators – Number of trees (boosting rounds).
learning_rate (eta) – Controls step size of boosting (small values prevent overfitting).
max_depth – Limits tree depth to prevent overfitting.
subsample – Percentage of data used in each boosting round.
colsample_bytree – Fraction of features used per tree (like Random Forest).
lambda & alpha – L2 and L1 regularization terms.
Handling Missing Values
XGBoost can automatically handle missing data by learning optimal splits.
No need to manually fill missing values before training.

--- Page 41 ---

Xgboost 
Important Notes about Xgboost
Understanding XGBoost Output (Feature Importance)
XGBoost provides feature importance scores, helping understand which features contribute the most.
Useful for feature selection and improving model performance.
Why is XGBoost faster?
Uses parallel computing (multi-threading) to train trees quickly.
Optimized memory usage to handle large datasets efficiently.
Tree pruning (depth-wise growth) improves speed & reduces overfitting.

--- Page 42 ---

Feature AdaBoost XGBoost
Base Model
Optimization
Weighting Strategy
Loss Function
Regularization
Speed & Performance
Handling Missing Data
Tree Pruning
Parallelization
Use CaseAdaBoost
AdaBoost (Adaptive Boosting) and XGBoost (Extreme Gradient Boosting) are both boosting algorithms that
improve weak learners into strong classifiers.
Homework

--- Page 43 ---

Hands-On Code
XGBoost Implementation

--- Page 44 ---

The End.

---


### 12

--- Page 1 ---

AI Diploma

--- Page 2 ---

Semester One | Course TwoMachine Learning Algorithms
and Applications

--- Page 3 ---

Data PreprocessingUnit 1: Basic Data
processing methods
and regression Unit 2: Advance
Regression Algorithms Unit 3:
Classification Unit 4 : Clustering
& Dimensionality
ReductionUnit 5: Model Selection
& Boosting  
ClassificationClusteringRegression AlgorithmsML
Road
Map
Dimensionality ReductionMissing Data
Categorical Data
Template For
Preprocessing Data
(General Steps)K-Means Clustering
Hierarchical ClusteringSupport Vector
Regression
Decision Tree Regression
Random Forest
Regression
Evaluating Regression
Model
Regularisation MethodsK-Nearest Neighbors (K-NN)
Support Vector Machine
(SVM)
Kernel SVM
Naive Bayes
Decision Tree Classification
Random Forest Classification
Evaluating Classification
ModelModel Selection
XGBoost
Principal Component
AnalysisRegression
Simple Linear
Regression
Multiple Linear
Regression
Polynomial regressionClassification in Regression
Logistic RegressionROADMAP

--- Page 4 ---

Semester One | Course TwoMachine Learning Algorithms and Applications
Unit 1 : Basic Data
Processing Methods
and Regression

--- Page 5 ---

 Data Preprocessing

--- Page 6 ---

The Machine Learning Process
Data Pre-
Processing1 2 3
Data Pre-Processing
Import the data
Clean the data
Split into training & test sets
Feature ScalingModelling
Modelling
Build the model  
Train the model
Make predictionsEvaluation
Evaluation
Calculate performance
metrics
Make a predict

--- Page 7 ---

Training Set & Test Set
https://support.cognex.com/docs/deep-learning_311/web/EN/deep-learning/Content/deep-learning-Topics/training-blue-read/prepare-train-test.htm?TocPath=Training%20Blue%20Read%7C_____8

--- Page 8 ---

Feature Scaling
Feature scaling is a technique to
standardize or normalize the
range of independent variables
(features).
It ensures that no feature
dominates the learning process
due to larger numerical values.
Examples of why it’s needed:
Height (cm) and weight (kg)
might have very different ranges.

--- Page 9 ---

Feature Scaling
Improves Model Performance: Many ML algorithms rely on distance-based
calculations (e.g., KNN, SVM, Gradient Descent).
Speeds Up Convergence: For optimization algorithms, scaling helps them reach
a solution faster.
Avoids Bias: Prevents large values from dominating smaller ones.Why Do We Need It?

--- Page 10 ---

Feature Scaling
Normalization
Rescales data between 0 and 1.
Suitable for: Algorithms sensitive to absolute magnitudes (e.g., KNN).).Standardization
Rescales data to have a mean of 0 and a standard deviation of 1.
Suitable for: Gaussian-distributed features (e.g., Logistic Regression)

--- Page 11 ---

Feature Scaling
Normalization
Rescales data between 0 and 1.
Suitable for: Algorithms sensitive to absolute magnitudes (e.g., KNN).).Standardization
Rescales data to have a mean of 0 and a standard deviation of 1.
Suitable for: Gaussian-distributed features (e.g., Logistic Regression)

--- Page 12 ---

Feature Scaling
Normalization
Use when features have different ranges but need to be scaled between 0 and 1.
Example: Min-Max Scaling.
Standardization
Use when data needs a Gaussian distribution or involves outliers.Choosing the Right Scaling Method

--- Page 13 ---

Feature Scaling
Example
Normalization
1
0 . 8
01
0 . 4 4 4
0

--- Page 14 ---

Data that represents categories or groups.
Types:
Ordinal: Has an order (e.g., small, medium, large).
Nominal: No order (e.g., colors: red, green, blue).
Why Handle Categorical Data?
Machine learning models require numerical data.
Example:
Raw: ["Red", "Green", "Blue"]
Encoded: [1, 2, 3] or One-Hot Encoding.Categorical Data
What is Categorical Data?

--- Page 15 ---

Categorical Data
How to deal with Categorical Data?
Ordinal Encoding 

--- Page 16 ---

Categorical Data
How to deal with Categorical Data?
One Hot Encoding 

--- Page 17 ---

Categorical Data
How to deal with Categorical Data?
Dummy Encoding 

--- Page 18 ---

Categorical Data
How to deal with Categorical Data?
Other Type Encoding 
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniques

--- Page 19 ---

Handling Missing Data
What is Missing Data?
Missing or incomplete values in the dataset.
Types of Missing Data:
Missing Completely at Random (MCAR).
Missing at Random (MAR).
Not Missing at Random (NMAR).
Challenges:
Leads to biased models or errors in predictions.

--- Page 20 ---

Handling Missing Data
Why we have Missing Data?
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniques

--- Page 21 ---

Handling Missing Data
1) Missing completely at random (MCAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesMCAR is a situation in which the data is genuinely missing at random and has no relation to any observed or unobserved variables.
In other words, the missing data points follow no recognized pattern.

--- Page 22 ---

Handling Missing Data
1) Missing completely at random (MCAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesUnrealistic Assumption: MCAR is rarely realistic in real-world datasets because missing data is often influenced by observed or unobserved factors.
Influencing Factors: Missing data may arise due to:
Human behavior (e.g., omitting sensitive information).
Survey administration errors.
External events influencing responses.
Selective Missingness: Certain groups or individuals may be more likely to leave responses blank, leading to patterns in missingness.
Need for Context: Assuming MCAR requires:
Understanding the full data collection process.
Consulting domain experts.
Collaboration between data scientists and data engineers.
Practical Approach: If MCAR seems reasonable after analysis or expert input, simple imputation techniques can be used for handling missing values.

--- Page 23 ---

Handling Missing Data
2) Missing at random (MAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesMAR is a situation in which the missingness of one feature can be explained by other observed features in the dataset.

--- Page 24 ---

Handling Missing Data
2) Missing at random (MAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesMissing at Random (MAR) assumes that the probability of missing data is related to observed features but not to the
missing feature itself.
Practical Observation: MAR is more commonly seen in real-world datasets compared to MCAR.
Missingness can be estimated using available data, allowing for accurate imputation through statistical methods.
To identify MAR, examine if the probability of missingness changes based on other observed features.
Example: In an academic survey, students with higher grades might avoid reporting study hours, showing a
relationship between grades (observed feature) and missingness.
Imputation Techniques for MAR:
kNN Imputation
Miss Forest
These methods leverage observed features to fill in missing values effectively.

--- Page 25 ---

Handling Missing Data
kNN Imputation
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniques

--- Page 26 ---

Handling Missing Data
Miss Forest
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniques

--- Page 27 ---

Handling Missing Data
3) Missing not at random (MNAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesMNAR is the most complicated situation of all three.
In MNAR, missingness is either attributed to the missing value itself or the feature(s) that we didn’t collect data for.

--- Page 28 ---

Handling Missing Data
3) Missing not at random (MNAR)
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesPreserving Missingness Patterns: Add a binary indicator feature to flag whether a
value was imputed. This allows machine learning algorithms to recognize and learn
from the missingness pattern.MNAR is the most complicated situation of all three.
In MNAR, missingness is either attributed to the missing value itself or the feature(s) that we didn’t collect data for.
Unlike MCAR (no pattern) or MAR (related to observed features), MNAR has a clear missingness pattern tied to the missing variable.
Example: In a health survey, individuals with high stress levels might avoid disclosing their stress level due to stigma, creating a non-
random missingness pattern.
Challenge: Since missingness is dependent on the missing variable, it’s difficult to address without collecting additional data or having
domain expertise.

--- Page 29 ---

Data Preprocessing Template
https://blog.dailydoseofds.com/p/7-categorical-data-encoding-techniquesSteps to Follow:
Load the data.
Check for missing data and handle it.
Encode categorical data.
Split dataset into training and test sets.
Feature scale numerical data.
Input Raw Data → Handle Missing Data → Encode
Categories → Train/Test Split → Scale Features → 
ML Algorithm

--- Page 30 ---

Hands-On Code
Data Preprocessing Template

---


### 13

--- Page 1 ---

Regression

--- Page 2 ---

Sim ple Linear
Regression

--- Page 3 ---

Sim ple Linear Regression

--- Page 4 ---

Sim ple Linear Regression
Linear regression tries to model the relationship between an
independent variable (x1 , e.g., Nitrogen Fertilizer) and a dependent
variable (y, e.g., Potato Yield) using a straight line.
Points in the Plot:
Each blue dot represents a separate observation or harvest.
The model attempts to fit the best line that minimizes the error
(distance) between the actual data points and the predicted
values.
Regression Line:
The grey line is the fitted regression line.
It shows the predicted relationship between x1  (fertilizer) and y
(yield).
Slope of the Line:
The slope (+3t) indicates that for every 1 kg increase in Nitrogen
Fertilizer, the Potato Yield increases by 3 tonnes.
This is the coefficient of x1  in the regression equation:
                                                       y=8+3x1
Intercept (Baseline Value):
The intercept (8t) represents the predicted Potato Yield when no
fertilizer (x1 =0) is used.

--- Page 5 ---

Sim ple Linear Regression

--- Page 6 ---

Ordinary Least Squares

--- Page 7 ---

Multiple Linear Regression

--- Page 8 ---

Multiple Linear Regression
Definition: Multiple linear regression models the relationship between one dependent
variable (y) and two or more independent variables (x1 ,x2 ,...,xn ), using the equation:
Purpose: It predicts the dependent variable (y) based on multiple factors
(independent variables), allowing a more comprehensive analysis of real-world
scenarios.

--- Page 9 ---

R Squared

--- Page 10 ---

R Squared
R-Squared is a statistical measure that explains how well the regression line fits the
observed data.
It represents the proportion of variance in the dependent variable (y) that is
predictable from the independent variable (x1 ).
SSres : Residual Sum of Squares (difference between actual values yi  and predicted values y^ i ).
SStot : Total Sum of Squares (difference between actual values yi  and the mean of y (yavg )).

--- Page 11 ---

R Squared

--- Page 12 ---

Adjusted R Squared
Problem with R-Squared:
R-Squared always increases or stays the same when you add more predictors (x3 ,x4 ) to the model, even if the new
predictors don't contribute meaningful information.
This happens because adding predictors reduces SSres  (Residual Sum of Squares) or keeps it the same, but SStot 
remains constant.
Issue with Overfitting:
Adding irrelevant predictors makes the model more complex without improving its performance or explanatory
power, leading to overfitting.
R-Squared cannot penalize for unnecessary predictors, so it can give a false impression of better performance.

--- Page 13 ---

Adjusted R Squared
Solution: Adjusted R-Squared:
Adjusted R-Squared penalizes for adding predictors that don't improve the model.
It provides a more realistic measure of how well the model explains the variability in the data.

--- Page 14 ---

Assumptions Of
Linear Regression

--- Page 15 ---

Assumptions Of Linear Regression
Linear regression relies on several key
assumptions to ensure accurate
predictions and meaningful results. 
linearity assumes a straight-line
relationship between the dependent
variable (y) and each independent
variable (x1 ,x2 ,...). 
If the relationship is non-linear, linear
regression will not capture it correctly. 

--- Page 16 ---

Assumptions Of Linear Regression
Linear regression works best when certain conditions are
met, ensuring accurate and reliable results. 
These conditions include:
Linear Relationship: The dependent variable (y) should
have a straight-line relationship with the independent
variables (x1 ,x2 , etc.).1.
Equal Spread of Errors: The variation in prediction errors
should stay consistent across all values of the
independent variables.2.
Normal Distribution of Errors: The errors (differences
between actual and predicted values) should follow a
normal distribution.3.
Independence: Each observation in the data should be
independent of the others.4.
No Strong Correlation Between Variables: Independent
variables should not be too closely related to each other,
as it can confuse the model.5.
Check for Outliers: Outliers can heavily influence the
regression line and should be addressed if found.6.
If these conditions aren't met, the model might not provide
the best predictions, and adjustments or different techniques
may be needed.

--- Page 17 ---

Dum m y Variables

--- Page 18 ---

Dum m y Variables

--- Page 19 ---

Dum m y Variables

--- Page 20 ---

Dummy 
Variables Trap

--- Page 21 ---

Dummy Variables Trap
Dummy Variables:
"State" is converted into two dummy variables:
New York (D₁): 1 if the state is New York, 0
otherwise.
California (D₂): 1 if the state is California, 0
otherwise.
Dummy Variable Trap:
Notice that the two dummy variables are highly
dependent: 
if D₁ = 1 (New York), D₂ must be 0 (California), and
vice versa.
This creates a problem of multicollinearity in the regression
model because one dummy variable can be perfectly
predicted from the other (e.g., D2 =1−D1 ).
Multicollinearity makes it hard for the model to estimate
coefficients correctly.

--- Page 22 ---

Dummy Variables Trap
Solution:
To avoid the trap, drop one dummy variable (e.g., D₂)
from the model.
Now, the model only uses D₁ to represent the "State"
variable, while the dropped category (e.g., California)
becomes the baseline.
For example:
If D₁ = 1 → State is New York.
If D₁ = 0 → State is California (by default).
Regression Equation:
The equation includes:
Numerical variables (x1 ,x2 ,x3 ) like R&D Spend,
Admin, Marketing.
A single dummy variable (D1 ) representing the state.
This avoids the dummy variable trap while still
capturing the effect of the state on profit.

--- Page 23 ---

Building A Model

--- Page 24 ---

Building A Model
The idea here is to explain different methods of building regression
models by selecting the most relevant predictors (independent
variables). 
These methods aim to balance simplicity and accuracy in the model,
ensuring only significant variables are included

--- Page 25 ---

 Use all the predictors without elimination.
When to use:
You have prior knowledge that all variables are important.
It's required to include all variables (e.g., for regulatory reasons).
You're preparing for Backward Elimination and want to start with all predictors.Building A Model
All in one 

--- Page 26 ---

Start with all predictors and remove the least significant one (based on p-value) until only
significant predictors remain.
Steps:
Set a significance level (e.g., SL=0.05). 1.
Fit a full model with all predictors. 2.
Remove the predictor with the highest p-value if p>SL, then refit the model. 3.
Repeat until all remaining predictors have p<SLp<SL. 4.
 Useful when starting with many predictors and you want to eliminate irrelevant ones.Building A Model
Backward
Elimination

--- Page 27 ---

Start with no predictors and add the most significant one step-by-step.
Steps:
Set a significance level for inclusion (e.g., SL=0.05). 1.
Fit models with each predictor separately and select the one with the lowest p-value. 2.
Add the selected variable and repeat by testing additional predictors one by one. 3.
Stop when no remaining variable has p<SL. 4.
 Useful when starting with no predictors and gradually adding relevant ones.Building A Model
Forward
Selection

--- Page 28 ---

Combine Forward Selection and Backward Elimination by adding and removing predictors
dynamically.
Steps:
Set significance levels for adding (SLENTER ) and removing (SLSTAY ). 1.
Add new predictors with p<SLENTER  (like Forward Selection). 2.
Remove existing predictors with p>SLSTAY  (like Backward Elimination). 3.
Repeat until no variables can be added or removed. 4.
Useful when you want a flexible approach that checks both directions.Building A Model
Bidirectional
Elimination

--- Page 29 ---

The significance level (SL) is a threshold used in statistical tests to decide whether a
variable is significant enough to be included in a regression model.  
Standard Practice (Default Value):
SL=0.05: This is a common default value used in most statistical analyses.
It corresponds to a 5% risk of incorrectly rejecting a variable that is actually
significant (Type I error).
Widely accepted in fields like science, engineering, and social sciences.Building A Model
Why SL=0.05 (Significance Level) ? 

--- Page 30 ---

Based on Desired Confidence:
Relationship to Confidence Level:
SL=1−Confidence Level.
For example:
SL=0.05SL=0.05 → 95% Confidence Level.
SL=0.01SL=0.01 → 99% Confidence Level (more stringent).
SL=0.10SL=0.10 → 90% Confidence Level (less stringent).
Domain-Specific Considerations:
High-Stakes Decisions: Use a smaller SL (e.g., SL=0.01) in fields where errors are costly, such as medicine,
finance, or safety-critical industries.
Exploratory Analysis: Use a larger SL (e.g., SL=0.10) if you're exploring data and want to include more
predictors for further analysis.Building A Model
Why SL=0.05 (Significance Level) ? 

--- Page 31 ---

Size of Dataset and Model Complexity:
Large Datasets: A smaller SL (e.g.,SL=0.01) might be more appropriate since larger datasets can detect even
small effects.
Small Datasets: A larger SL (e.g.,SL=0.10) might be acceptable because small datasets may lack the power to
detect subtle relationships.
Practical Tips:
Start with SL=0.05 as a general rule.
Adjust it based on:
The importance of avoiding errors in your context.
The size and complexity of your data.
Your domain knowledge and goals.Building A Model
Why SL=0.05 (Significance Level) ? 

--- Page 32 ---

Hands-On Code
Simple Linear Regression

--- Page 33 ---

Hands-On Code
Multiple Linear Regression

--- Page 34 ---

Polynomial
Regression

---


### 14

--- Page 1 ---

Polynom ial Regression

--- Page 2 ---

Polynomial Regression
Polynomial Linear Regression is an extension of linear regression that models non-linear relationships
by transforming the input variables into polynomial terms. Even though the relationship between the
variables may not be linear, the regression itself is still considered "linear" because the model is linear in
terms of the coefficients.

--- Page 3 ---

Polynomial Regression
Key Features of Polynomial Regression
Transformation of Variables:
In regular linear regression, the model is: y=b0 +b1 x
In polynomial regression, higher-order terms are added:y=b0+b1x+b2x2+b3x3+…
These polynomial terms allow the model to capture curves or more complex relationships.
Fitting Curves:
Useful when the data shows a non-linear relationship, such as U-shaped, S-shaped, or exponential
patterns.
Still a "Linear Model":
Even though the relationship is non-linear, it is called "linear" because the equation remains linear in
terms of the coefficients (b0,b1,b2).
This is why it's called Polynomial Linear Regression.

--- Page 4 ---

Polynomial Regression
When to Use Polynomial Regression?
When the data shows clear non-linear patterns that cannot be captured by regular linear regression.
When adding flexibility is needed for better accuracy but without overfitting (important to choose the
right degree of the polynomial).

--- Page 5 ---

Polynomial Regression
Why Do We Need Polynomial Regression?
Linear regression works only for straight-line
relationships.
Many real-world relationships are non-linear,
such as:
Population growth.
Disease progression.
Economic data (e.g., sales trends).
Example: Stock price data that linear regression
cannot capture.
https://www.investopedia.com/terms/p/polynomial_trending.asp

--- Page 6 ---

Polynom ial Regression
How Polynom ial Regression W orks
C o n v e r t the input variable (x) into polynomial terms (x^2,x^3).
A p p l y linear regression to estimate coefficients ( β 0, β 1).
Higher-order terms allow the model to capture curves.

--- Page 7 ---

Polynomial Regression
Choosing the Polynomial Degree
The degree of the polynomial affects the model's
complexity:
Low degree: Underfitting (model too simple).
High degree: Overfitting (model too complex,
fits noise).
Use tools like:
Cross-validation.
Adjusted R2.

--- Page 8 ---

Polynomial Regression
Choosing the Polynomial Degree
https://allmodelsarewrong.github.io/overfit.html

--- Page 9 ---

Polynom ial Regression
Practical Applications
Use cases for polynomial regression:
Forecasting trends in sales or demand.
Modeling natural phenomena (e.g., rainfall vs. crop yield).
Predicting disease progression.
Engineering data (e.g., stress-strain curves).
---------------------------------------------------------------------------------------------------------
Limitations of Polynomial Regression
Overfitting when the degree is too high.
Sensitive to outliers.
May not generalize well to unseen data.
Not suitable for truly complex, non-linear relationships (consider other models like decision trees or
neural networks).

--- Page 10 ---

Hands-On Code
Polynomial Linear Regression

---


### 15

--- Page 1 ---

Clustering

--- Page 2 ---

Clustering
https://www.researchgate.net/publication/344389401_DS-Regression-04-SVRWhat is Clustering?
Clustering – grouping 
Unlabelled Data

--- Page 3 ---

Clustering
Image source: mdpi.com/2073-8994/10/12/73What is Clustering?

--- Page 4 ---

Clustering
Image source: mdpi.com/2073-8994/10/12/73What is Clustering?

--- Page 5 ---

K-Means
Clustering

--- Page 6 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
No labels data 
How many clusters ? 
Let consider twoReplace them randomly ,
any point (centroid)K-means assign distance
line to the closest these
centroid , easiest way like
this 

--- Page 7 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
Calculate mass or gravity of each
clusters ..
For take all x and get average and for
blue take all y and get the average so
you will find the cluster mass move the centriod to new positions
and repeat the process Place the line to the closest centroid 

--- Page 8 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
Repeat the process .. 

--- Page 9 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
Repeat the process .. 

--- Page 10 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
Repeat the process

--- Page 11 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
Repeat until the cluster wont change

--- Page 12 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Intuition Behind K-Means Clustering
So Here is our final clusters 

--- Page 13 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The question is how many clusters should
be/should we have !
Sometimes from the knowledge domain 
Sometimes we need to know how many we should have 

--- Page 14 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Elbow Method
It basically looks at the distance between each point and
the centroid and square it 

--- Page 15 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Elbow Method
In this example, measure each points with the centroid
and square it to find the WCSS  

--- Page 16 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Elbow Method
Case if we have two clusters

--- Page 17 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Elbow Method
Case if we have three clusters and so on ...

--- Page 18 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73The Elbow Method
If you notice, we need the clusters to find
WCSS .. so we need to run it first 
It is backward !! 
The more clusters we have,  the smaller WCSS
we have .. So we can continue increasing
numbers of clusters until we get max number
of clusters = number of points so WCSS will
become 0 
The optimal number of clusters is three
because it is the elbow , where WCSS stop
dropping as rapidly.
Judgment call !! sometimes not clear, more than
candidate .. so 

--- Page 19 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73K-Means++

--- Page 20 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73K-Means++
K-Means++ Initialization Algorithm:
Step 1: Choose first centroid at random among data point
Step 2: For each of the remaining data points compute the distance (D) to the nearest out of already selected centroids
Step 3: Choose next centroid among remaining data points using weighted random selection – weighted by D2
Step 4: Repeat Steps 2 and 3 until all k centroids have been selected 
Step 5: Proceed with standard k-means clustering

--- Page 21 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73K-Means++

--- Page 22 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73K-Means++

--- Page 23 ---

K-Means Clustering
Image source: mdpi.com/2073-8994/10/12/73K-Means++

---

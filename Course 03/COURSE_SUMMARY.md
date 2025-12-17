# Course 03 - Course Summary
## ملخص الدورة

This document provides a comprehensive text summary of all course materials.
هذا المستند يوفر ملخص نصي شامل لجميع مواد الدورة.

---


## Pptx Files



### 01

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Linear Algebra for Machine Learning

--- Slide 2 ---

Introduction to Linear Algebra
Fundamentals and Applications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Recall and explain the relationship between machine learning concepts and mathematical constructs like vectors and matrices.
Course Learning Outcomes:
Recall how machine learning and vectors and matrices are related
Interpret how changes in the model parameters affect the quality of the fit to the training data

--- Slide 4 ---

The Role of Linear Algebra in Machine Learning
Machine learning algorithms rely heavily on linear algebra. Vectors and matrices provide a concise and efficient way to represent data and perform the mathematical operations for many Machine Learning models. Let's explore how these mathematical tools are used:
Data Representation
Model Training and Computation
Optimization (Gradient Descent)
Dimensionality Reduction
Distance and Similarity Measures

--- Slide 5 ---

1. Data Representation
Feature Vectors:  Each data point in a machine learning dataset can be represented as a vector of features.  Think of it as a list of characteristics describing that data point.

Example: A house price prediction model may use a feature vector x = [area, bedrooms, age] = [1500, 3, 10]
Datasets as Matrices: When we have multiple data points, these feature vectors are organized into a matrix. Each row of the matrix represents a single data point (or instance), and each column represents a specific feature.
Rows = Data samples
Columns = Features
Example: A dataset with n samples and m features is represented as an n × m matrix.

--- Slide 6 ---

2. Model Training and Computation
Linear Regression: This model predicts a value based on a linear combination of the features. Using matrix multiplication to calculate the  predictions 
Model:  y = Xw + b
X: Feature matrix 
w: Weight vector 
b: Bias 
y: Predicted output
Y

--- Slide 7 ---

3. Optimization (Gradient Descent)
Machine learning models learn by adjusting their parameters (like w and b in linear regression). Gradient descent is a common algorithm for this, and it relies on vector calculus.
Process:  The gradient of a loss function (which measures how well the model is performing) is calculated. This gradient is a vector that points in the direction of the steepest ascent.  We move against the gradient (downhill) to find better parameter values.

--- Slide 8 ---

4. Dimensionality Reduction: Simplifying Complex Data
Imagine you're trying to understand a complex system, like the factors influencing a city's air quality. You might have dozens of measurements: pollution levels, traffic volume, weather conditions, industrial activity, and so on. Analyzing all these factors at once can be overwhelming and computationally expensive. This is where dimensionality reduction comes in.
What is Dimensionality Reduction?
Dimensionality reduction is a technique that aims to simplify high-dimensional data by reducing the number of features (or dimensions) while preserving the essential information. This simplification can make data easier to visualize, process, and analyze, and it can also help prevent overfitting in machine learning models. Techniques like:

Principal Component Analysis (PCA) use eigenvectors and eigenvalues (concepts from linear algebra) to reduce the number of features while preserving important information. This is useful for dealing with high-dimensional data.
Singular Value Decomposition (SVD): Another powerful technique for dimensionality reduction is Singular Value Decomposition (SVD). Unlike PCA, which works on the covariance matrix of the data, SVD directly decomposes the data matrix itself.

--- Slide 9 ---

5. Dimensionality Reduction: Simplifying Complex Data
5. Distance and Similarity Measures
Many machine learning algorithms rely on calculating distances or similarities between data points.
Euclidean Distance: A common way to measure the straight-line distance between two points (vectors).





Cosine Similarity: Measures the angle between two vectors, indicating how similar their directions are. This is often used in natural language processing and recommendation systems.

--- Slide 10 ---

Summary

--- Slide 11 ---

How Changes in Model Parameters Affect Fit Quality in Machine Learning
Model parameters (such as weights, biases, and hyperparameters) directly influence how well a model fits the training data. Here’s how different parameter changes impact model performance:
Equation of Linear Regression
Y= wX + b 
w(weight or slope): Controls how steep the line is.
b(bias or intercept): Shifts the line up or down.
Effect of Changing Parameters
Increasing w: Steeper slope, which can lead to overfitting.
Decreasing w: Flatter slope, which may cause underfitting.
Changing b: Moves the regression line up/down but does not affect the slope.

--- Slide 12 ---

How Changes in Model Parameters Affect Fit Quality in Linear Regression
.

--- Slide 13 ---

How Changes in Model Parameters Affect Fit Quality in Linear Regression
.
Effect of Changing Parameters:
Increasing w: The slope of the regression line becomes steeper. If weight is too large, the line may overfit the data.
Decreasing w: The slope becomes flatter. If weight is too small, the line may underfit the data.
Changing b: The intercept shifts the line up or down without affecting the slope.

The original data points scattered in blue.
Three regression lines corresponding to different values of w and b.

--- Slide 14 ---

Gradient Descent and Learning Rate Effect
.
The learning rate is a crucial parameter in gradient descent. It controls the size of the steps you take downhill:

High Learning Rate: If the learning rate is too high, you might take large steps and overshoot the lowest point, bouncing around and never settling at the optimal solution. This can lead to instability and prevent convergence.
Low Learning Rate: If the learning rate is too low, you'll take tiny steps, and it will take a very long time to reach the bottom of the valley. The training process will be very slow.
Optimal Learning Rate: A properly tuned learning rate allows the network to converge efficiently to a good solution. It's a balancing act – large enough to make progress but small enough to avoid overshooting.

In summary: Training a neural network involves carefully balancing the weights and biases to avoid overfitting and underfitting, and tuning the learning rate in gradient descent to ensure efficient convergence. It's a process of finding the sweet spot where the network learns the underlying patterns in the data without memorizing noise.

--- Slide 15 ---

Gradient Descent and Learning Rate Effect
.
Key Takeaways
High Learning Rate: Fast but unstable convergence.
Low Learning Rate: Slow but stable convergence.
Optimal Learning Rate: Balances speed and stability for efficient convergence.

--- Slide 16 ---

Regularization: Impact on Overfitting & Underfitting
.
Types of Regularization
L1 (Lasso): Shrinks some weights to zero → Feature selection.
L2 (Ridge): Shrinks weights but doesn’t remove them → Prevents overfitting.
Dropout (for neural networks): Randomly drops neurons to improve generalization.
Effect of Regularization Strength (λ\lambda)
No regularization → Overfits.
Moderate regularization → Generalizes well.
Too much regularization → Underfits.

--- Slide 17 ---

Effects of L2 Regularization on fit
.
No regularization (small λ\lambda) → Overfits.
Medium regularization → Best fit.
High regularization (large λ\lambda) → Underfits.

--- Slide 18 ---

Overall Effects of Parameters on Fit

--- Slide 19 ---

Practical Implementation
Click here for the code

--- Slide 20 ---

الشراكات العالمية

--- Slide 21 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 02

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Linear Algebra for Machine Learning

--- Slide 2 ---

Introduction to Linear Algebra
Fundamentals and Applications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Recall and explain the relationship between machine learning concepts and mathematical constructs like vectors and matrices.
Course Learning Outcomes:
Recognize that variations in the model parameters are vectors on the response surface - that vectors are a generic concept not limited to a physical real space
Use substitution / elimination to solve a fairly easy linear algebra problem
Understand how to add vectors and multiply by a scalar number

--- Slide 4 ---

Recognizing Variations in Model Parameters as Vectors on the Response Surface
Learning Objectives
Understand the concept of a response surface.
Recognize how changes in model parameters form vectors in parameter space.
Learn that vectors are an abstract concept beyond physical space.

--- Slide 5 ---

What is a Response Surface?
A response surface represents how an objective function (e.g., loss function) varies with model parameters.
Common in optimization, machine learning, and statistics.
Example: Loss function in neural network training.
Response Variable (Z-axis): This is the thing you're trying to optimize (minimize or maximize).  In machine learning, this is often the loss function – a measure of how poorly your model is performing.  Other examples could be the accuracy of your model
    
Predictor Variables (X and Y axes): These are the variables you can control that influence the response variable. In machine learning, these are the parameters of your model (e.g., the weights and biases in a neural network).  
.     
The Surface Itself: The surface itself represents the relationship between the predictor variables and the response variable.  The shape of the surface tells you how changing the parameters affects the loss.  Valleys in the surface represent areas of low loss (good performance), while peaks represent areas of high loss (poor performance).

--- Slide 6 ---

Why are Response Surfaces Important?
Response surfaces are crucial for understanding and optimizing complex systems, including machine learning models:   

  Visualization: They provide a visual representation of the relationship between parameters and the objective function, making it easier to understand how changes in parameters affect performance. 

  Optimization:  By analyzing the response surface, you can identify the "best" settings for your parameters 
This is what optimization algorithms like gradient descent do in machine learning.   

Understanding Interactions: Response surfaces can reveal how different parameters interact with each other.  For example, changing one parameter might have a different effect depending on the value of another parameter.
Loss

--- Slide 7 ---

Vectors in Generic Spaces
Vectors are not limited to the familiar 2D and 3D physical space. 
Vectors exist in any space: physical, abstract (e.g., probability distributions, function spaces).
The same rules (addition, scalar multiplication) apply.
Example: A vector in high-dimensional machine learning models represents adjustments to weights.

In machine learning, a model's weights are adjusted during training to improve its performance. These adjustments can be represented as a vector in a high-dimensional space where each dimension corresponds to a weight. The direction of the vector indicates how each weight should be changed, and the magnitude of the vector indicates the size of the adjustment.

--- Slide 8 ---

Solving Linear Equations: The Substitution Method
What is Substitution?
Substitution is a technique for solving systems of equations by expressing one variable in terms of the others and then replacing that variable in another equation.This reduces the problem to a simpler equation with fewer variables.It's like replacing a part in a machine with an equivalent part to make it easier to work with.

Consider the following system of equations:
2x + 3y = 13 ...(Equation 1)
x - 2y = -4 ...(Equation 2)

--- Slide 9 ---

Solving Linear Equations: The Substitution Method
Step 1: Isolate a Variable
Choose one equation and solve it for one variable.
 It's often easiest to pick an equation where a variable already has a coefficient of 1 (or -1).
In our example, Equation 2 is easiest. Solving for x:
	x = 2y - 4 ...(Equation 3)
Step 2: Substitute
Substitute the expression you found (Equation 3) into the other equation (Equation 1). 
This will give you an equation with only one variable (y).
2(2y - 4) + 3y = 13
Step 3: Solve
Simplify and solve the resulting equation for the remaining variable.
4y - 8 + 3y = 13
7y - 8 = 13
7y = 21
y = 3
 Step 4: Back-Substitute
Substitute the value you found (y = 3) back into any of the original equations (or Equation 3). Equation 3 is often the easiest:
x = 2(3) – 4
x = 6 – 4
x = 2

--- Slide 10 ---

Solving Linear Equations: The Elimination Method
What is Elimination? 
Elimination involves manipulating equations so that when they are added or subtracted, one variable cancels out.This simplifies the system, allowing us to solve for the remaining variable.Think of it like strategically canceling terms in an algebraic expression to make it simpler.
Consider the system:

2x + 7y = 10 ...(Equation 1)
3x + y = 6 ...(Equation 2)

Notice that the y term in Equation 2 has a coefficient of 1. This makes it easy to eliminate.

--- Slide 11 ---

Solving Linear Equations: The Elimination Method
Step 1: Prepare for Elimination
Multiply one or both equations by constants so that the coefficients of one variable are opposites (or the same). 
Our goal is to make the coefficients of either x or y the same so we can add or subtract the equations to eliminate that variable.
Multiply Equation 2 by -7:
-21x - 7y = -42 ...(Equation 3)
Step 2: Eliminate

Add Equation 1 and Equation 3. 
Notice the y terms will cancel out.
(2x + 7y) + (-21x - 7y) = 10 + (-42)
-19x = -32

--- Slide 12 ---

Solving Linear Equations: The Elimination Method
Step 3: Solve

Solve the resulting equation for the remaining variable:
x = 32/19
Step 4: Back-Substitute

Substitute the value of x back into any of the original equations (Equation 1 or Equation 2) to solve for y. 
Equation 2 is often the easiest:
3(32/19) + y = 6
y = 6 - 96/19
y = 18/19
Solution
The solution is:
x = 32/19
y = 18/19
Always check your solution by substituting it back into the original equations!

--- Slide 13 ---

Solving Linear Equations: The Elimination Method
Step 3: Solve

Solve the resulting equation for the remaining variable:
x = 32/19
Step 4: Back-Substitute

Substitute the value of x back into any of the original equations (Equation 1 or Equation 2) to solve for y. 
Equation 2 is often the easiest:
3(32/19) + y = 6
y = 6 - 96/19
y = 18/19
Solution
The solution is:
x = 32/19
y = 18/19
Always check your solution by substituting it back into the original equations!

--- Slide 14 ---

Understanding Vector Addition and Scalar Multiplication
Learning Objectives:
Understand how to add vectors graphically and algebraically.
Learn the concept of scalar multiplication and how it scales a vector.
Visualize vector operations using Python.

--- Slide 15 ---

What is a Vector?
A vector is a quantity that has both magnitude and direction.

Represented as in 2D or in 3D

Used in physics, engineering, and computer graphics.

--- Slide 16 ---

Vector Addition
When adding two vectors of the same dimension, we combine their corresponding components. 
This can be visualized geometrically as placing the tail of the second vector at the head of the first vector; the resultant vector stretches from the tail of the first to the head of the second.
Mathematically:
u + v = [u₁, u₂, ..., uₙ] + [v₁, v₂, ..., vₙ] = [u₁+v₁, u₂+v₂, ..., uₙ+vₙ]

--- Slide 17 ---

Vector Addition
Implementation:

--- Slide 18 ---

Scalar Multiplication
Scalar multiplication involves multiplying a vector by a single number (a scalar).  This has the effect of scaling the vector's magnitude (length).  If the scalar is positive, the direction remains the same; if negative, the direction is reversed.
Mathematically: αv = α[v₁, v₂, ..., vₙ] = [αv₁, αv₂, ..., αvₙ]
Implementation:

--- Slide 19 ---

Visualization with Python

--- Slide 20 ---

Practical Implementation
Click here for the Code

--- Slide 21 ---

الشراكات العالمية

--- Slide 22 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 03

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Linear Algebra for Machine Learning

--- Slide 2 ---

Introduction to Linear Algebra
Fundamentals and Applications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Recall and explain the relationship between machine learning concepts and mathematical constructs like vectors and matrices.
Course Learning Outcomes:
Demonstrate a comprehensive understanding of key mathematical concepts, including linear algebra and probability, and their applications in AI and machine learning.

--- Slide 4 ---

Part 2: Learning Objectives
Calculate basic operations (dot product, modulus, negation) on vectors
Calculate a change of basis
Recall linear independence
Identify a linearly independent basis and relate this to the dimensionality of the space

--- Slide 5 ---

Dot Product of Vectors(Scalar Product)
The dot product of two vectors is a scalar value.
It measures how much the two vectors point in the same direction.
If u = [u₁, u₂, ..., uₙ] and v = [v₁, v₂, ..., vₙ],
	then u • v = u₁v₁ + u₂v₂ + ... + uₙvₙ.
 





Also, u • v = |u| |v| cos(θ), where θ is the angle between the vectors
.

--- Slide 6 ---

Dot Product of Vectors(Scalar Product)
.
Implementation

--- Slide 7 ---

Dot Product of Vectors Visualization
The dot product of two vectors:

 u=[1,2] and V=[3,4] is  11 

as shown at the right

--- Slide 8 ---

Modulus (Magnitude) of a Vector
The Euclidean norm measures the magnitude (length) of a vector. 
It is useful in optimization and distance computations in Machine Learning.

--- Slide 9 ---

Visualizationof a Vector  (Magnitude)
import numpy as np
v = np.array([3, 4])//The np.array() function is used to create a NumPy array from a list of values. In this case, the list [3, 4] represents a 2-dimensional vector (or a point in 2D space).

result = np.linalg.norm(v)//This line calculates the magnitude (or Euclidean norm, or length) of the vector v using the np.linalg.norm() function. np.linalg is a submodule within NumPy that provides linear algebra functions, and norm() is the function for calculating vector norms.
print(result)// 5

--- Slide 10 ---

Vector Negation
Vector Negation
The negation of a vector reverses its direction.
All components of the vector are multiplied by -1.
If v = [v₁, v₂, ..., vₙ], then -v = [-v₁, -v₂, ..., -vₙ].

Example: If v = [2, -1, 3], then -v = [-2, 1, -3].

--- Slide 11 ---

Vector Negation
Vector Negation
The negation of a vector reverses its direction.
All components of the vector are multiplied by -1.
If v = [v₁, v₂, ..., vₙ], then -v = [-v₁, -v₂, ..., -vₙ].

Example: If v = [2, -1, 3], then -v = [-2, 1, -3].

--- Slide 12 ---

Basis of a Vector Space
What is a Basis?
A basis of a vector space is a set of linearly independent vectors that span the entire space.
Any vector in the space can be uniquely expressed as a linear combination of the basis vectors.

--- Slide 13 ---

What is a Change of Basis?
A change of basis is the process of expressing the same vector or linear transformation in terms of a different basis.
Suppose we have two bases for a vector space:
Basis A: {a1,a2,…,an}
Basis B: {b1,b2,…,bn}
A vector v can be represented in terms of either basis A or basis B.

--- Slide 14 ---

Why Change Basis?
Simplification: Some problems are easier to solve in a specific basis.
Diagonalization: In machine learning and physics, changing to a basis where a matrix is diagonal simplifies computations.
Visualization: In computer graphics, changing the basis allows us to rotate, scale, or transform objects.
Dimensionality Reduction: Techniques like PCA (Principal Component Analysis) involve changing the basis to reduce the number of dimensions while preserving important information.

--- Slide 15 ---

How to Perform a Change of Basis
Let’s say we have a vector vv represented in basis A, and we want to represent it in basis B.
Step 1: Define the Bases
Let vA​ be the coordinates of v in basis A.
Let vB​ be the coordinates of v in basis B.

Step 2: Find the Change of Basis Matrix
The change of basis matrix P transforms coordinates from basis A to basis B.
To construct P, express each vector of basis A in terms of basis B:
P=[a1​​ a2 ​​…​an​​]Here, a1​,a2​,…,an​ are the basis vectors of A expressed in terms of basis B.

--- Slide 16 ---

How to Perform a Change of Basis
Step 3: Transform the Vector

--- Slide 17 ---

Applications of Change of Basis
Principal Component Analysis (PCA): Reduces dimensionality by projecting data onto a new basis of principal components.
Eigen Decomposition: Diagonalizes a matrix by changing to a basis of eigenvectors.
Computer Graphics: Transforms objects between coordinate systems (e.g., world coordinates to camera coordinates).
Quantum Mechanics: Changes the representation of quantum states.

--- Slide 18 ---

Key Takeaways
A basis is a set of linearly independent vectors that span a vector space.
Change of basis allows us to represent vectors or matrices in terms of a different basis.
The change of basis matrix P transforms coordinates from one basis to another.
Changing basis is useful for simplification, diagonalization, and dimensionality reduction.

--- Slide 19 ---

Linear independence
Linear independence is a fundamental concept in linear algebra that describes the relationship between vectors in a vector space. Let’s break it down step by step:

--- Slide 20 ---

Intuitive Explanation
Linear Independence: The vectors are "independent" in the sense that none of them can be constructed by scaling or adding the others.






Linear Dependence: At least one vector in the set is redundant because it can be expressed as a combination of the others.

--- Slide 21 ---

How to Check for Linear Independence
To determine whether a set of vectors is linearly independent:

--- Slide 22 ---

How to Check for Linear Independence
To determine whether a set of vectors is linearly independent:

--- Slide 23 ---

Geometric Interpretation
In R2:
Two vectors are linearly independent if they are not collinear (i.e., they do not lie on the same line).
Three or more vectors are always linearly dependent in R2.
In R3:
Three vectors are linearly independent if they do not lie in the same plane.
Four or more vectors are always linearly dependent in R3.

--- Slide 24 ---

Applications
Basis Selection: Linear independence is used to determine if a set of vectors can form a basis for a vector space.
Solving Systems of Equations: Linear independence helps determine if a system has a unique solution.

Machine Learning: Feature vectors in datasets must be linearly independent to avoid redundancy.

--- Slide 25 ---

How to Identify a Linearly Independent Basis
To identify a linearly independent basis for a vector space:

Start with a set of vectors that span the space.

Check for linear independence:
If the vectors are linearly independent, they form a basis.
If they are linearly dependent, remove redundant vectors until the remaining set is linearly independent.

--- Slide 26 ---

Example: Identifying a Basis in R3
Step 1: Start with a Set of Vectors
Consider the following vectors in R3:




Step 2: Check for Linear Independence
Set up the equation:
c1​v1​+c2​v2​+c3​v3​=0
This gives:

--- Slide 27 ---

Example: Identifying a Basis in R3

--- Slide 28 ---

Example: Identifying a Basis in R3Step 3: Remove Redundant VectorsSince v3​=v1​+v2​, we can remove v3​. The remaining vectors v1​ and v2​ are linearly independent and span the subspace of R3 where the third component is 0.Step 4: Identify the BasisThe set {v1​,v2​} is a basis for the subspace of R3 where the third component is 0. The dimension of this subspace is 2.

--- Slide 29 ---

Relating Basis to DimensionalityThe number of vectors in a basis equals the dimension of the space.For example:In R2, any basis has 2 vectors, and the dimension is 2.In R3, any basis has 3 vectors, and the dimension is 3.In a subspace, the dimension is the number of vectors in its basis.

--- Slide 30 ---

Summary
Basis: A set of linearly independent vectors that span a space.
Linearly Independent Basis: Ensures that no vector is redundant.
Dimensionality: Defined by the number of basis vectors.
Change of Basis: Transforming vector coordinates from one basis to another.
Applications: Graphics, Physics, Machine Learning.

--- Slide 31 ---

References
Strang, G. (2016). Introduction to Linear Algebra. Wellesley-Cambridge Press.
Lay, D. C. (2019). Linear Algebra and Its Applications. Pearson.
NumPy Documentation: https://numpy.org/doc/
Matplotlib Animation Guide: https://matplotlib.org/stable/api/animation_api.html

--- Slide 32 ---

الشراكات العالمية

--- Slide 33 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 04

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Linear Algebra for Machine Learning

--- Slide 2 ---

Introduction to Linear Algebra
Fundamentals and Applications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Recall and explain the relationship between machine learning concepts and mathematical constructs like vectors and matrices.
Course Learning Outcomes:
Demonstrate a comprehensive understanding of key mathematical concepts, including linear algebra and probability, and their applications in AI and machine learning.

--- Slide 4 ---

Understanding Matrices and Their Role in Transformations
Learning Objectives
Define what a matrix is.
Understand how matrices represent transformations.
Explore different types of transformations using matrices.
Visualize matrix operations with examples.
Implement matrix transformations in Python.

--- Slide 5 ---

What is a Matrix?

--- Slide 6 ---

Matrices as Transformations

--- Slide 7 ---

Transformations of Matrices

--- Slide 8 ---

Transformations of Matrices

--- Slide 9 ---

Applications
Where are Transformations Used?

Computer graphics (games, movies)
Robotics
Image processing
Physics (e.g., changes of coordinates)
Machine learning (e.g., PCA)

--- Slide 10 ---

Understanding Inverse and Determinant of Matrices
Matrices play a crucial role in linear algebra, engineering, physics, and computer science. 
Two important operations associated with matrices are the determinant and the inverse of a matrix. These properties help solve systems of linear equations, perform transformations, and analyze mathematical models.

--- Slide 11 ---

Determinant of a Matrix
Definition:
The determinant is a scalar value derived from a square matrix that provides important insights into the properties of the matrix.
Key Properties:
* A matrix with a determinant of zero is singular and does not have an inverse.
* The determinant can be used to determine if a system of linear equations has a unique solution.
* Determinants help in computing eigenvalues, volume scaling, and transformations.

--- Slide 12 ---

Formula for 2×2 and 3×3 Matrices:

--- Slide 13 ---

Determinant for 2×2 Matrices in Python
This line creates a 2 X2 NumPy array named A.
This line creates a 3 X3 NumPy array named B.
np.linalg is a submodule within NumPy that provides linear algebra functions. 
det() is the function specifically for calculating determinants.

--- Slide 14 ---

Inverse of a Matrix

--- Slide 15 ---

Identity Matrix
The identity matrix is a special square matrix (a matrix with the same number of rows and columns) that has the following properties:
Ones on the Diagonal: All the elements on the main diagonal (from the top-left corner to the bottom-right corner) are 1.   
Zeros Elsewhere: All the other elements (not on the main diagonal) are 0.

--- Slide 16 ---

Calculating the Inverse of a 2x2 Matrix

--- Slide 17 ---

Inverse for 2×2 Matrices in Python
This line creates a 2x2 NumPy array (matrix) named A with the given values.
This line calculates the determinant of matrix A using np.linalg.det(A). The determinant is a scalar value that provides information about the matrix. A non-zero determinant is a crucial condition for a matrix to be invertible
this line calculates the inverse of matrix A using np.linalg.inv(A)

--- Slide 18 ---

What Goes Wrong When Finding Inverses?
Non-Square Matrices: Only square matrices can have inverses.

Zero Determinant: If det(A)=0, the matrix is singular (no inverse).

Numerical Instability:Near-singular matrices (very small determinants) can lead to inaccurate results.

Computational Errors:Rounding errors in floating-point arithmetic.

--- Slide 19 ---

Applications of Determinants and Inverses
Solving Linear Systems: Used to solve equations using Cramer's rule and matrix inversion.

Computer Graphics: Used in transformations like scaling, rotation, and perspective projection.

Cryptography: Inverses of matrices play a role in encoding and decoding messages.

Physics & Engineering: Used in simulations, robotics, and structural analysis.

--- Slide 20 ---

الشراكات العالمية

--- Slide 21 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 05

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Linear Algebra for Machine Learning

--- Slide 2 ---

Introduction to Linear Algebra
Fundamentals and Applications
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Recall and explain the relationship between machine learning concepts and mathematical constructs like vectors and matrices.
Course Learning Outcomes:
Demonstrate a comprehensive understanding of key mathematical concepts, including linear algebra and probability, and their applications in AI and machine learning.

--- Slide 4 ---

Learning Objectives
Identify matrices as operators
Relate the transformation matrix to a set of new basis vectors
Formulate code for mappings based on these transformation matrices
Write code to find an orthonormal basis set computationally

--- Slide 5 ---

Understanding Matrices as Operators

--- Slide 6 ---

Matrices as Transformations

--- Slide 7 ---

Matrices as Transformations

--- Slide 8 ---

Practice Problems

--- Slide 9 ---

Practice Problems

--- Slide 10 ---

Practice Problems

--- Slide 11 ---

Relating the Transformation Matrix to a Set of New Basis Vectors

--- Slide 12 ---

Transformation Matrices and Basis Change

--- Slide 13 ---

References
Strang, G. (2016). Introduction to Linear Algebra. Wellesley-Cambridge Press.
NumPy Documentation: https://numpy.org/doc/
Matplotlib Guide: https://matplotlib.org/stable/contents.html

--- Slide 14 ---

الشراكات العالمية

--- Slide 15 ---

شــــــكــــرًا لكــــــم
THANK YOU

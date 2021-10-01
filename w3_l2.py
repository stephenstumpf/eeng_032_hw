"""
Problem: solve equations with numpy.

Author: Capt Stephen Stumpf
Date: 2021
Inputs: none.
Outputs: script will display answers to problems 1 and 2.
"""

### Python 101: Homework
### By Evelyn J. Boettcher
### Week 3 Lesson 2: Solving Equations


### Solving Linear equations

### Solve the following with numpy.
### Find the two angles.
### Problem 1

### a + b = 180
### b = 5x - 22
### b = 8x + 46

### Let A be composed of column vectors a, b, x.

if __name__=="__main__":
    import numpy as np
    A = np.array([[1, 1, 0], [0, 1, -5], [0, 1, -8]])
    B = np.array([[180], [-22], [46]])
    vars = np.linalg.solve(A, B)
    print("Angle a = %0.1f; angle b = %0.1f; x = %0.1f" % tuple(vars))

### Angle a = 315.3; angle b = -135.3; x = -22.7


### Problem 2

### a + b = 180
### a = 2x+1
### b = 3x-31 

### Let A be composed of column vectors a, b, x.

if __name__=="__main__":
    import numpy as np
    A = np.array([[1, 1, 0], [1, 0, -2], [0, 1, -3]])
    B = np.array([[180], [1], [-31]])
    vars = np.linalg.solve(A, B)
    print("Angle a = %0.1f; angle b = %0.1f; x = %0.1f" % tuple(vars))

### Angle a = 85.0; angle b = 95.0; x = 42.0

### Problem 3
### What is the difference between .dot() and @ in python's numpy math functions

### .dot() performs a dot product between two arrays of any dimension; its behavior depends on the dimension of the
### function inputs. On the other hand, "@" is an operator that performs multiplication between two 2-D arrays only.

### Problem 4
### Read 15.4 General Linear Least Squares from chapter 15 of Numerical_recipes_chap15.pdf
### [Numerical Recipes in C](http://s3.amazonaws.com/nrbook.com/book_C210.html)
### * with focus on Solution by Use of Singular Value Decomposition



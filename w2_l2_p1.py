# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 2

## Problems
### 1

import numpy as np
a = np.arange(16, 100000, 4)
b = a.reshape(2083, 12)
for i in range(3):
    print(b[i,:])
for j in range(3):
    print(b[-j-1,:])
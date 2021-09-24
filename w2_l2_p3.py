# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 2

## Problems
### 3


def solve_w2l2p3():
    import numpy as np
    A = np.ones(5);
    B = A
    B = B * 5 # "creates" new B, doesn't change A
    print(A) # behold, A is unchanged
    
    A = np.ones(5)
    B = A
    B.__imul__(5) # uses built-in method __imul__ to change itself - doesn't create new B!
    print(A) # behold, A IS changed

if __name__ == "__main__":
    solve_w2l2p3()

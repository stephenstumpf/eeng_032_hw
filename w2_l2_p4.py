# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 2

## Problems
### 4

### take the mode of the data in A 


def solve_w2l2p4():
    import numpy as np
    import pandas as pd
    A = np.ones(5);
    B = A
    B = B * 5 # "creates" new B, doesn't change A
    print(A) # behold, A is unchanged
    mode1 = pd.DataFrame(A).mode()
    print(mode1)
    
    A = np.ones(5)
    B = A
    B.__imul__(5) # uses built-in method __imul__ to change itself - doesn't create new B!
    print(A) # behold, A IS changed
    mode2 = pd.DataFrame(A).mode()
    print(mode2)

if __name__ == "__main__":
    solve_w2l2p4()

# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 2

## Problems
### 5

### read in a CSV but use dtype 'U5" for the header


def solve_w2l2p5():
    import numpy as np
    filenm = '.\ASPN----CUB_0--PAYLOAD_PIXHAWK--10020--ALTITUDE.csv'
    
    data = np.genfromtxt(filenm, delimiter=",", skip_header = 1)
    headers = np.genfromtxt(filenm, delimiter=",", max_rows=1, dtype='U5')
    headers[10]
    data[:, 10]
    for h, col in zip(headers, data.T):
        if h=='altitude':
            print('altitude', col.mean())
            
    data = np.genfromtxt(filenm,delimiter=',', skip_header=1,names=headers.tolist())
    print(data.dtype.names)
    print(data['altit'].mean())

if __name__ == "__main__":
    solve_w2l2p5()

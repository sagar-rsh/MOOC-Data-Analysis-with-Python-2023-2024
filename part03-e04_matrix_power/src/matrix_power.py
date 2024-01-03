#!/usr/bin/env python3
import numpy as np
from functools import reduce
# import numpy.linalg

def matrix_power(a, n):
    # if n >= 0:
    #     return reduce(np.matmul, (a for _ in range(n) ), np.eye(a.shape[0]))
    # else:
    #     inv = np.linalg.inv(a)
    #     return reduce(np.matmul, (inv for _ in range(-n) ))

    if n == 0:
        return np.eye(a.shape[0], dtype= int)
    
    if n>0:
        mat_gen = (a for i in range(n))
        return reduce(lambda x,y: x@y, mat_gen)
    
    elif n <0:
        inv_mat = np.linalg.inv(a)
        mat_gen = (inv_mat for i in range(abs(n)))
        return reduce(lambda x,y: x@y, mat_gen)
    

def main():
    np.random.seed(2)
    a = np.random.randint(0, 10, (2,2))
    n = -2
    print(f"a: {a}")
    print(f"Expected result: {np.linalg.matrix_power(a, n)}")
    print(f"Result: {matrix_power(a, n)}")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    num = np.sum(X*Y, axis=1)
    denom = scipy.linalg.norm(X, axis=1) * scipy.linalg.norm(Y, axis=1)
    cos = num/denom
    # print("cos: ", cos)
    inv_cos = np.rad2deg(np.arccos(np.clip(cos, a_min=-1.0, a_max=1.0)))

    return inv_cos


def main():
    # np.random.seed(0)
    # a=np.random.randint(-50, 50, (4,5))
    # b=np.random.randint(-30, 30, (4,5))
    a = np.array([[ 0 ,0 ,1], [-1 ,1 ,0]])
    b = np.array([[ 0 ,1 ,0], [1 ,1 ,0]])

    print("a: ", a)
    print("b: ", b)

    print(vector_angles(a,b))



if __name__ == "__main__":
    main()

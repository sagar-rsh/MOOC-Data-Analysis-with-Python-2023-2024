#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    plt.subplot(1,2,1)
    plt.plot(a[:, 0], a[:, 1])
    plt.subplot(1,2,2)
    plt.scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()

def main():
    np.random.seed(0)
    a = np.random.randint(1,100, (4,4))
    print(a)
    subfigures(a)


if __name__ == "__main__":
    main()

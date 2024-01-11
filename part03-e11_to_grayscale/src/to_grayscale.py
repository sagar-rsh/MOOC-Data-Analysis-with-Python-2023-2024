#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    # w=np.array([0.2126, 0.7152, 0.0722]).reshape(1, 1, 3)
    # a = image * w
    # return a.sum(axis=2)
  r = img[:,:,0]
  g = img[:,:,1]
  b = img[:,:,2]

  return 0.2126*r + 0.7152*g + 0.0722*b

def to_red(img):
  img_red = np.copy(img)
  img_red[:,:,1:] = 0
  return img_red

def to_green(img):
  img_green = np.copy(img)
  img_green[:,:,[0,2]] = 0
  return img_green

def to_blue(img):
  img_blue = np.copy(img)
  img_blue[:,:,0:2] = 0
  return img_blue

def main():
    img = plt.imread("src/painting.png")
    plt.gray()
    plt.imshow(to_grayscale(img))

    _, axes = plt.subplots(3,1)
    axes[0].imshow(to_red(img))
    axes[1].imshow(to_green(img))
    axes[2].imshow(to_blue(img))
    plt.show()

if __name__ == "__main__":
    main()

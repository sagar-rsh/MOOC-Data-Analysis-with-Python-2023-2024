#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, param1):
        self.start = param1
    
    def write(self, s):
        print(self.start + s)

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()

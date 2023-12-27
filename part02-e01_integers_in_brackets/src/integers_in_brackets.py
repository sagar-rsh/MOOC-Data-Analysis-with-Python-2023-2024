#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    int_list = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    if not int_list:
        return []

    return list(map(int, int_list))

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()

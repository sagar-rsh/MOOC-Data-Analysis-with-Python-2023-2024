#!/usr/bin/env python3
import re

def file_extensions(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    no_ext = []
    dict_ext = dict()
    for line in lines:
        line = line.strip("\n")
        ext = re.search(r"(.*)\.(.*)", line)
        if ext and ext.group(2):
            try:
                dict_ext[ext.group(2)].append(ext.group(0))
            except KeyError:
                dict_ext[ext.group(2)] = []
                dict_ext[ext.group(2)].append(ext.group(0))
        else:
            no_ext.append(line)


    return (no_ext, dict_ext)

def main():
    no_ext, dict_ext = file_extensions("src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for key in dict_ext:
        print(key, len(dict_ext[key]))

if __name__ == "__main__":
    main()

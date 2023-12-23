#!/usr/bin/env python3

def merge(L1, L2):
    if not L1 and not L2:
        return []
    
    merged_list = []
    L1_idx, L2_idx = 0, 0

    while L1_idx < len(L1) and L2_idx < len(L2):
        print(L1_idx, L2_idx)
        if L1[L1_idx] < L2[L2_idx]:
            merged_list.append(L1[L1_idx])
            L1_idx+=1
        else:
            merged_list.append(L2[L2_idx])
            L2_idx+=1

    if L1_idx >= len(L1):
        merged_list.extend(L2[L2_idx:])
    if L2_idx >= len(L2):
        merged_list.extend(L1[L1_idx:])
    
    return merged_list

def main():
    print(merge([1,4,5,7,10], [2,4,6,7,8]))

if __name__ == "__main__":
    main()

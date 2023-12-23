#!/usr/bin/env python3

def detect_ranges(L):
    result = sorted(L)
    range_list = []
    final_result = []
    streak, streak_start = 1, 0

    for idx in range(len(result)):
        if idx + 1 >= len(result):
            break
        if result[idx] + 1 != result[idx + 1]:
            range_list.append((streak_start, streak_start + streak))
            streak_start = idx + 1
            streak = 1

        elif result[idx] + 1 == result[idx+1]:
            streak+=1
        else:
            streak_start = idx

    range_list.append((streak_start, streak_start + streak))

    # print(result)
    # print(range_list)
    for i in range_list:
        if i[1] - i[0] > 1:
            final_result.append((result[i[0]], result[i[1] - 1] + 1))
        else:
            final_result.append(result[i[0]])

    return final_result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

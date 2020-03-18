"""Determines the longest zigzag sequence in a sequence"""

def longestZigZag(seq):
    """Returns the longest zigzag sequence for a list of ints"""
    if len(seq) == 1:
        return 1

    zz_len = [1]*len(seq)
    if seq[0] != seq[1]:
        zz_len[1] = 2

    i = 2
    while i < len(seq):
        j = i - 1
        while j > 0:
            k = j - 1
            while k > -1:
                if seq[i] == seq[j] and zz_len[i] < zz_len[j]:
                    zz_len[i] = zz_len[j]
                elif seq[i] > seq[j] and zz_len[i] <= zz_len[j]:
                    if seq[k] > seq[j] and zz_len[k] == zz_len[j] - 1:
                        zz_len[i] = zz_len[j] + 1
                    elif zz_len[i] == 1:
                        zz_len[i] = 2
                elif seq[i] < seq[j] and zz_len[i] <= zz_len[j]:
                    if seq[k] < seq[j] and zz_len[k] == zz_len[j] - 1:
                        zz_len[i] = zz_len[j] + 1
                    elif zz_len[i] == 1:
                        zz_len[i] = 2
                k -= 1
            j -= 1
        i += 1
    print(zz_len)
    return max(zz_len)


assert longestZigZag([1, 7, 4, 9, 2, 5]) == 6
assert longestZigZag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
assert longestZigZag([44]) == 1
assert longestZigZag([40, 40]) == 1
assert longestZigZag([40, 40, 40, 40, 40, 40, 40]) == 1
assert longestZigZag([1, 3, 1]) == 3
assert longestZigZag([3, 1, 3]) == 3
assert longestZigZag([3, 1]) == 2
assert longestZigZag([70, 55, 13]) == 2
assert longestZigZag([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5,
                      5, 1000, 32, 32]) == 8
assert longestZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
                      600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
                      67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
                      477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
                      249, 22, 176, 279, 23, 22, 617, 462, 459, 244]) == 36

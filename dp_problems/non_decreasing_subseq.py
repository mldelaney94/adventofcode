"""Finds the longest 'non-decreasing' subsequence in a seq of numbers 1 - N"""

import random

random_list = random.sample(range(0, 1000), 1000)
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subseq_len = 1

i = 1
for index, num in enumerate(test_list):
    if index > 0:
        if num >= test_list[index-1]:
            i += 1
            if i > subseq_len:
                subseq_len = i
        else:
            i = 0

print(subseq_len)

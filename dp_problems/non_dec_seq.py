"""Finds the longest 'non-decreasing' sequence in a seq of numbers 1 - N"""

import random

seq = random.sample(range(0, 1000), 1000)
placeholder = [5, 3, 4, 8, 6, 7]
seq_len = [1]*len(seq)

i = 1
while i < len(seq):
    j = i - 1
    while j > -1:
        if seq[i] >= seq[j] and seq_len[j] >= seq_len[i]:
            seq_len[i] = seq_len[j] + 1
            if j < seq_len[i]:
                break
        j -= 1
    i += 1

print (max(seq_len))

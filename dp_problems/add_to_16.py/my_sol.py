""" takes in a +ve integer list and returns number of subsets of numbers that
add up to 16
"""

def find_16(S, n):
    if n == 0:
        return 1

    init_subsets = set()
    all_subsets = set()
    for ele in S:
        ele_set = frozenset([ele])
        if ele_set not in init_subsets:
            init_subsets.add(ele_set)
        for subset in init_subsets:


    print(all_subsets)
    return len(S)

assert find_16([2, 4, 6, 10], 16) == 2

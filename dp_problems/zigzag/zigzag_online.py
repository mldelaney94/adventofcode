def longestZigZag(arr):
    n = len(arr)

    '''Z[i][0] = Length of the longest Zig-Zag subsequence
        ending at index i and last element is greater
        than its previous element
    Z[i][1] = Length of the longest Zig-Zag subsequence
        ending at index i and last element is smaller
        than its previous element '''
    Z = [[1 for i in range(2)] for i in range(n)]


    res = 1 # Initialize result

    # Compute values in bottom up manner '''
    for i in range(1, n):

        # Consider all elements as previous of arr[i]
        for j in range(i):

            # If arr[i] is greater, then check with Z[j][1]
            if (arr[j] < arr[i] and Z[i][0] < Z[j][1] + 1):
                Z[i][0] = Z[j][1] + 1

            # If arr[i] is smaller, then check with Z[j][0]
            if( arr[j] > arr[i] and Z[i][1] < Z[j][0] + 1):
                Z[i][1] = Z[j][0] + 1

        # Pick maximum of both values at index i ''' 
        if (res < max(Z[i][0], Z[i][1])):
            res = max(Z[i][0], Z[i][1])

    return res

# Driver Code
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

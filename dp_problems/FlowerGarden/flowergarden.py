def block(curr_bloom, curr_wilt, compare_bloom, compare_wilt):
    if curr_wilt < compare_bloom or curr_bloom > compare_wilt:
        return False
    return True

def getOrdering(height, bloom, wilt):
    garden = []
    bhw = []
    bhw += zip(height, bloom, wilt)
    bhw.sort()
    for flower in bhw:
        gIndex = len(garden)
        while gIndex > 0 and not block(flower[1], flower[2], garden[gIndex-1][1],
                                       garden[gIndex-1][2]):
            gIndex -= 1
        garden[gIndex:gIndex] = [flower]
    
    garden = [i[0] for i in garden]

    return garden

assert getOrdering([3,2,5,4], [1,2,11,10], [4,3,12,13]) == [4,5,2,3]
assert getOrdering([1,2,3,4,5,6],[1,3,1,3,1,3],[2,4,2,4,2,4]) == [2,4,6,1,3,5]
assert getOrdering([5,4,3,2,1],[1,1,1,1,1],[365,365,365,365,365]) == [1,2,3,4,5]

import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)
    
    reveresed_nums = []
    while heap:
        pair = heapq.heappop(heap)
        reveresed_nums.append(pair[1])
    return reveresed_nums



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))


"""
[5, 6, -4, 2, 4, 7, -3, -1]
-4, -3, -1, 2, 4, 5, 6, 7
7, 6, 5, 4, 2, -1, -2, -3, -4 

5, -5
6, -6
-4, 4
2, -2
4, -4
7, -7
-3, 3
-1, 1

"""
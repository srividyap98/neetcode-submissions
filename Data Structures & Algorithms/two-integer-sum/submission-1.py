class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, a in enumerate(nums):
            difference = target - a
            if difference in hashmap:
                return[hashmap[difference], i]
            hashmap[a] = i




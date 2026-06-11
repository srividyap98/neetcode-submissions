class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums and target 
        # nums[i] + nums[j] == target and i! = j

        hashmap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [min(i, hashmap[diff]), max(i, hashmap[diff])]
            else:
                hashmap[n] = i 
        return []
            




        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j and nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]
        return []

        """

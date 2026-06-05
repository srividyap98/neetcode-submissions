class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        # check every element and store the largest element 
        # largest_integer < curr 
        # largest_int = curr 
        # brute force?    






        largest_int = -1


        for i in nums:
            if i <= largest_int or nums.count(i) > 1:
                continue
            largest_int = i
        
        return largest_int

        
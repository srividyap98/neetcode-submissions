class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        # check every element and store the largest element 
        # largest_integer < curr 
        # largest_int = curr 
        # brute force?

        hashmap = {}
        largest_int = -1


        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else: 
                hashmap[n] = 1
            
        for i in hashmap:
            if i <= largest_int or hashmap[i] != 1:
                continue
            largest_int = i
        
        return largest_int
        




        """

        largest_int = -1


        for i in nums:
            if i <= largest_int or nums.count(i) > 1:
                continue
            largest_int = i
        
        return largest_int
        """
        
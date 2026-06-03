class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #if nums1[i] = x if x is in nums2 give index of nums1

        hashmap = {}
        my_list = []

        for i,n in enumerate(nums2):
            hashmap[n] = i

        
        for i,n in enumerate(nums1):
            if n in hashmap:
                my_list.append(hashmap[n])
        return my_list
        



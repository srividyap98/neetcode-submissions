class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #if nums1[i] = x if x is in nums2 give index of nums2

        my_list = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    my_list.append(j)
                    break
        
        return my_list
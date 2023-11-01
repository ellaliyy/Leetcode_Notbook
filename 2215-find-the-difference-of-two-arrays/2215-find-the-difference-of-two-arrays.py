class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
 
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
    
        in_1_not_2 = set_nums1 - set_nums2  # Elements in nums1 but not in nums2
        in_2_not_1 = set_nums2 - set_nums1  # Elements in nums2 but not in nums1
    
        ans = [list(in_1_not_2), list(in_2_not_1)]
    
        return ans

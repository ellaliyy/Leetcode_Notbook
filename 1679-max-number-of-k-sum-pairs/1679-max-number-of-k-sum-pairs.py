class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1
        
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                ans += 1
                left += 1
                right -= 1
            
            elif cur < k:
                left += 1
            else:
                right -= 1
                
        return ans
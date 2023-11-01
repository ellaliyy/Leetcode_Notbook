class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        counts = {0:0, 1:0}
        
        for i, num in enumerate(nums):
            counts[num] += 1
            
            while counts[0] > 1:
                if nums[left] == 0:
                    counts[0] -= 1
                left += 1
                
            current_len = i - left
            #it is not (i-left+1) as usual because we have to exclude the deleted 0
            
            ans = max(ans, current_len)
            
        return ans
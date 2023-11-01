class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Task: To find the longest subarray (a continuous portion of the array) that has 1's. If there are 0's in this subarray, you can flip some or all of them to 1s, but the total number of flipped 0s should not exceed k.
        
        left = 0
        ans = 0
        counts = {0:0, 1:0} 
        #initializes a dictionary called counts.
        # This dictionary has two keys, 0 and 1, 
        # and both of their associated values are initially set to 0
        
        for right, num in enumerate(nums):
            
            counts[num] += 1
            
            while counts[0] > k: 
    #checks if the number of zeros in the current window (counts[0]) exceeds k. 
    #If it does, the window isn't valid, so we need to shrink it from the left.
               
               counts[nums[left]] -= 1
               left += 1
            
            curr_window_size = right - left + 1
            ans = max(ans, curr_window_size)
        
        return ans
             
                
            
        
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[0:k])
        maxx = sums
        
        for i in range(k, len(nums)):
            sums += nums[i] - nums[i-k]
            maxx = max(maxx, sums)
           
        return float(maxx)/k
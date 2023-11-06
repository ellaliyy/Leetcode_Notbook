class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set_arr = set(arr)
        
        counts = []
        
        for cur in set_arr:
            count = 0
            for j in range(len(arr)):
                if arr[j] == cur:
                    count += 1
            counts.append(count)
        
        set_counts = set(counts)
        
        if len(set_counts) == len(counts):
            return True
        else:
            return False
            
            
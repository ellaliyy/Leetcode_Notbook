class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        count = 0
        i =  0
        while i < len(flowerbed):
    
            #first check if the plot is empty
            if flowerbed[i] == 0:
              ## Check if previous and next spots are also empty or if we're at the boundaries
                if(i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    #then we can plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    i += 2 #because next plot can't plant flower anymore
                    
              ## if not satisfy above condition, then we check next plot
                else:
                    i += 1
                    
            #if the current plot is not empty, then next plot can't plant flower 
            else:
                i += 2
         
        
        if count >= n:
            return True

    
##Note:
# in line16, we should put i == 0 and i = len - 1 before indexing to avoid index out of range.
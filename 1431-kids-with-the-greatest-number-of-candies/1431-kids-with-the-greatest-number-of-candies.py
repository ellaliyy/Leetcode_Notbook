class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = []
        max_candies = max(candies)
        
        for i in range(len(candies)):
            candies_inhand = candies[i] + extraCandies
            
            if candies_inhand >= max_candies:
                n.append(True)
            else:
                n.append(False)
        
        return n
        
#Notes:
#The len(candies) function returns an integer representing the length, not a interval
#So we can't use 'len(candies)' directly in for loop
# we should use 'for i in range(len(candies))'

#we need to define 
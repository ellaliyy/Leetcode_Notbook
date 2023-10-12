class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = []
        
        for i in range(len(candies)):
            candies_inhand = candies[i] + extraCandies
            
            if candies_inhand >= max(candies):
                n.append(True)
            else:
                n.append(False)
        
        return n
        
#Notes:
#The len(candies) function returns an integer representing the length, not a interval
#So we can't use 'len(candies)' directly in for loop
# we should use 'for i in range(len(candies))'

#we need to use Python's built-in boolean values True and False to make the result a boolean array.
#If we use 'TRUE', "FALSE" if we want the elements all strings

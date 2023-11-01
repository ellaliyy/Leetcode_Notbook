from fractions import gcd

class Solution(object):
    import math
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        m = len(str1)
        n = len(str2)
        len_gcd = gcd(m,n)
        
        #first, check if these two strings are the same
        if str1 == str2:
            return str1
        
        #then check if they have no common factor, if so, then we reject it
        elif (str1 + str2) != (str2 + str1):
            return ""
        
        else:
            return(str1[:len_gcd])
            
    
### Side Note:
# /--is the divide operator, e.g. 7/3=2.33333
# // --- is the "floor division" operator, it rounds down the division into nearest integer

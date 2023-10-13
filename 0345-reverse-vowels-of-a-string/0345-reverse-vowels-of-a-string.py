class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU' #define a string
        
        while left < right:
            if s[left] in m and s[right] in m:
                s[left], s[right] = s[right], s[left]
                left += 1 
                right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
        return ''.join(s)

# Note:
# strings in Python are immutable, which means you cannot modify them after they are created
# so we cannot swap location of elements in a string
# therefore we have to change the str s into a list 
# and then change s back to string using ''.join(s) in the end
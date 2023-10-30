class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        
        current_vowels = 0
        max_vowels = 0
        
        for i, v in enumerate(s):
            
        #Removing the leftmost character of the previous window if the window has moved past it
            if i >= k:
                if s[i-k] in vowels:
                    current_vowels -= 1
                #s[i-k] gets the leftmost character of the previous window.
            
            if s[i] in vowels:
                current_vowels += 1
            
            max_vowels = max(current_vowels, max_vowels)
            
        return max_vowels
                
                
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # pointer for s
        j = 0  # pointer for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # if the characters match, move the pointer for s
                i += 1
            j += 1  # if doesn't match, move the pointer for t 
        return i == len(s)  #it will return T or F, which is r!
    # if i has reached the end of s, s is a subsequence of t, else not
    
          
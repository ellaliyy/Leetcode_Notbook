from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # (a) word1 and word2 have the same set of distinct characters
        # (b) the collection of counts for distinct characters for word1 and word2 are identical. 
        # (The counts for the same letter do not have to be equal, however.)
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if set(word1) == set(word2) and sorted(c1.values()) == sorted(c2.values()):
            return True
        else:
            return False
        
        
        
        
        
        
        
            
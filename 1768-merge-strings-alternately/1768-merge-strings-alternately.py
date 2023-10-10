class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        merged_word = []

        while i < m or j < n:
            if i < m:
               merged_word.append(word1[i])
            if j < n:
               merged_word.append(word2[j])
            i += 1
            j += 1
        return "".join(merged_word)

#we need to return a string but here merged_word is a list
#we use "".join(list) here to join together the elements of the list into a #single string
        
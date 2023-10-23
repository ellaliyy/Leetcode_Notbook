class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        l.reverse()
        return ' '.join(l)
        
        
#The split() method without any arguments splits a string based on whitespace. Multiple spaces will be treated as a single delimiter. This means that words separated by multiple spaces will still be split correctly

#reverse() Reverses the order of the words in the list

## ' '.join() Joins the words in the list back into a string, separated by spaces
#Note: we have to add the ' ' to get the returned string seperated by spaces,
#"".join(l) will get returned reversed string without spaces between words.



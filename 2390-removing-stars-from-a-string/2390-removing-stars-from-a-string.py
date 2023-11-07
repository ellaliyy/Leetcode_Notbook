class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  # Create a stack to hold non-star characters

        for char in s: 
            if char == "*":   # When we see a star, we pop (remove) the last non-star character
                if stack: #Check if the stack is not empty, return True if it's not empty
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
            
            
     
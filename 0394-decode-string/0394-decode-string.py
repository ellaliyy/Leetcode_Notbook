class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        current_num = 0
        current_str = ''
        
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                current_num = current_num * 10 + int(c)
                
            # If the character is an opening bracket, push the current number and current string onto the stack
            elif c == '[':
                stack.append(current_str)
                stack.append(current_num)
                #reset these two values
                current_str, current_num = '', 0
                
             # If the character is a closing bracket, 
             # repeat the popped characters and push the result back onto the stack
            elif c == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + current_str *prev_num
            
            # If the character is a letter, append it to the current string
            else:
                current_str += c
        return current_str
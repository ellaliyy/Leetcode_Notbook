class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        
        while i < len(asteroids):
            cur = asteroids[i]
            
            if stack and stack[-1] > 0 and cur < 0:
                if abs(cur) > stack[-1]: # stack[-1] exploded but cur remains and compare with new top element
                    stack.pop()
                    continue
                elif abs(cur) == stack[-1]: # both exploded, move to next element in asteroids
                    stack.pop()
                    i += 1
                else:
                    i += 1
            else:
                stack.append(cur)
                i += 1
        return stack
                
                
                
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        #we use read to iterate through all the elements in chars
        #use write to keep track of the number of elements in the re-wrote list "chars"
        
        while read < len(chars):
            ch = chars[read]
            count = 0
            
            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1
            
            chars[write] = ch
            #rewrite the chars with new elements
            write += 1 #num of elements +1
            
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            
            
        return write
            
            
                
            
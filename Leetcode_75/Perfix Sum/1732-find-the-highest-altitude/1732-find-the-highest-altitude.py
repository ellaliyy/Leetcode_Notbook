class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude_list = [0]
        
        for i in range(len(gain)):
            altitude_list.append(altitude_list[i] + gain[i])
            
        return max(altitude_list)
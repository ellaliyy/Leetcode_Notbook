class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rest = []
        
        acc = 1
        #first we get the product of all the elemets that are in the left side of ith element
        for num in nums:
            rest.append(acc) #first element in rest is always 1 because the product of all the elements on the left side for the 1st element is 1
            acc *= num
            
        #now reset acc to 1 and calculate the right side
        acc = 1 
        for i in reversed(range(len(nums))):
            rest[i] *= acc #first i is the last element in nums, and we time acc=1 since the product of all the elements on the right side for the last element is 1
            acc *= nums[i]
        
        return rest
        

        
#for i in reversed(range(len(nums))): print(i) --- we got 3,2,1,0


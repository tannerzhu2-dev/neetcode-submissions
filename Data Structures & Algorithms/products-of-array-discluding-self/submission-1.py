class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix: product of all values before i
        #postfix: product of all values after i
        #output: prefix[i - 1] * postfix[i + 1] 

        """
        For the opotized version: default value of the start point (pre-fix)
                                  default value of the end point (post-fix)
                                  both starts at 1
        """
        
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # start, stop, step
            result[i] *= postfix
            postfix *= nums[i]

        return result


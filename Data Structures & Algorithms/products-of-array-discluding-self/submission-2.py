class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        # remember the prefix and suffix
        # prefix at index[0] = 1
        # suffix at index[-1] = 1

        output[0] = 1

        #for prefix
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]


        # for suffix 
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]
            
        return output
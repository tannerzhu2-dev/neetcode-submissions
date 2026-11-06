class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output is an array
        # create a for loop
            # inside that loop I created a hashmap
            # insert that vlaue into output[i]
        output = []
        total = 1
        for n in nums:
            total *= n

        for i in range(len(nums)):
            if nums[i] == 0:
                # Handle division by zero
                product = 1
                for j in range(len(nums)):
                    if j != i:
                        product *= nums[j]
                output.append(product)

            else:
                output.append(total // nums[i])

        return output
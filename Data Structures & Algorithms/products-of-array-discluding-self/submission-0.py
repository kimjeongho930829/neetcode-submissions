class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            sum = 1

            for j in range(len(nums)):
                if i != j:
                    sum *= nums[j]
            
            result.append(sum)
        
        return result


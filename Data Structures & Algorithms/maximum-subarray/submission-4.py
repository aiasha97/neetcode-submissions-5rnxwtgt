class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        res, cur = nums[0], 0

        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            res = max(res, cur)
        
        return res
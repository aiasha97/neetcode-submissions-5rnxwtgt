class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force solution
        if len(nums) == 1:
            return nums[0]

        n, res = len(nums), nums[0]

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        
        return res


        
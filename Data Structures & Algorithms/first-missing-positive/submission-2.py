class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 1

        for n in nums:
            if n > 0 and n == res:
                res += 1
        
        return res

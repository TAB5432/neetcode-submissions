class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, nums[0]

        for n in nums:
            if n == res:
                count += 1
            else:
                count -= 1
                if count < 0:
                    res = n
        
        return res
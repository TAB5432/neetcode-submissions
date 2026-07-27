class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev_step = 0

        for i in range(len(nums) - 1):
            step = nums[i+1] - nums[i]
            
            if step == 0:
                continue
            
            if prev_step != 0 and (step > 0) != (prev_step > 0):
                return False
            
            prev_step = step
        
        return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = {} #n:i

        for i, n in enumerate(nums):
            if n in nums_set.keys():
                if abs(i - nums_set[n]) <= k:
                    return True
                else:
                    nums_set[n] = i
            else:
                nums_set[n] = i
        return False
                

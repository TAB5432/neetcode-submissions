class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixes = []
        prefixes = []

        curr_prefix = 1
        for n in nums:
            prefixes.append(curr_prefix)
            curr_prefix *= n
        
        curr_suffix = 1
        for n in nums[::-1]:
            suffixes.insert(0, curr_suffix)
            curr_suffix *= n
        
        res = []
        for index, n in enumerate(nums):
            res.append(suffixes[index] * prefixes[index])
        
        return res


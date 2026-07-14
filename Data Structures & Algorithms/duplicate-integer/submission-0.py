class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = []

        for n in nums:
            if n in elements:
                return True
            else:
                elements.append(n)
        
        return False
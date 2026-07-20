class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        #find split
        l, r = 0, n-1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m

        split = l

        #search right side
        l, r = split, n-1

        while l <= r:
            m = (l+r) // 2
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                return m
        
        #search left side
        l, r = 0, split-1

        while l <= r:
            m = (l+r) // 2
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                return m
        
        return -1



        

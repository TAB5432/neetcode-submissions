class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n - 1
        max_left = height[l]
        max_right = height[r]

        total_water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(height[l], max_left)

                total_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(height[r], max_right)

                total_water += max_right - height[r]
        
        return total_water
            
        
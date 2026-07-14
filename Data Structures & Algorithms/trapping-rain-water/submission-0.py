class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        prefix[0] = height[0]
        for i in range(1, len(height) - 1):
            prefix[i] = max(prefix[i-1], height[i])
        
        suffix[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) -2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        sum = 0
        for i in range(len(height)):
            area_at_point = min(suffix[i], prefix[i]) - height[i]
            if area_at_point > 0:
                sum += area_at_point
        
        return sum

            
        
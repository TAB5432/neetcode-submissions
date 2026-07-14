class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        res = 0
        while i < j:
            height = min(heights[i], heights[j])
            area = height * (j-i)
            
            if area > res:
                res = area
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return res
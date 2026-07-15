class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #h, i pairs

        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                stackH, stackI = stack.pop()
                max_area = max(max_area, stackH * (i-stackI))
                start = stackI
        
            stack.append((h, start))
        
        for h, i in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r  = 1, max(piles)

        minK = max(piles)
        while l <= r:
            k = (l+r) // 2
            i = 0
            
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            
            if total_hours > h:
                l = k+1
            else:
                r = k-1
                minK = min(k, minK)
        
        return minK
            

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = l + (r-l) // 2

            curr_day, curr_cap = 1, mid
            for w in weights:
                if (curr_cap - w) >= 0:
                    curr_cap -= w
                else:
                    curr_day += 1
                    curr_cap = mid - w
            
            if curr_day <= days:
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        
        return res
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = (l+r) // 2
            m_square = m ** 2

            if m_square < x:
                l = m+1
                res = m
            elif m_square > x:
                r = m-1
            else:
                return m
        return res
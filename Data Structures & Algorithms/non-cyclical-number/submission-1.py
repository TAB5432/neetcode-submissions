class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(n):
            s = 0
            while n:
                s += (n % 10) ** 2
                n //= 10
            
            return s

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_squares(n)
            if n == 1:
                return True
        
        return False
        


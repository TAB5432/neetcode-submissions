class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(n):
            s = 0
            while n:
                s += (n % 10) ** 2
                n //= 10
            
            return s

        slow, fast = n, sum_squares(n)

        while slow != fast:
            fast = sum_squares(sum_squares(fast))
            slow = sum_squares(slow)
        
        if fast == 1:
            return True
        
        return False
        


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ""

        while n > 26:
            res += chr((n % 26) + 64)
            n = n // 26
        
        res += chr(n+64)
        
        return res[::-1]
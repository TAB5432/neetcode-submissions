class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def hcf(num1, num2):
            a = max(num1, num2)
            b = min(num1, num2)

            r = a % b
            while r != 0:
                a = b
                b = r
                r = a % b
            return b



        if str1 + str2 == str2 + str1:
            factor = hcf(len(str1), len(str2))
            return str1[:factor]

        return ""

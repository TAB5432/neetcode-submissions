class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()


        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in s:
            if not i in chars:
                s = s.replace(i, "")
        print(s)
        print(s[::-1])
        if s == s[::-1]:
            return True
        else:
            return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1)
        for l in range(len(s2) - len(s1)+1):
            if sorted(s1) == sorted(s2[l:r]):
                return True
            r += 1
        
        return False


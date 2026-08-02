class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i= 0
        min_len = min(len(word1), len(word2))

        res = ""

        while i < min_len:
            res += word1[i]
            res += word2[i]
            i += 1

        if len(word1) > len(word2):
            res+= word1[i:]
        elif len(word2) > len(word1):
            res += word2[i:]
        
        return res

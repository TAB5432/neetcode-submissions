class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            if res in s:
                continue
            else:
                while res not in s and res != "":
                    res = res[:-1]
        
        return res
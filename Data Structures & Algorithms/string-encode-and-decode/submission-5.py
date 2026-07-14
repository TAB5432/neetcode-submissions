class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for index, s in enumerate(strs):
            res += "ç"
            res += s
            if index == len(strs) - 1:
                res = res[1:]
                res += "ç"
                break
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""
        for l in s:
            if l == "ç":
                res.append(curr)
                curr = ""
            else:
                curr += l
        return res
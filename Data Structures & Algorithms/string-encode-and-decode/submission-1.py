class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += i
            string += " ||"
        return string 

    def decode(self, s: str) -> List[str]:
        strs = s.split(" ||")
        return strs[0:len(strs) - 1]
        


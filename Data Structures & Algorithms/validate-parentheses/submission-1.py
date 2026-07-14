class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                if stack and bracket_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False


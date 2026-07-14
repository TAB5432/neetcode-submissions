class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t in "+-*/":
                print(nums)
                if t == "+":
                    nums[-2] = nums[-2] + nums[-1]
                elif t == "-":
                    nums[-2] = nums[-2] - nums[-1]
                elif t == "*":
                    nums[-2] = nums[-2] * nums[-1]
                elif t == "/":
                    nums[-2] = int(nums[-2] / nums[-1])
                nums.pop()
            else:
                nums.append(int(t))
        
        return nums[-1]
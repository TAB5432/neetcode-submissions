class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict()

        for n in nums:
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1
        
        return max(count, key=count.get)
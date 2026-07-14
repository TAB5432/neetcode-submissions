class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numbers = {
            #number: no_times
            
        }

        ans = []

        for num in nums:
            numbers[num] = 1 + numbers.get(num, 0)
        print(numbers)

        while k > 0:
            ans.append(max(numbers, key=numbers.get))
            numbers.pop(max(numbers, key=numbers.get))
            k -= 1;
        return ans
            






        
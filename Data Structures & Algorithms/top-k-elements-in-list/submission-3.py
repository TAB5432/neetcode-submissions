class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_copy = nums
        output = [] #num: freq

        while k > 0:
            hashmap = {}
            for n in nums_copy:
                if n in hashmap.keys():
                    hashmap[n] += 1
                else:
                    hashmap[n] = 1

            most_freq = [-1, -1] #num, freq
            for n in hashmap.keys():
                if hashmap[n] > most_freq[1]:
                    most_freq[1] = hashmap[n]
                    most_freq[0] = n

            output.append(most_freq[0])
            nums_copy = [n for n in nums_copy if n != most_freq[0]]
            k -= 1
        
        return output


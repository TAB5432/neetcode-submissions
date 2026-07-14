class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best_count = 0

        for n in num_set:
            if (n-1) not in num_set:
                curr_num = n
                curr_count = 1

                while (curr_num + 1) in num_set:
                    curr_num += 1 
                    curr_count += 1
                
                best_count = max(best_count, curr_count)
        
        return best_count
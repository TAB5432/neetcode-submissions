class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #anagram: [indicies]

        for index, s in enumerate(strs):
            s_sorted = str(sorted(s))
            if s_sorted in anagrams.keys():
                anagrams[s_sorted].append(index)
            else:
                anagrams[s_sorted] = [index] 
        
        result = []
        for val in anagrams.keys():
            words = []
            for i in anagrams[val]:
                words.append(strs[i])
            result.append(words)
        
        return result
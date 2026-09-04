class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            right_letter = ord(s2[r]) - ord("a")
            
            if s2_count[right_letter] == s1_count[right_letter]:
                matches -= 1

            s2_count[right_letter] += 1

            if s2_count[right_letter] == s1_count[right_letter]:
                matches += 1
            
            left_letter = ord(s2[l]) - ord("a")
            
            if s2_count[left_letter] == s1_count[left_letter]:
                matches -= 1

            s2_count[left_letter] -= 1

            if s2_count[left_letter] == s1_count[left_letter]:
                matches += 1
            
            l+=1

        return matches == 26
            


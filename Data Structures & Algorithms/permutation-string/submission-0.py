class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        base = ord('a')

        for i, ch in enumerate(s1):
            need[ord(ch) - base] += 1
            window[ord(s2[i]) - base] += 1
        
        match = sum(1 for i in range(26) if need[i] == window[i])
        if match == 26:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            add = ord(s2[right]) - base
            if window[add] == need[add]:
                match -= 1
            window[add] += 1
            if window[add] == need[add]:
                match += 1
            
            remove = ord(s2[left]) - base
            if window[remove] == need[remove]:
                match -= 1
            window[remove] -= 1
            if window[remove] == need[remove]:
                match += 1            
            left += 1
            
            if match == 26:
                return True

            
        return False
            

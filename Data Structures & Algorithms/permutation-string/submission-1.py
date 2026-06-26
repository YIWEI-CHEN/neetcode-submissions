"""
sliding window len(s1) for s2 checking
char frequency
26 lower case, counts[26] for s1, sliding window of s2
c1 == c2 for all char --> match
matches == 26 
each step, remove left, add right, update counts, matches
Time: O(len(s1) + len(s2))
Space: O(26 * 2) = O(1)
edge case:
|s1| > |s2| --> False
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1, count2 = [0] * 26, [0] * 26
        base = ord('a')
        # char freq in s1
        for i, c in enumerate(s1):
            count1[ord(c) - base] += 1
            count2[ord(s2[i]) - base] += 1
        # check 26 letter counts
        matches = sum(1 for i in range(26) if count1[i] == count2[i])
        if matches == 26:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            # add right char in s2 window
            add = ord(s2[right]) - base
            if count1[add] == count2[add]:
                matches -= 1
            count2[add] += 1
            if count1[add] == count2[add]:
                matches += 1

            # remove left char in s2 window
            remove = ord(s2[left]) - base
            if count2[remove] == count1[remove]:
                matches -= 1
            count2[remove] -= 1
            if count2[remove] == count1[remove]:
                matches += 1
            
            if matches == 26:
                return True
            
            left += 1
        return False

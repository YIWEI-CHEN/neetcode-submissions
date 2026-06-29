from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagram: char freq -> 26-count as hash key
        group by key: compute word's char freq tuple, append the word to that group
            -> defaultdict(list), 26-count as key, append the word to the same key
        Time: O(total char); Space: O(total char)
        """
        base = ord('a')
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - base] += 1
            groups[tuple(counts)].append(word)
        
        return list(groups.values())
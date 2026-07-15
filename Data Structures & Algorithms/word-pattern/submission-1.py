class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        1. restate problem
        2. maintain two hash map
        ab vs [dog, dog], dog to a, or b
        3. check len of pattern same as len(words in s), return False
        4. words and pattern, scan, check any violation return false, otherwise true.
        5. Time O(n), where n is len of pattern/words; Space O(n)
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        
        # two hash maps
        ch_to_w = {}
        w_to_ch = {}

        for ch, word in zip(pattern, words):
            if ch in ch_to_w and ch_to_w[ch] != word:
                return False
            if word in w_to_ch and w_to_ch[word] != ch:
                return False
            
            ch_to_w[ch] = word
            w_to_ch[word] = ch
        
        return True
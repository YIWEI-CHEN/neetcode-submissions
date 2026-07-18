class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        """
        a = "red"
        b = "blue"
        a b a b -> red blue red blue
        redblueredblue
        ans = True

        a -> r
          - re
          - red
          - redb
         
        substring boudaries are unknown

        backtracking approach, choose, explore, unchoose

        pattern_idx, str_idx
        backtrack(pattern_idx, str_idx)
        """

        char_to_str = {}
        used = set()

        def backtrack(pattern_idx, str_idx):
            # base success case
            if pattern_idx == len(pattern) and str_idx == len(s):
                return True
            if pattern_idx == len(pattern) or str_idx == len(s):
                return False
            
            ch = pattern[pattern_idx]
            if ch in char_to_str:
                word = char_to_str[ch]
                if not s.startswith(word, str_idx):
                    return False
                return backtrack(pattern_idx + 1, str_idx + len(word))
            
            for end in range(str_idx + 1, len(s) + 1):
                candidate = s[str_idx: end]
                if candidate in used:
                    continue
                
                # choose
                char_to_str[ch] = candidate
                used.add(candidate)

                # explore
                if backtrack(pattern_idx + 1, end):
                    return True
                
                # unchoose
                used.remove(candidate)
                del char_to_str[ch]

            return False
        
        return backtrack(0, 0)
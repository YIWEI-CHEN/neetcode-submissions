class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        reachable = [False] * (len(s) + 1)
        reachable[0] = True

        for start in range(len(s)):
            if not reachable[start]:
                continue
            
            for word in wordDict:
                end = start + len(word)
                if s.startswith(word, start) and end <= len(s):
                    reachable[end] = True
        
        return reachable[-1]

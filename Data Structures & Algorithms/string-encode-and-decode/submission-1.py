class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        1. encoding format = "length#text"
        2. `#` in the text, but length can avoid confusing
        3. time O(total char); space O(total char)
        """
        parts = []
        for text in strs:
            parts.append(f"{len(text)}#{text}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        # pointer of s
        i = 0

        # 5#hello
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            res.append(s[start:start + length])
            i = start + length
        
        return res



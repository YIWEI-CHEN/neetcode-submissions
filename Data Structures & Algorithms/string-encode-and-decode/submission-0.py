class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        1. hello -> 5#hello, where 5 is length of hello
        2. although encoded str might have `#`, length could avoid the # confusing
        """
        parts = []
        for text in strs:
            parts.append(f'{len(text)}#{text}')
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res


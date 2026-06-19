class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        """
        1. find the max words in a line
        2. fill with spaces with selected words to get final line
            2.1 fill space evenly for all gaps. Extra space is filled from left to right
            2.2 a line have 1 word, "a _ _ _" or last line "a b c _", Fill up spaces at the end
        3. return all lines
        """
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # j point to the next word after inner while loop
            words_line = words[i:j]
            words_len = sum(len(word) for word in words_line)
            gaps = len(words_line) - 1

            # 2.2: gaps = 0, the line has 1 word; j == len(words), this is the last line
            if j == len(words) or gaps == 0:
                line = " ".join(words_line)
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - words_len
                # quotient, remainder = divmod()
                base_spaces, extra = divmod(spaces, gaps)
                parts = []
                for k, word in enumerate(words_line[:-1]):
                    parts.append(word)
                    parts.append(" " * (base_spaces + (1 if k < extra else 0)))
                parts.append(words_line[-1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res
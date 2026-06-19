class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            # line = w1 + w2 .. + wj
            line_len = len(words[i])
            j = i + 1

            # find wi to wj, total line length is less than maxWidth
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len = line_len + 1 + len(words[j])
                j += 1

            selected_words = words[i:j]
            gaps = len(selected_words) - 1
            total_words_len = sum(len(w) for w in selected_words)

            # create the final line by filling with spaces
            # last word gaps = 0, or last line: j == len(words)
            if gaps == 0 or j == len(words):
                line = " ".join(selected_words)
                line += " " * (maxWidth - len(line))
            else:
                allowed_spaces = maxWidth - total_words_len
                base_space, extra = divmod(allowed_spaces, gaps)
                parts = []
                for k, w in enumerate(selected_words[:-1]):
                    parts.append(w)
                    parts.append(" " * (base_space + (1 if k < extra else 0)))
                parts.append(selected_words[-1])
                line = "".join(parts)

            res.append(line)
            i = j
        return res
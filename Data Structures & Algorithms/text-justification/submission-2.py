class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        1. pack words greediy
            each line, add words line length <= maxWidth
            maxWidth = 16
            words = ["This","is","an","example","of","text","justification."]
            This: line_len = 4
            This is: line_len = 4 + 1 + 2 = 7
            ...
            ... justification line_len = 27 > maxWidth <-- stop
        2. space distribution 
            total space, gap, space size for each gap, extra spaces distribute them left to right
            divmod = (a//b, a%b)
            word_len = 10 (for three words)
            total_space = 16 - 10 = 6
            gaps = 3 - 1 = 2
            gap_size = 6 // 2 = 3
            extra = 6 % 2 = 0 -> even space

            word_len = 11 (3 words)
            total_space = 5
            gaps = 2; gap_size = 2, extra = 5 % 2 = 1
            w1 _ _ _ w2 _ _ w3
                   ^       
                   |
                   extra
        3. edge case
           1. line with one word
              w1 _ _ _ _
           2. last line with w1, w2, w3
             w1, w2, w3, _ _ _
            
        4. Time: O(total char) Space: O(maxWidth for line numbers) = O(output)

        """
        # pack word greedily
        i = 0
        res = []
        while i < len(words):
            j = i + 1
            line_len = len(words[i])
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            # j stop at the next word that exceed maxWidth
            selected_words = words[i:j]
            words_len = sum(len(w) for w in selected_words)
            spaces = maxWidth - words_len
            gaps = len(selected_words) - 1

            # distribute space correctly
            # edge cases: last line or one word in a line
            if j == len(words) or gaps == 0:
                line = ' '.join(selected_words)
                space_size = maxWidth - len(line)
                line += ' ' * space_size
            else:
                space_size, extra = divmod(spaces, gaps)
                line = selected_words[0]
                for idx, word in enumerate(selected_words[1:]):
                    if idx < extra:
                        line += ' ' * (space_size + 1)
                    else:
                        line += ' ' * space_size
                    line += word
            res.append(line)
            i = j
        return res

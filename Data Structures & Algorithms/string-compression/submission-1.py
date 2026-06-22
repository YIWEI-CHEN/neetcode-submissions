class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        1. read pointer for current scanned position; write pointer for the position to write
        2. Time: O(n)
        3. Space: O(1)
        """
        read, write = 0, 0
        while read < len(chars):
            char = chars[read]
            start = read
            while read < len(chars) and chars[read] == char:
                read += 1  # the loop will stop the next char that != char
            
            count = read - start
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write

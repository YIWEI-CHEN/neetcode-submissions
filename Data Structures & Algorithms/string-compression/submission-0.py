class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        1. Do not use Counter, since it cannot remember group order. ['a', 'a', 'b', 'a']. Counter will confuse
        2. In-place change `chars`, ['a', 'a', 'b', 'a'] -> ['a', '2', 'b', 'a']
        3. create two pointers for current read and write positions
        4. ['a', ... 'a', 'b', 'a'] ->  ['a', '1', '0', ..., 'a'], we need to count digits
        """
        read, write = 0, 0
        
        while read < len(chars):
            char = chars[read]
            i = read + 1
            while i < len(chars) and chars[i] == char:
                i += 1
            
            # i stops at the next char, ['a', 'a', 'b'], i = 2
            count = i - read

            # write to original char list
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            read = i
        
        return write

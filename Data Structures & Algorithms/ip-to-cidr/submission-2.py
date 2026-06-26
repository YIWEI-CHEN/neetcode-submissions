"""
CIDR
1. prefix, power of 2
2. start address a multiple of the block size
255.0.0.8/29, block size = 32 - 29 = 3, power(2, 3) = 8,
255.0.0.8 is a multiple of block size 8
greedy: max block size now, low CIDR block number
bit trick: start & -start -> lowest set bit
start 255.0.0.8 -> 11111111 00000000 00000000 00001000
&
-start ->          00000000 11111111 11111111 11111000
                   00000000 00000000 00000000 00001000
            
"""
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # ip (str) -> int
        # lowest set bit, 
        # prefix
        # int -> ip (str)/prefix
        res = []
        start = self._to_int(ip)

        while n > 0:
            max_size = start & -start
            # edge case: 0 & -0 = 0; meaning whole ip ranges
            if max_size == 0:
                max_size = 1 << 31

            while max_size > n:
                # halving max_size
                max_size >>= 1

            # exponent of max_size
            prefix = 32 - (max_size.bit_length() - 1)
            res.append(f"{self._to_ip(start)}/{prefix}")

            # remaining counts
            n -= max_size
            start += max_size
        
        return res
    
    def _to_int(self, ip: str) -> int:
        val = 0
        for part in ip.split('.'):
            val = val * 256 + int(part)
        return val


    def _to_ip(self, val: int) -> str:
        parts = []
        for shift in (24, 16, 8, 0):
            parts.append(str(val >> shift & 255))
        return '.'.join(parts)

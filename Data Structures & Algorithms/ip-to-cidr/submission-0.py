class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # ip to int
        start = self.to_int(ip)
        res = []

        while n > 0:
            # start      = 00001000
            # ~start     = 11110111
            # ~start + 1 = 11111000 (-start)
            # start & -start = 00001000 
            # -> we will get the largest number, power of 2, and start is divisible by
            max_block = start & -start
            # max_block == 0, it can accomodate 2^32 ips
            if max_block == 0:
                max_block = 1 << 32


            while max_block > n:
                max_block >>= 1
            
            prefix = 32 - (max_block.bit_length() - 1)
            res.append(f"{self.to_ip(start)}/{prefix}")

            n -= max_block
            start += max_block
        
        return res

    def to_int(self, ip: str) -> int:
        res = 0
        for value in ip.split('.'):
            res = res * 256 + int(value)
        return res

    def to_ip(self, val: int) -> str:
        res = []
        for shift in (24, 16, 8, 0):
            res.append(str((val >> shift) & 255))
        return ".".join(res)
        

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        start = self.to_int(ip)
        blocks = []
        while n > 0:
            max_size = start & -start
            if max_size == 0:
                max_size = 1 << 32
            
            while max_size > n:
                max_size >>= 1
            
            prefix = 32 - (max_size.bit_length() - 1)
            blocks.append(f"{self.to_ip(start)}/{prefix}")

            n -= max_size
            start += max_size

        return blocks

    def to_int(self, ip: str) -> int:
        value = 0
        for part in ip.split('.'):
            value = value * 256 + int(part)
        return value
    
    def to_ip(self, value: int) -> str:
        res = []
        for shift in (24, 16, 8, 0):
            res.append(str((value >> shift) & 255))
        return ".".join(res)

        
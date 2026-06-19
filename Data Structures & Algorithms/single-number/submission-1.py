class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR property
        a ^ a = 0
        a ^ 0 = a
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans

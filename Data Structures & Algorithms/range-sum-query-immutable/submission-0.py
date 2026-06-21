class NumArray:

    def __init__(self, nums: List[int]):
        """
        1. prefix sum, prefix[i], the first i-th element sum
        """
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)
        

    def sumRange(self, left: int, right: int) -> int:
        """
        1. idx i means (i+1)-th elements
        2. to get sum(nums[l:r]), all sums of the first (r+1) elements - the first (l) element
            eg: sum(nums[1:3]) = num[1] + num[2] + num[3] = sum of first 4 elemnets -  sum of first num 
        3. space = o(n), time = o(1)
        """
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
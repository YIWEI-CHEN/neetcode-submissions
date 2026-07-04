from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. val in nums1 -> positions i nums2.
        2. postions mapping for nums2
        nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
        positions = {50:[0], 12:[1], 32:[2], 46:[3], 28:[4]}
        res = [1, 4, 3, 2, 0]
        3. Time: O(n) Space: O(n)
        """
        positions = defaultdict(list)  # for nums2
        for i, val in enumerate(nums2):
            positions[val].append(i)
        res = []
        for val in nums1:
            """
            pop is helpful: we can use position once
            e.g, [12, 12] in nums1, [12, 12] nums2 -> res=[0, 1] better than [0, 0]
            [0, 0] is acceptable
            """
            res.append(positions[val].pop())  
        return res

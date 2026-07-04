from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = defaultdict(list)

        for idx, n in enumerate(nums2):
            indices[n].append(idx)
        
        res = []
        for n in nums1:
            res.append(indices[n][0])
        
        return res
        
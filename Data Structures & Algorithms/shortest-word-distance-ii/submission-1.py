from collections import defaultdict

class WordDistance:
    """
    1. save word idx in ascending order. 
      since word might appear more than once, I use defaultdict(list) to keep all index
    2. For the shortest dist, compare the idx lists of the two words. 
        two pointers to each list, keep the best by iterating them.
    3. Time: O(n) for init; O(|l1| + |l2|) for shortest
    4. Space: O(n) for init; O(1) for shortest
    """

    def __init__(self, wordsDict: List[str]):
        self.word_idx_lists = defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.word_idx_lists[w].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.word_idx_lists[word1], self.word_idx_lists[word2]
        i = j = 0
        best = float('inf')

        while i < len(l1) and j < len(l2):
            best = min(best, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        
        return best



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

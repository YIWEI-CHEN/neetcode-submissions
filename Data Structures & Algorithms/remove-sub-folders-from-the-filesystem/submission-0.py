class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        sort folder list in ascending order
        ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        Time: O(nlogn)
        Space: O(output)
        """
        folder.sort()
        result = []

        for path in folder:
          if result and path.startswith(result[-1] + "/"):
            continue
          result.append(path)
        return result
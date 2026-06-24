class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        1. sort folder, parent, sub-folder, e.g, /a, /a/b
        2. after sorting, iterate folder, startswith '/a' + /
        3. / is needed, /ab is wrongly to be a subfolder /a
        4. time: o(nlogn) for sort, total char
        5. space: o(output)
        """
        ans = []
        folder.sort()

        for path in folder:
          if ans and path.startswith(ans[-1] + '/'):
            continue
          ans.append(path)
        
        return ans

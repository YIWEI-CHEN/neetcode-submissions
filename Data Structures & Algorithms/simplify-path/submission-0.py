class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        four cases
        1. '..', go up one level
        2. '.' current folder
        3. '//' empty with multiple slash
        4. normal dir names, '...' is also valid name

        stack natural fit, '..', what pop does. dir name -> push; '..' -> pop

        path = "/neetcode/practice//...///../courses" 
        split path by '/' -> ['', neetcode, practice, '', ..., '', '', .., courses]
        '' -> skip
        neetcode, practice, course -> push
        ... -> push
        .. -> pop
        [neetcode, practice, course] -> '/'.join(stack)

        Time: O(n), n is length of path
        Space: O(n)
        """
        stack = []
        
        for part in path.split('/'):
            if part == '.' or part == '':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)

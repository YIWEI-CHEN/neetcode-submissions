class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        1. '.', current folder
        2. '..', go up one layer
        3. '//', empty dir name, keep '/'
        4. normal dir name, '...'

        split '/'

        '..', stack good fit, pop 

        '/a/aaa/.../..//' -> split on '/' -> '', a, aaa, ..., .., ''
        return '/' + '/'.join(stack)

        Time: O(n); Space: O(n)
        """
        stack = []
        for part in path.split('/'):
            if part == '.' or part == '':
                continue
            if part == '..':
                if stack:
                    # '/..'
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)
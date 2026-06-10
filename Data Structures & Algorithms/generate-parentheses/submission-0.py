class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backpack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                backpack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backpack(openN, closedN + 1)
                stack.pop()
        backpack(0, 0)
        return res
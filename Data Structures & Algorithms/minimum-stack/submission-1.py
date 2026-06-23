class MinStack:

    def __init__(self):
      self.stack = []

    def push(self, val: int) -> None:
      hist_min = self.stack[-1][1] if self.stack else val
      self.stack.append((val, min(val, hist_min)))

    def pop(self) -> None:
      """
      prev min in the stack, never lose tracks of his min.
      """
      self.stack.pop()

    def top(self) -> int:
      return self.stack[-1][0]
        

    def getMin(self) -> int:
      return self.stack[-1][1]

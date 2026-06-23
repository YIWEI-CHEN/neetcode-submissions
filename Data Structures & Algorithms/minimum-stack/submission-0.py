class MinStack:

    def __init__(self):
      # saving current and minimum val so far
      # (val, min)
      self.stack = []


    def push(self, val: int) -> None:
      cur_min = self.stack[-1][1] if self.stack else float('inf')
      self.stack.append((val, min(cur_min, val)))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
      return self.stack[-1][1]
        

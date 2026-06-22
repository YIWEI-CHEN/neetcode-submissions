class Excel:
    """
    1. row: 1, 2, .., 26; col: A, B, ...Z; cell coordinate, eg: A1 -> row 1 col A
        _cell to parse a cell to an coordinate
    2. values dict, (row, col) -> val, set by `set`; formulas, (row, col) -> freq of a cell range. used in `sum`
    3. since `sum` accept `A1:B2 + A1`, i create `Counter` to count {A1:2, B1:1, A2:1, B2:2}.
        The freq count is in `_parse`

    """
    from collections import Counter

    def __init__(self, height: int, width: str):
        self.values = {}
        self.formulas = {}

    def set(self, row: int, column: str, val: int) -> None:
        self.values[(row, column)] = val
        # clear a range of cells in formulas
        self.formulas.pop((row, column), None)

    def get(self, row: int, column: str) -> int:
        cell = (row, column)
        if cell not in self.formulas:
            # default cell val is 0
            return self.values.get(cell, 0)

        refs = self.formulas[cell]
        val = 0
        for ref, count in refs.items():
            val += self.get(ref[0], ref[1]) * count
        return val

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = (row, column)
        self.formulas[cell] = self._parse(numbers)
        # If that cell has a val, formulas does not work
        self.values.pop(cell, None)
        return self.get(row, column)
    
    def _parse(self, numbers: List[str]) -> Counter:
        refs = Counter()
        for token in numbers:
            if ':' not in token:  # pure cell, like A1
                refs[self._cell(token)] += 1
            else:
                # like A1:B2
                start, end = token.split(':')
                r1, c1 = self._cell(start)
                r2, c2 = self._cell(end)
                for r in range(r1, r2 + 1):
                    for c in range(ord(c1), ord(c2) + 1):
                        refs[(r, chr(c))] += 1
        return refs
        
    def _cell(self, name: str) -> (int, str):
        return int(name[1:]), name[0]  # row, col


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

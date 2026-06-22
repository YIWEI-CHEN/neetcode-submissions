from collections import Counter

class Excel:
    """
    1. cell: A1 -> row: int, `1`, col: str, `A`
    2. values: dict, cell (row, col), get val by `values.get((row, col))`. 
        Since a cell might save formula, pure mat does not handle two types of val.
        formulas: dict, formulas.get((row, col)), how this cell refer to other cells.
    3. formulas will save cell freq, like {A1:2, B1:1, A2:1, B2:1} for A1 + A1:B2. 
        `sum` can use the cell counts to get result
    """
    def __init__(self, height: int, width: str):
        self.values = {}
        self.formulas = {}        

    def set(self, row: int, column: str, val: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        cell = (row, column)
        self.values[cell] = val
        # clean a cell if it had a formula previously
        self.formulas.pop(cell, None)

    def get(self, row: int, column: str) -> int:
        """
        Time: O(R), R is the total number of touched cells that recursively expanded
        Space: O(D), D is the deepest formula chain
        """
        cell = (row, column)
        if cell not in self.formulas:
            # this is a pure value cell. default to 0
            return self.values.get(cell, 0)
        
        refs = self.formulas[cell] # cell -> count
        total = 0
        for ref, count in refs.items():
            # C1 = sum(A1, B1); D1 = sum(C1, B1). D1 needs recursively reference.
            total += self.get(ref[0], ref[1]) * count
        return total        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        """
        Time: O(P+R), P the number of expansions for all cell ranges
        R: total get recursively evalueation
        Space: O(P)
        """
        cell = (row, column)
        self.formulas[cell] = self._parse(numbers)
        self.values.pop(cell, None)  # remove cell in values to make formula work
        return self.get(row, column)
    
    def _parse(self, numbers: List[str]) -> Counter:
        refs = Counter()
        for token in numbers:
            if ":" not in token:  # A1
                refs[self._cell(token)] += 1
            else:
                start, end = token.split(':')
                r1, c1 = self._cell(start)
                r2, c2 = self._cell(end)
                for r in range(r1, r2 + 1):
                    for c in range(ord(c1), ord(c2) + 1):
                        refs[(r, chr(c))] += 1
        return refs
    
    def _cell(self, name: str) -> (int, str):
        # row: int, col: str
        return int(name[1:]), name[0]


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

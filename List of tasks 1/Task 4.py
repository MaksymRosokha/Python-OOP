class Matrix:
    def __init__(self, row, col, value = None):
        self._row = row
        self._col = col
        self._matrix = [[value for i in range(self._col)] for j in range(self._row)]

    def size(self):
        return (self._row, self._col)

    def _check_index(self, row, col):
        r,c = self.size()
        if 0 > row or row > r or 0 > col or col > c:
            raise IndexError

    def get_cell(self, row, col):
        try:
            self._check_index(row, col)
            return self._matrix[row][col]
        except IndexError:
            print("You entered an incorrect cell")
        return None

    def set_cell(self, row, col, value):
        try:
            self._check_index(row, col)
            self._matrix[row][col] = value
        except IndexError:
            print("You entered an incorrect cell")

    def __str__(self):
        return "\n".join(
            ["".join(f"{value}\t" for value in row) for row in self._matrix]
        )

if __name__ == "__main__":
    m = Matrix(2, 3, 0)
    m.set_cell(0, 0, 1)
    m.set_cell(0, 1, 2)
    m.set_cell(0, 2, 3)
    m.set_cell(1, 0, 4)
    m.set_cell(1, 1, 5)
    m.set_cell(1, 2, 6)

    print(m)

    print("\nElement (1,2):", m.get_cell(1, 2))
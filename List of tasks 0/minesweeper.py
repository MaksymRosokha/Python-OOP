import random

def ask_number(a, b, text):
    while True:
        try:
            n = int(input(f"{text} (number in the range [{a}, {b}]): "))
        except ValueError:
            print("It isn't a number")
        else:
            if a <= n <= b:
                return n
            else:
                print("the number must be within a specific range")


def place_mines(m, n, number_of_mines):
    assert number_of_mines <= m * n
    mines = set()
    while len(mines) < number_of_mines:
        mines.add((random.randrange(m), random.randrange(n)))

    return mines


def count_adjacent_mines(field, mines):
    i, j = field
    s = {(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
         (i, j - 1), (i, j + 1),
         (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)}
    count = 0
    # for x in s:
    # if x in mines:
    # count += 1
    return len(s & mines)


def create_board(n, m, mines, symbol_of_mines="*"):
    board = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i, j) in mines:
                row.append(symbol_of_mines)
            else:
                row.append(count_adjacent_mines((i, j), mines))
        board.append(row)

    return board


def reveal_cells(field, n, m, board, expose_fields):
    i, j = field
    # warunek stopu (gdy pza planszą lub odkryte to koniec)
    if not (0 <= i < n and 0 <= j < m) or (i, j) in expose_fields:
        return

    expose_fields.add((i, j))  # odkruwamy pole
    if board[i][j] != 0:
        return

    # rekurencyjne wywołanie dla 8 sąsiadów
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x, y) != (0, 0):
                reveal_cells((i + x, j + y), n, m, board, expose_fields)


def display_board(n, m, board, expose_fields, show_all=False):
    print("   ", end="")
    for j in range(m):
        print(f"{j:<3}", end="")
    print()

    for i in range(n):
        print(f"{i:<3}", end="")  # numer wiersza
        for j in range(m):
            if (i, j) in expose_fields or show_all:
                print(f"{board[i][j]:^3}", end="")
            else:
                print(f"{'#':^3}", end="")
        print()


def sapper():
    n = 10
    m = 10
    number_of_mines = 10
    mines = place_mines(n, m, number_of_mines)
    board = create_board(n, m, mines)
    expose_fields = set()

    print("=== Welcome to Sapper! ===")
    print("Uncover all fields without hitting a mine.")
    print("Enter coordinates as row and column numbers.\n")

    while True:
        display_board(n, m, board, expose_fields, False)

        row = ask_number(0, n - 1, "Enter row")
        col = ask_number(0, m - 1, "Enter column")

        if (row, col) in mines:
            print("\n💥 BOOM! You hit a mine. Game over.")
            display_board(n, m, board, expose_fields, show_all=True)
            break
        else:
            reveal_cells((row, col), n, m, board, expose_fields)

        if len(expose_fields) == n * m - number_of_mines:
            print("\n🎉 Congratulations! You won!")
            display_board(n, m, board, expose_fields, show_all=True)
            break


if __name__ == "__main__":
    sapper()
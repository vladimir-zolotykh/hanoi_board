from django.shortcuts import render


def transpose(pegs):
    n = len(pegs[0])
    res = [[None] * n, [None] * n, [None] * n]
    col = 0
    row = 0
    rev = reversed(pegs[0])
    for row in range(n):
        for col in range(3):
            if pegs[row]:
                res[row][col] = pegs[row][col]
            else:
                res[row][col] = None
    return res


def build_board(pegs, height):
    board = []

    for level in range(height - 1, -1, -1):
        row = []
        for peg in pegs:
            if len(peg) > level:
                row.append(peg[level])
            else:
                row.append(None)
        board.append(row)

    # fmt: off
    board = [
        [1, None, None],
        [2, None, None],
        [3, None, None]
    ]
    # fmt: on
    board = transpose(pegs)
    return board


def hanoi_view(request):
    pegs = [[3, 2, 1], [], []]

    height = 3
    board = build_board(pegs, height)

    return render(request, "hanoi_board_app/board.html", {"board": board})

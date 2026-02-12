from django.shortcuts import render


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

    return board


def hanoi_view(request):
    pegs = [[3, 2, 1], [], []]

    height = 3
    board = build_board(pegs, height)

    return render(request, "hanoi_board_app/board.html", {"board": board})

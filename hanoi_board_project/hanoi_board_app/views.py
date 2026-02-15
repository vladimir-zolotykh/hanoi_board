from django.shortcuts import render


def transpose(pegs):
    board = []
    npegs = len(pegs)  # number of pegs
    ndisks = len(pegs[0])  # number of disks
    for i in range(ndisks - 1, -1, -1):
        row = []
        for j in range(npegs):
            try:
                row.append(pegs[j][i])
            except IndexError:
                row.append(None)
        board.append(row)
    return board


def build_board(pegs, height):
    board = transpose(pegs)
    return board


def hanoi_view(request):
    pegs = [[3, 2, 1], [], []]

    height = 3
    board = build_board(pegs, height)

    return render(request, "hanoi_board_app/board.html", {"board": board})

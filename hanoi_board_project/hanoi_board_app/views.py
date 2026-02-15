from django.shortcuts import render


def transpose(pegs):
    # board = []
    # for i in range(2, -1, -1):
    #     row = []
    #     for j in range(3):
    #         try:
    #             row.append(pegs[j][i])
    #         except IndexError:
    #             row.append(None)
    #     board.append(row)

    # fmt: off
    board = [
        [pegs[0][2], None, None],
        [pegs[0][1], None, None],
        [pegs[0][0], None, None],
    ]
    # fmt: on
    return board


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

    board = transpose(pegs)
    return board


def hanoi_view(request):
    pegs = [[3, 2, 1], [], []]

    height = 3
    board = build_board(pegs, height)

    return render(request, "hanoi_board_app/board.html", {"board": board})

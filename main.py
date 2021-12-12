board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
active = "x"


def print_board(boar):
    for i in range(3):
        for j in range(3):
            print(boar[i][j], end=" ")
        print()


def mark_board(boar, pos, a_p):
    boar[pos // 3][pos % 3] = a_p


def check(boar, pos):
    if no_problem(boar, pos // 3, pos % 3):
        return True
    return False


def no_problem(boar, a, b):
    if boar[a][b] != "-":
        return False
    return True


def has_won(boar, a_p):
    for i in range(3):
        if boar[i][0] == boar[i][1] and boar[i][0] == boar[i][2] and boar[i][0] == a_p:
            return True
        if boar[0][i] == boar[1][i] and boar[0][i] == boar[2][i] and boar[0][i] == a_p:
            return True
    if boar[0][0] == boar[1][1] and boar[0][0] == boar[2][2] and boar[0][0] == a_p:
        return True
    if boar[2][0] == boar[1][1] and boar[2][0] == boar[0][2] and boar[2][0] == a_p:
        return True


has_won(board, "x")

while True:
    x = int(input("Enter Pos (1-9): ")) - 1
    if active == "x" and check(board, x):
        mark_board(board, x, active)
        print_board(board)
        if has_won(board, active):
            print(f"{active} has won!")
            break
        active = "o"

    elif active == "o" and check(board, x):
        mark_board(board, x, active)
        print_board(board)
        if has_won(board, active):
            print(f"{active} has won!")
            break
        active = "x"

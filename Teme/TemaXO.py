import random


GRID = [[None, None, None], [None, None, None], [None, None, None]]


def display_grid():
    for i in range(3):
        row = [x if x else " " for x in GRID[i]]
        print("|".join(row))


def write_grid(pos, sym):
    pos -= 1
    row = pos // 3
    col = pos - row * 3
    if not GRID[row][col]:
        GRID[row][col] = sym
    else:
        raise RuntimeError


def computer_move():
    second_choice = {2: GRID[0][1], 4: GRID[1][0], 6: GRID[1][2], 8: GRID[2][1]}
    third_choice = {1: GRID[0][0], 3: GRID[0][2], 7: GRID[2][0], 9: GRID[2][2]}
    if not GRID[1][1]:
        write_grid(5, "O")
    elif None in second_choice.values():
        available_moves = [key for key, value in second_choice.items() if not value]
        move = random.randint(0, len(available_moves) - 1)
        write_grid(available_moves[move], "O")
    elif None in third_choice.values():
        available_moves = [key for key, value in third_choice.items() if not value]
        move = random.randint(0, len(available_moves) - 1)
        write_grid(available_moves[move], "O")


def check_win():
    # Check if won on row
    if GRID[0][0] and GRID[0][0] == GRID[0][1] == GRID[0][2]:
        return True
    if GRID[1][0] and GRID[1][0] == GRID[1][1] == GRID[1][2]:
        return True
    if GRID[2][0] and GRID[2][0] == GRID[2][1] == GRID[2][2]:
        return True
    # Check if won on col
    if GRID[0][0] and GRID[0][0] == GRID[1][0] == GRID[2][0]:
        return True
    if GRID[0][1] and GRID[0][1] == GRID[1][1] == GRID[2][1]:
        return True
    if GRID[2][0] and GRID[0][2] == GRID[1][2] == GRID[2][2]:
        return True
    # Check if won on diagonals
    if GRID[0][0] and GRID[0][0] == GRID[1][1] == GRID[2][2]:
        return True
    if GRID[0][2] and GRID[0][2] == GRID[1][1] == GRID[2][0]:
        return True
    # Check if no more moves are available
    if None not in GRID[0] and None not in GRID[1] and None not in GRID[2]:
        return True
    return False


print("Jocul X&O\nFiecare casuta este reprezentata de un numar intreg:\n1|2|3\n4|5|6\n7|8|9")
while not check_win():
    # Let user go first
    user_input = input("Alege casuta: ")[0]
    try:
        write_grid(int(user_input), "X")
        computer_move()
    except ValueError:
        print("Te rog sa scrii un numar intreg!")
    except RuntimeError:
        print("Te rog sa alegi o casuta libera!")
    display_grid()

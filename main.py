import copy
from random import randint


# flash (more minimalistic) django
# linear.app
# Prints arrays in a sudoku form
def print_in_form(brd):
    x = 0
    for row in range(9):
        if row % 3 == 0:
            print("_____________")
            if row != 0:
                x += 1
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(brd[i + x * 3][j + (row % 3) * 3], end="")
        print("|")
    print("_____________")


# Testing function, prints out each array
def print_raw(brd):
    for row in brd:
        for value in row:
            print(value, end="")
        print(" ", end="")
    print("")


# Main function
if __name__ == '__main__':
    # each array represents a square in the sudoku puzzle, going by row from left to right
    puzzle = [2, 0, 9, 0, 0, 0, 0, 0, 0], \
             [0, 0, 7, 3, 8, 6, 0, 0, 9], \
             [0, 0, 0, 9, 7, 2, 0, 0, 0], \
             [0, 6, 0, 0, 5, 3, 0, 0, 0], \
             [7, 5, 0, 0, 0, 0, 6, 0, 8], \
             [0, 0, 0, 8, 6, 0, 5, 0, 4], \
             [0, 9, 0, 0, 2, 0, 0, 0, 7], \
             [0, 0, 0, 0, 6, 5, 9, 0, 0], \
             [4, 0, 0, 0, 1, 9, 6, 0, 3]
    print_in_form(puzzle)

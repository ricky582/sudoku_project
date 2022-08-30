import copy
from random import randint
from flask import Flask, render_template, url_for, request
from forms import SudokuCell

app = Flask(__name__)
app.config['SECRET_KEY'] = '76345g0d83427f2f00fb9ba4e0d41567'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = SudokuCell()
        # calling init seems to keep the id of each form in the list constant
        form.__init__(formdata=None, obj=None, prefix='', data=None, meta=None)

        # we get the dict of the input which should contain a csrf token and our data
        cell_input = request.form.to_dict()
        for key in cell_input:
            # all ids in our form list will be of the form list-{number}
            if "list-" in key:
                # we can split string on the dash to convert to int
                test = int(key.split("-")[1])

                if cell_input.get(key):
                    # input is added to players solution
                    player_puzzle[test // 9][test % 9] = cell_input.get(key)
                else:
                    # on empty input, we return that cell to its default value (0)
                    player_puzzle[test // 9][test % 9] = 0

                # for testing:
                print_in_form(player_puzzle)
                print(test)
                print(key)
                print(cell_input.get(key))
        return render_template("main.html", core=puzzle, board=player_puzzle, form=form)
    else:
        form = SudokuCell()
        return render_template("main.html", core=puzzle, board=player_puzzle, form=form)


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
    # each array represents a square in the sudoku puzzle, going by row from left to right, where 0 is an empty cell
    puzzle = [2, 0, 9, 0, 0, 0, 0, 0, 0], \
             [0, 0, 7, 3, 8, 6, 0, 0, 9], \
             [0, 0, 0, 9, 7, 2, 0, 0, 0], \
             [0, 6, 0, 0, 5, 3, 0, 0, 0], \
             [7, 5, 0, 0, 0, 0, 6, 0, 8], \
             [0, 0, 0, 8, 6, 0, 5, 0, 4], \
             [0, 9, 0, 0, 2, 0, 0, 0, 7], \
             [0, 0, 0, 0, 6, 5, 9, 0, 0], \
             [4, 0, 0, 0, 1, 9, 6, 0, 3]
    # the puzzle that the player will manipulate
    player_puzzle = copy.deepcopy(puzzle)

    # for testing:
    print_in_form(puzzle)

    app.run(debug=True)  # - runs the app from main.py config

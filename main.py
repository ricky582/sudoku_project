import copy
from random import randint
from flask import Flask, render_template, url_for, request
from forms import SudokuCell, Options

app = Flask(__name__)
app.config['SECRET_KEY'] = '76345g0d83427f2f00fb9ba4e0d41567'


@app.route("/", methods=['GET', 'POST'])
def home():
    global hist_ptr
    if request.method == 'POST':
        option_forms = Options()
        option_forms.__init__(prefix='options')
        form = SudokuCell()
        # calling init seems to keep the id of each form in the list constant, prefix is "cell" to distinguish it
        form.__init__(formdata=None, obj=None, prefix='cell', data=None, meta=None)

        # we get the dict of the input which should contain a csrf token and our data
        input_data = request.form.to_dict()
        print(input_data)
        for key in input_data:
            # all ids in our form list will be of the form cell-list-{number}
            if "cell-list-" in key:
                # we can split string on the dash to convert to int
                cell_id = int(key.split('-')[2])
                prev_cell_value = player_puzzle[cell_id // 9][cell_id % 9]
                if hist_ptr < len(input_hist) - 1:
                    for i in range(hist_ptr + 1, len(input_hist)):
                        input_hist.pop(hist_ptr + 1)
                if input_data.get(key):
                    # input is added to players solution
                    player_puzzle[cell_id // 9][cell_id % 9] = input_data.get(key)
                    input_hist.append(f"{cell_id}:{prev_cell_value}->{input_data.get(key)}")
                else:
                    # on empty input, we return that cell to its default value (0)
                    player_puzzle[cell_id // 9][cell_id % 9] = 0
                    input_hist.append(f"{cell_id}:{prev_cell_value}->0")
                hist_ptr = hist_ptr + 1

                # for testing:
                # print_in_form(player_puzzle)
            elif "options-undo" in key:
                if hist_ptr >= 0:
                    cell_id = int(input_hist[hist_ptr].split(':')[0])
                    prev_val = int(input_hist[hist_ptr].split(':')[1].split('->')[0])
                    print(f"{cell_id}-{prev_val}")
                    player_puzzle[cell_id // 9][cell_id % 9] = prev_val
                    hist_ptr -= 1
                # else error
            elif "options-redo" in key:
                if hist_ptr != len(input_hist)-1:
                    hist_ptr += 1
                    cell_id = int(input_hist[hist_ptr].split(':')[0])
                    new_val = int(input_hist[hist_ptr].split(':')[1].split('->')[1])
                    print(f"{cell_id}-{new_val}")
                    player_puzzle[cell_id // 9][cell_id % 9] = new_val

        print(f"Pointer{hist_ptr}-Length{len(input_hist)}")
        print(input_hist)
        return render_template("main.html", core=puzzle, board=player_puzzle, form=form, options=option_forms)
    else:
        form = SudokuCell()
        form.__init__(formdata=None, obj=None, prefix='cell', data=None, meta=None)
        option_forms = Options()
        option_forms.__init__(prefix='options')
        return render_template("main.html", core=puzzle, board=player_puzzle, form=form, options=option_forms)


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
    input_hist = []
    hist_ptr = -1

    # for testing:
    print_in_form(puzzle)

    app.run(debug=True)  # - runs the app from main.py config

from flask_wtf import FlaskForm
from wtforms import IntegerField, FieldList, SubmitField
from wtforms.validators import NumberRange, Optional


class SudokuCell(FlaskForm):
    # an individual cell for input in the sudoku board
    input = IntegerField('input', validators=[NumberRange(min=1, max=9)])
    # a list of such input forms so that they are unique
    list = FieldList(input, min_entries=81)


class Options(FlaskForm):
    undo = SubmitField()
    redo = SubmitField()
    hint = SubmitField()

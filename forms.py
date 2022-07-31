from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import Length, NumberRange


class SudokuCell(FlaskForm):
    input = IntegerField('input', validators=[Length(min=0, max=1), NumberRange(min=1, max=9)])

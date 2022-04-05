from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class HoroscopeForm(FlaskForm):
    name = StringField("Horoscope name", name="horoscope-name", validators=[
        DataRequired(),
        Length(min=9),
    ])

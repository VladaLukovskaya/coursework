from wtforms import StringField, SubmitField, IntegerField, DateField, PasswordField, validators
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_wtf import FlaskForm


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Логин', [Length(min=5, max=20), validators.DataRequired])
    password = PasswordField('Пароль', [Length(min=8, max=30), validators.DataRequired])
    submit = SubmitField('Войти')


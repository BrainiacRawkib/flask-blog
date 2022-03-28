import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = wtforms.StringField('Username',
                                   validators=[wtforms.validators.DataRequired(),
                                               Length(min=2, max=20)])
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    confirm_password = wtforms.PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = wtforms.SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    remember = wtforms.BooleanField('Remember me', )
    submit = wtforms.SubmitField('Login')

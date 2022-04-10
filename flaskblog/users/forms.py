import wtforms
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Length, DataRequired, Email, EqualTo
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = wtforms.StringField('Username',
                                   validators=[wtforms.validators.DataRequired(),
                                               Length(min=2, max=20)])
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    confirm_password = wtforms.PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = wtforms.SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise wtforms.ValidationError('username already exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise wtforms.ValidationError('email already exists.')


class LoginForm(FlaskForm):
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    remember = wtforms.BooleanField('Remember me', )
    submit = wtforms.SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = wtforms.StringField('Username',
                                   validators=[wtforms.validators.DataRequired(),
                                               Length(min=2, max=20)])
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = wtforms.SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise wtforms.ValidationError('username already exists.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise wtforms.ValidationError('email already exists.')


class RequestResetForm(FlaskForm):
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    submit = wtforms.SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise wtforms.ValidationError('There is no account with this email.')


class ResetPasswordForm(FlaskForm):
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    confirm_password = wtforms.PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = wtforms.SubmitField('Reset Password')

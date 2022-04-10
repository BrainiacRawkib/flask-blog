import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = wtforms.StringField('Title', validators=[DataRequired()])
    content = wtforms.TextAreaField('Content', validators=[DataRequired()])
    submit = wtforms.SubmitField('Post')

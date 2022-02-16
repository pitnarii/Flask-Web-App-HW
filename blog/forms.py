from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from blog.models import User
from wtforms.widgets import TextArea

class RegistrationForm(FlaskForm):
    username = StringField(label = 'Email', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField(label ='Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField(label ='Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exist. Please choose a different one')

class LoginForm(FlaskForm):
    username = StringField(label = 'Email', validators=[DataRequired()])
    password = PasswordField(label = 'Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()], widget=TextArea())
    author = StringField('Author', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    submit = SubmitField('Submit')
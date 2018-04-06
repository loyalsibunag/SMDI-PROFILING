from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


#Add form class
class AddForm(FlaskForm):
    Station_Code = StringField('Station Code', validators=[DataRequired(), Length(min=1, max=200)])
    Station_Name = StringField('Station Name', validators=[DataRequired(), Length(min=1, max=200)])
    Location = StringField('Location', validators=[DataRequired(), Length(min=1, max=380)])
    Month = StringField('Month', validators=[DataRequired(), Length(min=1, max=32)])
    Day = StringField('Day', validators=[DataRequired(), Length(min=1, max=32)])
    Year = StringField('Year', validators=[DataRequired(), Length(min=1, max=32)])
    Weather = StringField('Weather', validators=[DataRequired(), Length(min=1, max=100)])
    PC = StringField('PC', validators=[DataRequired(), Length(min=1, max=380)])
    Client = StringField('Client', validators=[DataRequired(), Length(min=1, max=200)])
    Type = StringField('Type', validators=[DataRequired(), Length(min=1, max=50)])
    Longitude = StringField('Longitude', validators=[DataRequired(), Length(min=1, max=120)])
    Latitude = StringField('Latitude', validators=[DataRequired(), Length(min=1, max=120)])
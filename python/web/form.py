from wtforms import *
from wtforms.fields import *
from wtforms.validators import *


class CreateUser(Form):
    name = StringField('Name', [validators.Length(
        min=1, max=150), validators.DataRequired()])

    phone = StringField('Mobile Number', validators=[
                        DataRequired(), Length(min=8, max=8)])

    email = EmailField(
        'Email', [validators.Email(), validators.DataRequired()])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8)
    ])


class UserLogin(Form):
    email = EmailField(
        'Email', [validators.Email(), validators.DataRequired()])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8)
    ])
    

class UpdateUser(Form):
    phone = StringField('Mobile Number', validators=[
                        DataRequired(), Length(min=8, max=8)])

    email = EmailField(
        'Email', [validators.Email(), validators.DataRequired()])
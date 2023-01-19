from wtforms import *
from wtforms.fields import *
from wtforms.validators import *


class CreateUser(Form):
    name = StringField('Name', [validators.Length(
        min=1, max=150), validators.DataRequired(message='Enter your Name')])

    phone = StringField('Mobile Number', validators=[
                        validators.DataRequired(message='Enter your Mobile Number'), validators.Length(min=8, max=8, message='Mobile Number must be 8 numberals'), 
                        validators.Regexp(regex='^[8-9]', message='Mobile Number must start with 8 or 9')])

    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email')])

    password = PasswordField('Password', [
        validators.DataRequired(message='Enter your Password'),
        validators.Length(min=8,message='Enter a valid Password')
    ])


class UserLogin(Form):
    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email')])

    password = PasswordField('Password', [
        validators.DataRequired(message='Enter your Password'),
        validators.Length(min=8,message='Enter a valid Password')
    ])
    

class UpdateUser(Form):
    phone = StringField('Mobile Number', validators=[
                        validators.DataRequired(message='Enter your Mobile Number'), validators.Length(min=8, max=8, message='Mobile Number must be 8 numberals'), 
                        validators.Regexp(regex='^[8-9]', message='Mobile Number must start with 8 or 9')])

    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email')])

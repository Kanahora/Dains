from wtforms import *
from wtforms.fields import *
from wtforms.validators import *
import shelve
from flask import session

# Done by Andrew
def duplicate_email(form, field):
    user_db = shelve.open('database/user/user')
    for user in user_db:
        if field.data == user_db[user].get_email():
            raise ValidationError('The Email is already in use')

# Done by Andrew
def duplicate_phone(form, field):
    user_db = shelve.open('database/user/user')
    for user in user_db:
        if field.data == user_db[user].get_phone():
            raise ValidationError('The Mobile Number is already in use')
            
# Done by Andrew
class CreateUser(Form):
    name = StringField('Name', [validators.Length(
        min=1, max=150), validators.DataRequired(message='Enter your Name')])

    phone = StringField('Mobile Number', validators=[
                        validators.DataRequired(message='Enter your Mobile Number'), validators.Length(min=8, max=8, message='Mobile Number must be 8 numberals'), 
                        validators.Regexp(regex='^[8-9]', message='Mobile Number must start with 8 or 9'), duplicate_phone])

    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email'), duplicate_email])

    password = PasswordField('Password', [
        validators.DataRequired(message='Enter your Password'), validators.Regexp(regex='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$'
        , message= 'Password must contain at least 8 characters, one uppercase letter, one lowercase letter, and one digit')
    ])

# Done by Andrew
class UserLogin(Form):
    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email')])

    password = PasswordField('Password', [
        validators.DataRequired(message='Enter your Password'),
        validators.Length(min=8,message='Enter a valid Password')
    ])
    
# Done by Andrew
class UpdateUser(Form):
    phone = StringField('Mobile Number', validators=[
                        validators.DataRequired(message='Enter your Mobile Number'), validators.Length(min=8, max=8, message='Mobile Number must be 8 numberals'), 
                        validators.Regexp(regex='^[8-9]', message='Mobile Number must start with 8 or 9'), duplicate_phone])

    email = EmailField(
        'Email', [validators.Email(message="Enter a valid Email"), validators.DataRequired(message='Enter your Email'), duplicate_email])
import shelve
from wtforms import *

class NavLogin(Form):
	email = EmailField("Email", [validators.Email(message="Enter a valid email address"), validators.DataRequired(message="Provide an email address")])
	password = PasswordField("Password", [validators.Length(min=8, message="Enter your password"), validators.DataRequired(message="Enter your password")])
from flask import *
from python.classes.User import User
import shelve


def main():
	user_object = User('0', 'Andrew Leong', 'Dains123', 'DainsAdmin@gmail.com', '88654101')
	user_object.set_admin()
	key = user_object.get_id()
	value = user_object
	
	user_db = shelve.open('database/user/user')

	if len(user_db) < 1:
		user_db[key] = value
		user_db.close()
	else:
		user_db.close()
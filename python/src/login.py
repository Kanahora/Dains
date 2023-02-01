from flask import *
from python.classes.User import User
import shelve, python.classes.form as form

def login():
	user_login = form.UserLogin(request.form)
	user_status = False
	user_error = False

	if request.method == 'POST' and user_login.validate():
		user_db = shelve.open('database/user/user')
		for user in user_db:
			if user_login.email.data == user_db[user].get_email() and user_login.password.data == user_db[user].get_password():
				session['name'] = user_db[user].get_name()
				session['id'] = user_db[user].get_id()
				session['status'] = user_db[user].get_status()
				session['points'] = user_db[user].get_points()
				user_status = True
				user_error = False
				break
			else:
				user_status = False
				user_error = True
		user_db.close()
	return user_login, user_status, user_error


def logout():
	user_status = True

	if request.method == 'POST':
		session.pop('name', None)
		session.pop('id', None)
		session.pop('status', None)
		session.pop('points', None)

		user_status = False
	return user_status
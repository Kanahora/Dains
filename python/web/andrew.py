from flask import *
from python.classes.User import User
import shelve, python.web.form as form


# Done by Andrew
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
				user_status = True
				user_error = False
				break
			else:
				user_status = False
				user_error = True
		user_db.close()
	return user_login, user_status, user_error


# Done by Andrew
def logout():
	user_status = True

	if request.method == 'POST':
		session.pop('name', None)
		session.pop('id', None)
		session.pop('status', None)

		user_status = False
	return user_status


#Done by Andrew
def register():
	user_register = form.CreateUser(request.form)
	user_status = False

	if request.method == 'POST' and user_register.validate():
		user_db = shelve.open('database/user/user')
		user_object = User(str(len(user_db)), user_register.name.data, user_register.password.data, user_register.email.data, user_register.phone.data)
		key = user_object.get_id()
		value = user_object
		user_db[key] = value

		session['name'] = user_db[key].get_name()
		session['id'] = user_db[key].get_id()

		user_status = True

		user_db.close()

	return user_register, user_status


#Done by Andrew
def account_update():
	user_update = form.UpdateUser(request.form)
	user_status = True

	key = session.get('id', None)
	user_db = shelve.open('database/user/user')

	if request.method == 'POST' and user_update.validate:
		user_dict = {}
		user_dict = user_db[key]

		user_dict.set_phone(user_update.phone.data)
		user_dict.set_email(user_update.email.data)

		user_db[key] = user_dict
	else:
		user_update.phone.data = user_db[key].get_phone()
		user_update.email.data = user_db[key].get_email()

	user_db.close()

	return user_update, user_status


#Done by Andrew
def account_delete():
	user_status = True

	if request.method == 'POST':
		user_dict = {}
		user_db = shelve.open('database/user/user')
		user_dict = user_db

		user_dict.pop(session.get('id', None))
		user_db = user_dict
		user_db.close()

		session.pop('name', None)
		session.pop('id', None)
		session.pop('status', None)        

		user_status = False

	return user_status
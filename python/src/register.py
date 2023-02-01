from flask import *
from python.classes.User import User
import shelve, python.classes.form as form

def register():
	user_register = form.CreateUser(request.form)
	user_status = False

	if request.method == 'POST' and user_register.validate():
		user_db = shelve.open('database/users')
		user_object = User(str(len(user_db)), user_register.name.data, user_register.password.data, user_register.email.data, user_register.phone.data)
		key = user_object.get_id()
		value = user_object
		user_db[key] = value

		session['name'] = user_db[key].get_name()
		session['id'] = user_db[key].get_id()
		session['status'] = user_db[key].get_status()
		session['points'] = user_db[key].get_points()

		user_status = True

		user_db.close()

	return user_register, user_status

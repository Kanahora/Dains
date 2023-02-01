from flask import *
import shelve, python.classes.form as form

def login():
	user_login = form.UserLogin(request.form)
	user_status = False
	user_error = False

	if request.method == 'POST' and user_login.validate():
		user_db = shelve.open('database/users')
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

	if user_status == True:
		return render_template("index.html", user_status=user_status)
	elif user_error == True:
		session["error"] = "Incorrect Email and/or Password. Please try again."
		return render_template("andrew/login.html", form=user_login, user_status=user_status)


def logout():
	user_status = True

	if request.method == 'POST':
		session.pop('name', None)
		session.pop('id', None)
		session.pop('status', None)
		session.pop('points', None)
		user_status = False

	if user_status == False:
		return redirect(url_for("show_login"))
	else:
		return render_template("index.html", user_status=user_status)

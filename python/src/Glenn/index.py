import shelve
from flask import *
from python.classes import User
def index():
	create_admin()
	products = shelve.open("database/products")
	if request.method == "POST":
			id = request.form.get("quickorder-id")
			if id:
				if session.get("name"):
					print("Heading to checkout")
					return render_template("index.html", products=products)
			else:
				print("Heading to login")
				return redirect(url_for("show_login"))
	return render_template("index.html", products=products)

def create_admin():
	users = shelve.open("database/users")
	if len(users) < 1 or not users.get("0"):
		user = User.User("0", "Console", "Dains123", "dainsadmin@gmail.com", "83897086")
		user.set_admin()
		key = user.get_id()
		users[key] = user
	users.close()

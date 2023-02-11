import shelve
from flask import *
from python.classes import User, Cart
def run():
	create_admin()
	shelf_products = shelve.open("database/products")
	products = list()
	for key in shelf_products:
		product = shelf_products[key]
		if product.get_cost() < 2:
			products.append(product)

	if request.method == "POST":
			id = request.form.get("quickorder-id")
			if id:
				if session.get("name"):
					print("Heading to checkout")
					return render_template("index.html", products=products, Cart=Cart)
			else:
				print("Heading to login")
				return redirect(url_for("show_login"))
	return render_template("index.html", products=products, Cart=Cart)

def create_admin():
	users = shelve.open("database/users")
	if len(users) < 1 or not users.get("0"):
		user = User.User("0", "Console", "Dains123", "dainsadmin@gmail.com", "83897086")
		user.set_admin()
		key = user.get_id()
		users[key] = user
	users.close()

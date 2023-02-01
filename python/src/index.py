from flask import *
from python.classes import User, Product
import shelve
def run():
	initialize_admin()
	products = shelve.open("database/products")
	# Remember to delete later
	# This is only for testing
	if len(products) < 1:
		product_1 = Product.Product("classicbarbeq", "Classic BarbeQ", "Burger", 4.99)
		products["classicbarbeq"] = product_1
		product_2 = Product.Product("cheeseburger", "Cheeseburger", "Burger", 3.5)
		products["cheeseburger"] = product_2
		product_3 = Product.Product("cheesyfries", "Cheesy Fries", "Fries", 1.5)
		products["cheesyfries"] = product_3

	# Quick Order
	if request.method == "POST":
		id = request.form.get("quickorder-id")
		# If a quick order button was clicked
		if id:
			# If there is a session, go to checkout
			if session.get("name"):
				print("Heading to checkout")
				return render_template("index.html", products=products)
			# Otherwise, go to login
			else:
				print("Heading to login")
				return redirect(url_for("show_login"))
	return render_template("index.html", products=products)

def initialize_admin():
	users = shelve.open("database/users")
	if len(users) < 1 or not users.get("0"):
		user = User.User("0", "Console", "dains123", "dainsadmin@gmail.com", "83897086")
		user.set_admin()
		key = user.get_id()
		users[key] = user
	users.close()

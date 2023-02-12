from flask import *
import shelve
from python.classes import Cart
def run(category):
	categories = list()
	products = shelve.open("database/products")
	for product in products:
		if not (products[product].get_category() in categories):
			categories.append(products[product].get_category())
	categories.sort()

	if request.method == "POST":
		id = request.form.get("add-to-cart")
		if id:
			if session.get("name"):
				Cart.Cart(session.get("id")).add_product(id)
				return render_template("Glenn/menu.html", products=products, Cart=Cart, category=category, categories=categories)
			else:
				return redirect(url_for("show_login"))
	
	return render_template("Glenn/menu.html", category=category, Cart=Cart, products=products, categories=categories)
from flask import *
import shelve
from python.classes import Cart
def run():
	products = shelve.open("database/products")
	if request.method == "POST":
		add_id = request.form.get("add")
		sub_id = request.form.get("sub")
		del_id = request.form.get("delete")
		
		session_cart = Cart.Cart(session.get("id"))
		cart = session_cart.view_cart()
		checkout_cart = session_cart.view_checkout_cart()

		if add_id:
			Cart.Cart(session.get("id")).add_product(add_id)
		elif sub_id:
			if checkout_cart[sub_id] > 1:
				for id in cart:
					if id.startswith(sub_id):
						session_cart.remove_product(id)
						break
		elif del_id:
			if checkout_cart.get(del_id):
				session_cart.delete_product(del_id)
			else:
				for id in cart:
					if id.startswith(del_id):
						session_cart.remove_product(id)
						break
	return render_template("Glenn/checkout.html", Cart=Cart, products=products)

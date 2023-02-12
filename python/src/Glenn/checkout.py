from flask import *
import shelve
from python.classes import Cart
def run():
	products = shelve.open("products")
	return render_template("Glenn/checkout.html", Cart=Cart, products=products)

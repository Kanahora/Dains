import shelve
from flask import *
from python.classes import Cart
def run(id):
	products = shelve.open("database/products")
	return render_template("Glenn/addon.html", id=id, products=products, Cart=Cart)
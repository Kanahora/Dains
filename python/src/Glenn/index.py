from python.src.Glenn import main, menu, addon, checkout
from python.classes import Cart
from flask import *
def run(app: Flask):
	@app.route("/", methods=["GET", "POST"])
	def show_index():
		return main.run()

	@app.route("/menu", methods=["GET", "POST"])
	def show_menu():
		return menu.run(None)
	
	@app.route("/menu/<category>", methods=["GET", "POST"])
	def show_cmenu(category):
		return menu.run(category)

	@app.route("/addon/<id>", methods=["GET", "POST"])
	def show_addon(id):
		return addon.run(id)

	@app.route("/checkout", methods=["GET", "POST"])
	def show_checkout():
		return checkout.run()

from python.src.Glenn import main, menu
from python.classes import Cart
from flask import *
def run(app: Flask):
	@app.route("/", methods=["GET", "POST"])
	def show_index():
		return main.run()

	@app.route("/menu", methods=["GET", "POST"])
	def show_menu():
		return menu.run(None)

	@app.route("/checkout", methods=["GET", "POST"])
	def show_checkout():
		return render_template("Glenn/checkout.html", Cart=Cart)

	@app.route("/menu/<category>", methods=["GET", "POST"])
	def show_cmenu(category):
		return menu.run(category)
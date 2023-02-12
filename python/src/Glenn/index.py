from python.src.Glenn import main
from python.classes import Cart
from flask import *
def run(app: Flask):
	@app.route("/", methods=["GET", "POST"])
	def show_index():
		return main.run()

	@app.route("/menu", methods=["GET", "POST"])
	def show_menu():
		return render_template("Glenn/menu.html", Cart=Cart)

	@app.route("/checkout", methods=["GET", "POST"])
	def show_checkout():
		return render_template("Glenn/checkout.html", Cart=Cart)

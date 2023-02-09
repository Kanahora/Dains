from flask import *
def run(app: Flask):
	@app.route("/staff/inventory_manage")
	def show_inventory_manage():
		return render_template("Ryan/inventory_manage.html")
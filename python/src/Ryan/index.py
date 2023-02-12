from flask import *
from python.src.Ryan import manage,create,update,delete
def run(app: Flask):
	@app.route("/staff/inventory_manage", methods=["GET", "POST"])
	def show_inventory_manage():
		return manage.inventory_manage()

	@app.route("/staff/inventory_update/<id>", methods=["GET", "POST"])
	def show_inventory_update():
		return update.inventory_update()
	
	@app.route("/staff/inventory_create/", methods=["GET", "POST"])
	def show_inventory_create():
		return create.inventory_create()
	
	@app.route("/staff/delete_product/<product>", methods=["GET", "POST"])
	def delete_product(product):
		return delete.delete_product(product)

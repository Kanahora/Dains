from flask import *
from python.src.Insan import accounts
def run(app: Flask):
	@app.route("/staff/accounts_manage", methods=["GET", "POST"])
	def accounts_manage():
		return accounts.manage()

	@app.route("/staff/accounts_update/<id>", methods=["GET", "POST"])
	def accounts_update(id):
		return accounts.update(id)

	@app.route("/staff/delete_user/<id>", methods=["POST"])
	def delete_user(id):
		return accounts.delete_user(id)
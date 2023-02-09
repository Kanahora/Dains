from flask import *
from python.src.Andrew import login, settings, register
def run(app: Flask):
	@app.route("/login", methods=["GET", "POST"])
	def show_login():
		return login.login()

	@app.route("/logout", methods=["GET", "POST"])
	def show_logout():
		return login.logout()

	@app.route("/register", methods=["GET", "POST"])
	def show_register():
		return register.register()

	@app.route("/settings", methods=["GET", "POST"])
	def show_settings():
		return settings.account_update()

	@app.route('/account_delete', methods=['GET', 'POST'])
	def account_delete():	
		return settings.account_delete()

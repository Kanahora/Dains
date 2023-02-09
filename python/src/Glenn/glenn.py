from index import run_index
from flask import *
def run(app: Flask):
	@app.route("/", methods=["GET", "POST"])
	def show_index():
		return run_index()

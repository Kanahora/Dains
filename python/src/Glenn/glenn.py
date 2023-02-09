from python.src.Glenn import index
from flask import *
def run(app: Flask):
	@app.route("/", methods=["GET", "POST"])
	def show_index():
		return index.run()

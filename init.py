import python.web.main as main
from flask import *
app = Flask(__name__)

# Root
@app.route("/")
def root():
	main.main()
	return render_template("glenn/home.html")

app.run()
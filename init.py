from flask import *
app = Flask(__name__)
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def show_index():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("andrew/login.html")


app.run()
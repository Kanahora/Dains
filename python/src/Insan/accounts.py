from flask import *
from python.classes import User
import shelve


def manage():
    users = shelve.open("database/users")
    if request.method == "POST":
        return redirect(url_for("account_update"))
    return render_template("Insan/accounts_manage.html", count=len(users), user_list=users)

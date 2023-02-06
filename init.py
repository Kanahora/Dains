from flask import *
from python.src import index, login, register, settings
from python.src.Insan import accounts

app = Flask(__name__)
app.secret_key = "secret"

# Glenn
@app.route("/", methods=["GET", "POST"])
def show_index():
    return index.run()
# END Glenn

# Andrew
@app.route('/login', methods=['GET', 'POST'])
def show_login():
    return login.login()


@app.route('/logout', methods=['GET', 'POST'])
def show_logout():
    return login.logout()


@app.route('/register', methods=['GET', 'POST'])
def show_register():
    return register.register()


@app.route('/settings', methods=['GET', 'POST'])
def show_settings():
    return settings.account_update()


@app.route('/account_delete', methods=['GET', 'POST'])
def account_delete():
    return settings.account_delete()
# END Andrew

# Insan
@app.route("/staff/accounts_manage", methods=['GET', 'POST'])
def accounts_manage():
    return accounts.manage()

@app.route("staff/accounts_update/<id>", methods=['GET', 'POST'])
def accounts_update():
    return accounts.update(id)

@app.route('/staff/delete_user/<id>', methods=['POST'])
def delete_user(id):
    return accounts.delete_user(id)
# END Insan

# Rhaylene
@app.route("/staff/rewards_manage", methods=['GET', 'POST'])
def reward_manage():
    return render_template("Rhaylene/rewards_manage.html")
# END Rhaylene

# Ryan
@app.route("staff/inventory_manage", methods=['GET', 'POST'])
def inventory_manage():
    return render_template("Ryan/inventory_manage.html")
# END Ryan


app.run()

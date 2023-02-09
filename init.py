from flask import *
from python.src.Andrew import andrew
from python.src.Glenn import glenn
from python.src.Insan import accounts
from python.src.Rhaylene import rewards

app = Flask(__name__)
app.secret_key = "secret"

glenn.run(app)
andrew.run(app)

# Insan
@app.route("/staff/accounts_manage", methods=['GET', 'POST'])
def accounts_manage():
    return accounts.manage()

@app.route("/staff/accounts_update/<id>", methods=['GET', 'POST'])
def accounts_update():
    return accounts.update(id)

@app.route('/staff/delete_user/<id>', methods=['POST'])
def delete_user(id):
    return accounts.delete_user(id)
# END Insan

# Rhaylene
@app.route("/staff/rewards_manage", methods=['GET', 'POST'])
def rewards_manage():
    return rewards.reward_manage()

@app.route("/staff/reward_create", methods=['GET', 'POST'])
def create_reward():
    return rewards.create_reward()
# END Rhaylene

# Ryan
@app.route("/staff/inventory_manage", methods=['GET', 'POST'])
def inventory_manage():
    return render_template("Ryan/inventory_manage.html")
# END Ryan


app.run()

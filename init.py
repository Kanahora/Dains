from flask import *
import shelve, python.src.login as login, python.src.register as register, python.src.settings as settings
from python.classes.User import User

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def show_index():
    user_object = User('0', 'Andrew Leong', 'Dains123', 'DainsAdmin@gmail.com', '88654101')
    user_object.set_admin()
    key = user_object.get_id()
    value = user_object
	
    user_db = shelve.open('database/user/user')
    
    if len(user_db) < 1:
        user_db[key] = value
        user_db.close()
    else:
        user_db.close()
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def show_login():
    function = login.login()
    user_login = function[0]
    user_status = function[1]
    user_error = function[2]


    if user_status == True:
        return render_template('index.html', user_status=user_status)
    else:
        if user_error == True:
            session['error'] = 'Incorrect Email and/or Password. Please try again.'
        return render_template('andrew/login.html', form=user_login, user_status=user_status)


@app.route('/logout', methods=['GET', 'POST'])
def show_logout():
	logout = login.logout()

	if logout == False:
		return redirect(url_for('show_login'))
	else:
		return render_template('index.html', user_status=logout)


@app.route('/register', methods=['GET', 'POST'])
def show_register():
    function = register.register()
    user_register = function[0]
    user_status = function[1]

    if user_status == True:
        return render_template('index.html', user_status=user_status)
    else:
        return render_template('andrew/register.html', form=user_register, user_status=user_status)


@app.route('/settings', methods=['GET', 'POST'])
def show_settings():
	function = settings.account_update()
	user_update = function[0]
	user_status = function[1]

	return render_template('andrew/settings.html', form=user_update, user_status=user_status)


@app.route('/account_delete', methods=['GET', 'POST'])
def account_delete():
	function = settings.account_delete()

	if function == False:
		return redirect(url_for('show_login'))
	else:
		return render_template('index.html', user_status=account_delete)
app.run()
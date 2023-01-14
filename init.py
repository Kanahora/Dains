import python.web.main as main
from flask import *

app = Flask(__name__)
app.secret_key = 'any_random_string'

# Start of Andrew's Work
@app.route('/')
def root():
	main.main()
	return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	login = main.login()
	user_login = login[0]
	user_status = login[1]
	user_error = login[2]


	if user_status == True:
		return render_template('glenn/home.html', user_status=user_status, name=session.get('name', None), status=session.get('status', None))
	else:
		if user_error == True:
			return redirect(url_for('login'))
		return render_template('andrew/login.html', form=user_login, user_status=user_status)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	logout = main.logout()

	if logout == False:
		return redirect(url_for('login'))
	else:
		return render_template('includes/base.html', user_status=logout, name=session.get('name', None))


@app.route('/register', methods=['GET', 'POST'])
def register():
	register = main.register()
	user_register = register[0]
	user_status = register[1]

	if user_status == True:
		return render_template('glenn/home.html', user_status=user_status, name=session.get('name', None), status=session.get('status', None))
	else:
		return render_template('andrew/register.html', form=user_register, user_status=user_status)


@app.route('/account_settings', methods=['GET', 'POST'])
def account_settings():
	account_settings = main.account_settings()
	user_update = account_settings[0]
	user_status = account_settings[1]
	return render_template('andrew/account_settings.html', form=user_update, user_status=user_status, name=session.get('name', None))


@app.route('/account_delete', methods=['GET', 'POST'])
def account_delete():
	account_delete = main.account_delete()

	if account_delete == False:
		return redirect(url_for('login'))
	else:
		return render_template('includes/base.html', user_status=account_delete, name=session.get('name', None))
# End of Andrew's Work


# Start of Glenn's Work
@app.route('/home')
def home():
	return render_template('glenn/home.html', user_status=True, name=session.get('name', None)) # For your other web pages, pass these 2 parameters for the navbar to work
# End of Glenn's Work


# Start of Insan's Work
@app.route('/account_manage')
def account_manage():
	return render_template('insan/account_manage.html', nav=True)
# End of Insan's Work


# Start of Rhaylene's Work
@app.route('/reward_manage')
def reward_manage():
	return render_template('rhaylene/reward_manage.html', nav=True)
# End of Rhaylene's Work


# Start of Ryan's Work
@app.route('/inventory_manage')
def inventory_manage():
	return render_template('ryan/inventory_manage.html', nav=True)
# End of Ryan's Work






app.run()
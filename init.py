import python.web.main as main
import python.web.andrew as andrew
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
	login = andrew.login()
	user_login = login[0]
	user_status = login[1]
	user_error = login[2]


	if user_status == True:
		return render_template('glenn/home.html', user_status=user_status)
	else:
		if user_error == True:
			session['error'] = 'Incorrect Email and/or Password. Please try again.'
		return render_template('andrew/login.html', form=user_login, user_status=user_status)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	logout = andrew.logout()

	if logout == False:
		return redirect(url_for('login'))
	else:
		return render_template('includes/base.html', user_status=logout)


@app.route('/register', methods=['GET', 'POST'])
def register():
	register = andrew.register()
	user_register = register[0]
	user_status = register[1]

	if user_status == True:
		return render_template('glenn/home.html', user_status=user_status)
	else:
		return render_template('andrew/register.html', form=user_register, user_status=user_status)


@app.route('/account_update', methods=['GET', 'POST'])
def account_update():
	account_update = andrew.account_update()
	user_update = account_update[0]
	user_status = account_update[1]

	return render_template('andrew/account_update.html', form=user_update, user_status=user_status)


@app.route('/account_delete', methods=['GET', 'POST'])
def account_delete():
	account_delete = andrew.account_delete()

	if account_delete == False:
		return redirect(url_for('login'))
	else:
		return render_template('includes/base.html', user_status=account_delete)
# End of Andrew's Work


# Start of Glenn's Work
@app.route('/home')
def home():
	return render_template('glenn/home.html', user_status=True) # For your other web pages, pass these 2 parameters for the navbar to work
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
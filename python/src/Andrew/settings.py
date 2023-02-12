from flask import *
import shelve, python.classes.form as form

def account_update():
	user_update = form.UpdateUser(request.form)
	user_status = True

	key = session.get('id', None)
	user_db = shelve.open('database/users')

	if request.method == 'POST' and user_update.validate():
		user_dict = {}
		user_dict = user_db[key]

		user_dict.set_phone(user_update.phone.data)
		user_dict.set_email(user_update.email.data)

		user_db[key] = user_dict

		session['user_update'] = user_db[key].get_name()

	else:
		user_update.phone.data = user_db[key].get_phone()
		user_update.email.data = user_db[key].get_email()

	user_db.close()
	return render_template("andrew/settings.html", form=user_update, user_status=user_status)


def account_delete():
	user_status = True

	if request.method == 'POST':
		user_dict = {}
		user_db = shelve.open('database/users')
		user_dict = user_db

		user_dict.pop(session.get('id', None))
		user_db = user_dict
		user_db.close()

		session.pop('name', None)
		session.pop('id', None)
		session.pop('status', None)  
		session.pop('points', None)      

		user_status = False

	if user_status == False:
		return redirect(url_for("show_login"))
	else:
		shelf_products = shelve.open("database/products")
		products = list()
		for key in shelf_products:
			product = shelf_products[key]
			if product.get_cost() < 2:
				products.append(product)
		return redirect(url_for("show_index", user_status=user_status, products=products))

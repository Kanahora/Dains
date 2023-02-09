from flask import *
import shelve
from python.classes.form import UpdateAccount


def manage():
    dict = {}
    users = shelve.open("database/users")
    dict = users

    user_list = []
    for key in dict:
        user = dict.get(key)
        user_list.append(user)

    users.close()
    if request.method == "POST":
        return redirect(url_for("accounts_update"))

    return render_template("Insan/accounts_manage.html", count=len(user_list), user_list=user_list)


def update(id):
    forms = UpdateAccount(request.form)
    if request.method == 'POST' and forms.validate():
        user_shelf = shelve.open('database/users')

        users = user_shelf.get(id)
        users.set_name(forms.name.data)
        users.set_phone(forms.phone.data)
        users.set_email(forms.email.data)
        users.set_status(forms.status.data)
        user_shelf[id] = users
        user_shelf.close()

        return redirect(url_for('accounts_manage'))
    else:
        user_dict = {}
        user_shelf = shelve.open('database/users')
        user_dict = user_shelf

        users = user_dict.get(id)
        forms.name.data = users.get_name()
        forms.phone.data = users.get_phone()
        forms.email.data = users.get_email()
        forms.status.data = users.get_status()
        user_shelf.close()
        return render_template('Insan/accounts_update.html', form=forms)


def delete_user(id):
    user_dict = {}
    user_shelf = shelve.open('database/users', 'w')
    user_dict = user_shelf

    user_dict.pop(id)
    user_shelf = user_dict
    user_shelf.close()

    return redirect(url_for('accounts_manage'))

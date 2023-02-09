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
    form = UpdateAccount(request.form)
    if request.method == 'POST' and form.validate():
        user_list = shelve.open('database/users')

        user = user_list.get(id)
        user.set_name(form.name.data)
        user.set_phone(form.phone.data)
        user.set_email(form.email.data)
        print(form.status.data)
        if form.status.data == "CUSTOMER":
            user.set_customer()
        elif form.status.data == "STAFF":
            user.set_staff()
        elif form.status.data == "ADMIN":
            user.set_admin()
        user_list[id] = user

        return redirect(url_for('accounts_manage', count=len(user_list), user_list=user_list))
    else:
        user_dict = {}
        user_list = shelve.open('database/users')
        user_dict = user_list

        user = user_dict.get(id)
        form.name.data = user.get_name()
        form.phone.data = user.get_phone()
        form.email.data = user.get_email()
        form.status.data = user.get_status()
        user_list.close()
        return render_template('Insan/accounts_update.html', form=form)


def delete_user(id):
    user_list = shelve.open('database/users', 'w')
    user_list.pop(id)
    return redirect(url_for('accounts_manage', count=len(user_list), user_list=user_list))


from flask import *
import shelve

def inventory_manage():
    inventory = shelve.open("database/products")
    return render_template('Ryan/inventory_manage.html', count=len(inventory), product_list=inventory)

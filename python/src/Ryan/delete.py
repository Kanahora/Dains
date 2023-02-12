from flask import *
from python.classes import Product
import shelve

def delete_product(id):
    products = shelve.open('database/products', 'w')
    products.pop(id)
    return redirect(url_for('show_inventory_manage', count=len(products), products_list=products))

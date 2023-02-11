from flask import *
from python.classes import Product
import shelve
import python.src.Ryan.Form as form

def inventory_create():
    create_product = form.CreateProduct(request.form)
    if request.method == 'POST' and create_product.validate():
        products = shelve.open("database/products")
        product = Product.Product(create_product.product_id.data,
                               create_product.product_name.data, 
                               create_product.category.data,
                               create_product.price.data,
                               create_product.stock.data
                               )
                               
        products[product.get_id()] = product
        return redirect(url_for('show_inventory_manage', count=len(products), inventory_list=products))
    return render_template('Ryan/inventory_create.html', form=create_product)
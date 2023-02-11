from flask import *
import shelve
import python.src.Ryan.Form as form  

def inventory_update(id):
    update_inventory = form.UpdateProduct(request.form)
    product = shelve.open("database/products")
    if request.method == 'POST' and update_inventory.validate():
        products = shelve.open("database/products")
        product = products.get(id)
        product.set_id(update_inventory.product_id.data)
        product.set_name(update_inventory.product_name.data)
        product.set_category(update_inventory.category.data)
        product.set_price(update_inventory.price.data)
        product.set_stock(update_inventory.stock.data)

        products[id] = product
        return redirect(url_for('inventory_manage', count=len(products), products_list=products))
    else:
        product = products.get(id)
        update_inventory.product_id.data = product.get_id()
        update_inventory.product_name.data = product.get_name()
        update_inventory.category.data = product.get_category()
        update_inventory.price.data = product.get_price()
        update_inventory.stock.data = product.get_stock()
        return redirect(url_for("inventory_update", form=update_inventory))
from flask import *
import shelve
import python.src.Ryan.Form as form  

def inventory_update(product):
    update_inventory = form.UpdateProduct(request.form)
    products = shelve.open("database/products")
    if request.method == 'POST' and update_inventory.validate():
        products = shelve.open("database/products")
        updateproduct = products.get(product)
        updateproduct.set_name(update_inventory.product_name.data)
        updateproduct.set_category(update_inventory.category.data)
        updateproduct.set_cost(update_inventory.price.data)
        updateproduct.add_stock(update_inventory.stock.data)
        updateproduct.set_addon(update_inventory.addon.data)

        products[product] = updateproduct
        return redirect(url_for('show_inventory_manage', count=len(products), products=products))
    else:
        product = products.get(product)
        update_inventory.product_name.data = product.get_name()
        update_inventory.category.data = product.get_category()
        update_inventory.price.data = product.get_cost()
        update_inventory.stock.data = product.get_stock()
        update_inventory.addon.data = product.can_addon()
        return render_template('Ryan/inventory_update.html',form =update_inventory)

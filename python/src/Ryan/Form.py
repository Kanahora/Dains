from wtforms import *
from wtforms.fields import *
from wtforms.validators import *
import shelve
#Done by Ryan
def duplicate_product_id(form,product_id):
    inventory_db = shelve.open(('database/products'))
    for inventory in inventory_db:
        if product_id.data == inventory_db[inventory].get_id():
            raise ValidationError('The Product Id is already listed')
#Done by Ryan
def duplicate_product_name(form,product_name):
    inventory_db = shelve.open(('database/products'))
    for inventory in inventory_db:
        if product_name.data == inventory_db[inventory].get_name():
            raise ValidationError('The Product name is already listed')
# Done by Ryan
class CreateProduct(Form):
    product_id = StringField("Product Id", validators = [DataRequired(message = 'Enter a Product Id'),
                                                       
                                                       duplicate_product_id])
    product_name = StringField("Product Name",
                               validators =[
                                   validators.Length(min=1, max=100, message = 'Enter a product name that is not more than 100 characters'),
                                   validators.DataRequired(message = 'Enter a product name'), duplicate_product_name ])

    category = SelectField("Category",
                           validators = [validators.DataRequired(message = 'Select a category')],
                           choices=[('','Select'),('B', 'Burger'), ('S', 'Sides'), ('D', 'Drinks')],
                           default='')


    price = FloatField("Price ",
                       validators =[
                           validators.DataRequired(message = 'Enter a price') ,
                           validators.NumberRange(min=1, max=100, message = 'Enter a price in a range from 1.00 - 100.00')
                       ])

    stock = IntegerField("Stock Amount", validators = [DataRequired(message = 'Enter a stock amount'),
                                                       validators.NumberRange(min=1, max=1000, message = 'Enter a number between 1-1000')])
#Done by Ryan
class UpdateProduct(Form):
    product_id = IntegerField("Product Id", validators = [DataRequired(message = 'Enter a Product Id'),
                                                       validators.NumberRange(min=1, max=100, message = 'Enter a number between 1-1000'),
                                                       duplicate_product_id])
    product_name = StringField("Product Name",
                               validators =[
                                   validators.Length(min=1, max=100, message = 'Enter a product name that is not more than 100 characters'),
                                   validators.DataRequired(message = 'Enter a product name'), duplicate_product_name ])

    category = SelectField("Category",
                           validators = [validators.DataRequired(message = 'Select a category')],
                           choices=[('','Select'),('B', 'Burger'), ('S', 'Sides'), ('D', 'Drinks')],
                           default='')
    price = FloatField("Price ",
                       validators =[
                           validators.DataRequired(message = 'Enter a price') ,
                           validators.NumberRange(min=1, max=100, message = 'Enter a price in a range from 1.00 - 100.00')
                       ])

    stock = IntegerField("Stock Amount", validators = [DataRequired(message = 'Enter a stock amount'),
                                                       validators.NumberRange(min=1, max=1000, message = 'Enter a number between 1-1000')])

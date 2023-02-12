from wtforms import *
from wtforms.fields import *
from wtforms.validators import *
import shelve

class CreateRewardForm(Form):
    
    name = StringField("", [validators.DataRequired(message="Enter Reward Name")])
    points = SelectField('', [validators.DataRequired()], choices=[('', 'Select'), ('100', '100'), ('200', '200'), ('300', '300'),('400', '400'),('500', '500')],
default='')
    discount = SelectField('', [validators.DataRequired()], choices=[('', 'Select'), ('10% off', '10% off'), ('15% off', '15% off'), ('20% off', '20% off'), ('25% off', '25% off'), ('30% off', '30% off')],
default='')
    
class UpdateRewardForm(Form):
    name = StringField("", [validators.DataRequired(message="Enter Reward Name")])
    points = SelectField('', [validators.DataRequired()], choices=[('', 'Select'), ('100', '100'), ('200', '200'), ('300', '300'),('400', '400'),('500', '500')],
default='')
    discount = SelectField('', [validators.DataRequired()], choices=[('', 'Select'), ('10% off', '10% off'), ('15% off', '15% off'), ('20% off', '20% off'), ('25% off', '25% off'), ('30% off', '30% off')],
default='')
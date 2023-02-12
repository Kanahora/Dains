from wtforms import *
import shelve
from flask import *
def points_validator(form, field):
	if field.data:
		users = shelve.open("database/users")
		rewards = shelve.open("database/rewards")
		if not rewards.get(field.data):
			raise ValidationError("That redeem code does not exist")
		elif int(users[session.get("id")].get_points()) < int(rewards[field.data].get_reward_points()):
			user_points = int(users[session.get("id")].get_points())
			reward_points = int(rewards[field.data].get_reward_points())
			points_needed = reward_points - user_points
			raise ValidationError(f"You need {points_needed} more points to redeem this reward")

class PointsForm(Form):
	field = StringField("", [points_validator])
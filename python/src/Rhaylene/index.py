from python.src.Rhaylene import rewards
from flask import *
def run(app: Flask):
	@app.route("/staff/rewards_manage", methods=["GET", "POST"])
	def rewards_manage():
		return rewards.reward_manage()

	@app.route("/staff/reward_create", methods=["GET", "POST"])
	def create_reward():
		return rewards.create_reward()
from python.src.Rhaylene import rewards
from flask import *
def run(app: Flask):
	@app.route('/staff/rewards_manage', methods=['GET', 'POST'])
	def reward_manage():
		return rewards.reward_manage()

	@app.route('/staff/rewards_create', methods=['GET', 'POST'])
	def create_reward():
		return rewards.create_reward()

	@app.route('/staff/rewards_update/<id>/', methods=['GET', 'POST'])
	def reward_update(id):
		return rewards.reward_update(id)

	@app.route('/staff/deleteReward/<id>', methods=['POST'])
	def delete_reward(id):
		return rewards.delete_reward(id)
	

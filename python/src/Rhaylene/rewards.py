from flask import *
from python.classes import Reward
import shelve, python.classes.form as form

def reward_manage():
    rewards_dict = {}
    reward_shelf = shelve.open('database/reward')
    rewards_dict = reward_shelf['Rewards']
    

    rewards_list = []
    for key in rewards_dict:
        reward = rewards_dict.get(key)
        rewards_list.append(reward)
    reward_shelf.close()
    return render_template('Rhaylene/reward_manage.html', count=len(rewards_list), rewards_list=rewards_list)

def update_reward(id):
    update_reward_form = form.CreateRewardForm(request.form)
    if request.method == 'POST' and update_reward_form.validate():
        rewards_dict = {}
        reward_shelf = shelve.open('database/reward', 'w')
        rewards_dict = reward_shelf['Rewards']

        reward = rewards_dict.get(id)
        reward.set_reward_name(update_reward_form.name.data)
        reward.set_reward_points(update_reward_form.points.data)
        reward.set_reward_description(update_reward_form.description.data)

        reward_shelf['Rewards'] = rewards_dict
        reward_shelf.close()

        return redirect(url_for('reward_manage'))
    else:
        rewards_dict = {}
        reward_shelf = shelve.open('database/reward', 'r')
        rewards_dict = reward_shelf['Rewards']
        reward_shelf.close()

        reward = rewards_dict.get(id)
        update_reward_form.name.data = reward.get_reward_name()
        update_reward_form.points.data = reward.get_reward_points()
        update_reward_form.description.data = reward.get_reward_description()
        return render_template('Rhaylene/reward_update.html', form=update_reward_form)

def delete_reward(id):
    rewards_dict = {}
    reward_shelf = shelve.open('database/reward', 'w')
    rewards_dict = reward_shelf['Rewards']

    rewards_dict.pop(id)
    reward_shelf['Rewards'] = rewards_dict
    reward_shelf.close()

    return redirect(url_for('reward_manage'))

def create_reward():
    create_reward_form = form.CreateRewardForm(request.form)
    if request.method == 'POST' and create_reward_form.validate():
        rewards_dict = {}
        reward_shelf = shelve.open('database/reward', 'c')

        try:
            rewards_dict = reward_shelf['Rewards']
        except:
            print('Error')

        reward = Reward.Reward(create_reward_form.name.data, create_reward_form.points.data, create_reward_form.description.data)
        rewards_dict[reward.get_reward_id()] = reward
        reward_shelf['Rewards'] = rewards_dict
        return redirect(url_for('reward_manage'))
    return render_template('Rhaylene/reward_create.html', form=create_reward_form)


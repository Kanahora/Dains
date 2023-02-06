from flask import *
from python.classes import Reward
import shelve
import python.classes.form as form


def reward_manage():
    rewards = shelve.open("database/rewards")
    return render_template('Rhaylene/rewards_manage.html', count=len(rewards), rewards_list=rewards)


def update_reward(id):
    update_reward_form = form.CreateRewardForm(request.form)
    rewards = shelve.open("database/rewards")
    if request.method == 'POST' and update_reward_form.validate():
        rewards = shelve.open("database/rewards")
        reward = rewards.get(id)
        reward.set_reward_name(update_reward_form.name.data)
        reward.set_reward_points(update_reward_form.points.data)
        reward.set_reward_description(update_reward_form.description.data)

        rewards[id] = reward
        return redirect(url_for('rewards_manage', count=len(rewards), rewards_list=rewards))
    else:
        reward = rewards.get(id)
        update_reward_form.name.data = reward.get_reward_name()
        update_reward_form.points.data = reward.get_reward_points()
        update_reward_form.description.data = reward.get_reward_description()
        return redirect(url_for("rewards_update", form=update_reward_form))


def delete_reward(id):
    rewards = shelve.open('database/rewards', 'w')
    rewards.pop(id)
    return redirect(url_for('rewards_manage', count=len(rewards), rewards_list=rewards))


def create_reward():
    create_reward_form = form.CreateRewardForm(request.form)
    if request.method == 'POST' and create_reward_form.validate():
        rewards = shelve.open("database/rewards")
        reward = Reward.Reward(create_reward_form.name.data,
                               create_reward_form.points.data, create_reward_form.description.data)
        rewards[reward.get_reward_id()] = reward
        return redirect(url_for('rewards_manage'))
    return render_template('Rhaylene/create_reward.html', form=create_reward_form)

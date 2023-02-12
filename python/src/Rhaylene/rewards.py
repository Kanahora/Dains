from flask import *
from python.classes import Reward
import shelve
import python.src.Rhaylene.form as form
from python.classes import Identifier

def reward_manage():
    rewards = shelve.open("database/rewards")
    return render_template('Rhaylene/rewards_manage.html', count=len(rewards), rewards_list=rewards)


def reward_update(id):
    update_reward_form = form.UpdateRewardForm(request.form)
    rewards = shelve.open("database/rewards")
    
    if request.method == 'POST' and update_reward_form.validate():
        rewards = shelve.open("database/rewards")
        reward = rewards[id]
        
        reward.set_reward_name(update_reward_form.name.data)
        reward.set_reward_points(update_reward_form.points.data)
        reward.set_reward_discount(update_reward_form.discount.data)

        rewards[id] = reward
        return redirect(url_for('reward_manage', count=len(rewards), rewards_list=rewards))
    else:
        reward = rewards[id]
        
        update_reward_form.name.data = reward.get_reward_name()
        update_reward_form.points.data = reward.get_reward_points()
        update_reward_form.discount.data = reward.get_reward_discount()
        return render_template('Rhaylene/rewards_update.html', form=update_reward_form)
        

def delete_reward(id):
    rewards = shelve.open('database/rewards', 'w')
    
    rewards.pop(id)
    return redirect(url_for('reward_manage', count=len(rewards), rewards_list=rewards))


def create_reward():
    create_reward_form = form.CreateRewardForm(request.form)
    if request.method == 'POST' and create_reward_form.validate():
        rewards = shelve.open("database/rewards")
        reward = Reward.Reward(Identifier.Identifier().new_reward_id(),
                               create_reward_form.name.data,
                               create_reward_form.points.data, 
                               create_reward_form.discount.data)
        rewards[reward.get_reward_id()] = reward
        return redirect(url_for('reward_manage'))
    return render_template('Rhaylene/rewards_create.html', form=create_reward_form)

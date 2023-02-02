# Rhaylene
class Reward:
    def __init__(self, id, name, points, description):
        self.__reward_id = id
        self.__name = name
        self.__points = points
        self.__description = description

    def set_reward_id(self, reward_id):
        self.__reward_id = reward_id
    def set_reward_name(self, name):
        self.__name = name
    def set_reward_points(self,points):
        self.__points = points
    def set_reward_description(self, description):
        self.__description = description

    def get_reward_id(self):
        return self.__reward_id
    def get_reward_name(self):
        return self.__name
    def get_reward_points(self):
        return self.__points
    def get_reward_description(self):
        return self.__description


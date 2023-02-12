# Rhaylene
class Reward:
    def __init__(self, id, name, points, discount):
        self.__id = id
        self.__name = name
        self.__points = points
        self.__discount = discount
        
    def set_reward_name(self, name):
        self.__name = name

    def set_reward_points(self, points):
        self.__points = points

    def set_reward_discount(self, discount):
        self.__discount = discount

    

    def get_reward_id(self):
        return self.__id

    def get_reward_name(self):
        return self.__name

    def get_reward_points(self):
        return self.__points

    def get_reward_discount(self):
        return self.__discount

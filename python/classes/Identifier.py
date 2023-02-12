import shelve
import uuid
class Identifier:
	def new_product_id(self):
		id = str(uuid.uuid4())[:5]
		ids = shelve.open("database/ids")
		if not ids.get("product"):
			ids["product"] = [id]
		else:
			if id in ids["product"]:
				id = self.new_product_id()
			list = ids["product"]
			list.append(id)
			ids["product"] = list
		ids.close()
		return id

	def new_reward_id(self):
		id = str(uuid.uuid4())[:6]
		ids = shelve.open("database/ids")
		if not ids.get("reward"):
			ids["reward"] = [id]
		else:
			if id in ids["reward"]:
				id = self.new_reward_id()
			list = ids["reward"]
			list.append(id)
			ids["reward"] = list
		ids.close()
		return id

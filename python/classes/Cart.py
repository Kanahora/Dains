import shelve
class Cart:
	def __init__(self, id: str) -> None:
		self.__id__ = id

	def get_id(self):
		return self.__id__

	def view_cart(self):
		carts = shelve.open("database/carts")
		if carts.get(self.get_id()):
			return carts[self.get_id()]
		else:
			return dict()

	def quantity(self):
		result = 0
		cart = self.view_cart()
		for product in cart:
			result += 1
		if result > 99:
			result = " 99+"
		else:
			if result < 10 and result > 0:
				result = f" 0{result}"
			elif result >= 10:
				result = f" {result}"
			elif result == 0:
				result = ""
		return result

	# assigns a unique id after the product id
	# this is for when trying to know which product is being edited
	def product_id_number(self, product_id: str):
		cart = self.view_cart()
		products = filter(lambda id: id.startswith(product_id), cart)
		biggest_number = 0
		for product in products:
			number = int(product.split("_")[1])
			if number > biggest_number:
				biggest_number = number
		return biggest_number + 1

	def add_product(self, product_id: str, *addons):
		products = shelve.open("database/products")
		if products.get(product_id):
			products.close()
			# Create the ID for the new product
			id = f"{product_id}_{self.product_id_number(product_id)}"
			cart = self.view_cart()
			cart[id] = addons or []
			# Update cart
			carts = shelve.open("database/carts")
			carts[self.get_id()] = cart
			carts.close()
			return True
		return False

	def remove_product(self, product_id_with_num: str):
		result = False
		products = shelve.open("database/products")
		cart = self.view_cart()
		new_cart = dict()
		for id in cart:
			# If this is the product to be removed
			if id == product_id_with_num:
				result = True
			# If it's an existing product, add to cart
			if not(id == product_id_with_num) and id.split("_")[0] in products:
				new_cart[id] = cart[id]
		products.close()

		carts = shelve.open("database/carts")
		# Just to check if the new cart is empty
		isEmpty = True
		for product in new_cart:
			isEmpty = False
			break
		# if it's empty, delete cart entirely
		if isEmpty and carts.get(self.get_id()):
			carts.pop(self.get_id())
		# otherwise update
		elif not isEmpty:
			carts[self.get_id()] = new_cart
		carts.close()
		return result

class Product:
	def __init__(self, id: str, name: str, category: str, cost: int, isMeal: bool) -> None:
		self.__id__ = id
		self.__name__ = name
		self.__image__ = None
		self.__category__ = category
		self.__cost__ = cost
		self.__stock__ = 0
		self.__isMeal__ = isMeal

	def set_name(self, name: str):
		self.__name__ = name

	def set_image(self, url: str):
		self.__image__ = url

	def set_category(self, category: str):
		self.__category__ = category

	def set_cost(self, cost: int):
		self.__cost__ = cost
	
	def set_alacarte(self):
		self.__isMeal__ = False

	def set_meal(self):
		self.__isMeal__ = True

	def add_stock(self, **quantity: int):
		if not quantity:
			quantity = 1
		self.__stock__ += quantity

	def remove_stock(self, **quantity: int):
		if not quantity:
			quantity = 1
		if self.__stock__ > 0:
			self.__stock__ -= quantity

	def get_id(self) -> str:
		return self.__id__

	def get_name(self) -> str:
		return self.__name__

	def get_image(self) -> str:
		return self.__image__

	def get_category(self) -> str:
		return self.__category__

	def get_cost(self) -> int:
		return self.__cost__

	def get_stock(self) -> int:
		return self.__stock__

	def is_available(self) -> bool:
		return self.get_stock() > 0
class User:
	def __init__(self, id: str, name: str, password: str, email: str, phone: str):
		self.__id__ = id
		self.__cart__ = {}
		self.__name__ = name
		self.__email__ = email
		self.__password__ = password
		self.__phone__ = phone
		self.__status__ = "CUSTOMER"
		self.__isAdmin__ = False
		self.__points__ = 0

	def set_name(self, name: str):
		self.__name__ = name

	def set_email(self, email: str):
		self.__email__ = email

	def set_password(self, password: str):
		self.__password__ = password

	def set_phone(self, phone: str):
		self.__phone__ = phone

	def set_customer(self):
		self.__status__ = "CUSTOMER"
		self.__isAdmin__ = False

	def set_staff(self):
		self.__status__ = "STAFF"
		self.__isAdmin__ = False

	def set_admin(self):
		self.__status__ = "STAFF"
		self.__isAdmin__ = True

	def set_points(self, points: int):
		self.__points__ = points

	def add_points(self, points: int):
		self.__points__ += points

	def remove_points(self, points: int):
		if self.__points__ - points < 1:
			self.__points__ = 0
		else:
			self.__points__ -= points

	def get_points(self) -> int:
		return self.__points__
	
	def get_id(self) -> str:
		return self.__id__

	def get_name(self) -> str:
		return self.__name__

	def get_email(self) -> str:
		return self.__email__

	def get_password(self) -> str:
		return self.__password__

	def get_phone(self) -> str:
		return self.__phone__

	def get_status(self) -> str:
		return self.__status__

	def is_admin(self) -> bool:
		if self.get_status() == "CUSTOMER":
			return False
		if self.get_status() == "STAFF":
			return self.__isAdmin__

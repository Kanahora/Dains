class Reward:
	def __init__(self, code: str, points: int) -> None:
		self.__code__ = code
		self.__title__ = None
		self.__points__ = points
		self.__description__ = None

	def set_title(self, title: str) -> None:
		self.__title__ = title

	def set_description(self, description: str) -> None:
		self.__description__ = description

	def set_points(self, points: int) -> None:
		self.__points__ = points

	def get_code(self) -> str:
		return self.__code__

	def get_title(self) -> str:
		return self.__title__

	def get_points(self) -> int:
		return self.__points__

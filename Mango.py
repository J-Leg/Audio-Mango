class Mango:

	def __init__(self, toHide, medium):
		self.__toHide = toHide
		self.__medium = medium
		self.__pixels = 30
		self.__wav_rate = 44100

	def Process(self):
		print("hey")

	def set_sample(self, rate):
		self.__wav_rate = rate

	def set_pixel(self, rate):
		self.__pixels = rate
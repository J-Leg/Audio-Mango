from PIL import Image, ImageOps
from pydub import AudioSegment
from Mcoder import mc
import numpy
import soundfile as sf

class Mango:

	def __init__(self, medium):
		self.__medium = medium
		self.__pixels = 30
		self.__mc = mc(medium)

		# 44100 is an industry standard sampling rate
		self.__wav_rate = 44100


	def Mangonise(self):
		self.__inputSanity()
		medium_data = self.__d.decode()



	def __inputSanity(self):

		format = self.__medium[-3:]

		if format == 'wav' or format == 'flac' or format == 'ogg':
			# Native file format
			return
		elif format == 'mp3':

			print("mp3 file detected!\n"
				+ "Converting to "
				+ self.__medium[-3:] + ".wav...")

			# Convert into wav
			sound = AudioSegment.from_mp3(self.__medium)

			# Modify the mango to read from new file
			self.__medium = self.__medium[:-3] + "wav"
			sound.export(self.__medium, format="wav")	
		else:
			print(format + " is not a supported mango.")
			
		return

	def set_sample(self, rate):
		self.__wav_rate = rate

	def set_pixel(self, rate):
		self.__pixels = rate
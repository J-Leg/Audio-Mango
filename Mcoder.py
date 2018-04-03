import wave
import os

class Mcoder:
	def __init__(self, medium):
		self.__medium = medium
		self.__params = None
		self.__num_channels = None
		self.__num_frames = None
		self.__sample_width = None
		self.__num_samples = None
		self.__num_lsb = 2
		self.__min_sample = None


	# Set the sound file parameters
	def decode():
		w_handle = wave.open(sound_path, "r")

		self.__params = w_handle.getparams()
		self.__num_channels = w_handle.getnchannels()
		self.__sample_width = w_handle.getsamplewidth()
		self.__num_frames = w_handle.getnframes()

		self.__num_samples = self.__num_frames * self.__num_channels


		minSample = None

		# Floor division
		# 8 is a reasonable factor of the sampling rate
		max_bytes = (self.__num_samples * self.__num_lsb) // 8

		fileSize = os.stat(self.__medium).st_size


		# Assume sample width is 2
		fmt = "{}h".format(num_samples)


		mask = (1 << 15) - (1 << self.__num_lsb)
		self.__min_sample = -(1 << 15)

		raw_data = list(struct.unpack(fmt, sound.readframes(self.__num_frames)))
		return raw_data


	def set_lsb(value)
		self.__num_lsb = value
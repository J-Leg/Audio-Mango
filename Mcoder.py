import wave
import os
import struct

class Mcoder:
	def __init__(self, mango):
		self.__mango = mango
		self.__params = None
		self.__num_channels = None
		self.__sample_width = None
		self.__num_frames = None
		self.__num_samples = None
		self.__num_lsb = 2
		self.__min_sample = None
		self.__mask = None
		self.__fmt = None

	# Process
	def juice(self):
		medium_data = self.__decode(self.__mango.getMedium())
		print("Decoding complete.")
		self.__encode(self.__mango.getData(), medium_data)
		print("Encoding complete.")


	# Set the sound file parameters
	# Decode file into raw data
	def __decode(self, medium):
		w_handle = wave.open(medium, "r")

		self.__params = w_handle.getparams()
		self.__num_channels = w_handle.getnchannels()
		self.__sample_width = w_handle.getsampwidth()
		self.__num_frames = w_handle.getnframes()

		self.__num_samples = self.__num_frames * self.__num_channels


		minSample = None

		# Floor division
		# 8 is a reasonable factor of the sampling rate
		max_bytes = (self.__num_samples * self.__num_lsb) // 8

		fileSize = os.stat(medium).st_size


		# Assume sample width is 2
		# format string, expected layout of the data when packing and unpacking
		fmt = "{}h".format(self.__num_samples)

		self.__fmt = fmt

		self.__mask = (1 << 15) - (1 << self.__num_lsb)
		self.__min_sample = -(1 << 15)

		raw_data = list(struct.unpack(fmt, w_handle.readframes(self.__num_frames)))
		w_handle.close()
		return raw_data


	# Restore sound file according to the file parameters set
	# But with the data from another input >:)
	def __encode(self, input, medium):
		input_data = memoryview(open(input, "rb").read())
		num_lsb = self.__num_lsb

		# Pointing to the current bit for their respective lists
		# index in the array
		data_cursor = 0
		medium_cursor = 0

		# Will hold the bytes of new data
		new_sf = []

		# Buffer
		buff = 0
		buff_len = 0
		finished = False

		print("Encoding...")
		while(not finished):
			while (buff_len < num_lsb and data_cursor // 8 < len(input_data)):

				# Grab next byte from file
				# Working with bytes, 1 byte = 8 bits
				buff += (input_data[data_cursor // 8] >> (data_cursor % 8)) << buff_len
				bits_added = 8 - (data_cursor % 8)
				buff_len += bits_added

				# Increment the cursor
				data_cursor += bits_added

			# Retrieve next num_lsb bits from the buffer
			# for subsequent processing
			curr_data = buff % (1 << num_lsb)
			buff >>= num_lsb
			buff_len -= num_lsb

			while(medium_cursor < len(medium) and 
				medium[medium_cursor] == self.__min_sample):

				# We want to avoid changing LSB for the minimum sample value
				new_sf.append(struct.pack(self.__fmt[-1], medium[medium_cursor]))
				medium_cursor += 1

			print("data_cursor: " + str(data_cursor) + " ----- medium_cursor: " + str(medium_cursor))
			if(medium_cursor < len(medium)):
				current_sample = medium[medium_cursor]
				medium_cursor += 1

				sign = 1

				if(current_sample < 0):
					# two's complement issues
					current_sample = -current_sample
					sign = -1


				altered_sample = sign * ((current_sample & self.__mask) | curr_data)
				new_sf.append(struct.pack(self.__fmt[-1], altered_sample))

			# When the data cursor reaches the end of input_data[]
			# indicates completion
			if (data_cursor // 8 >= len(input_data) and buff_len <= 0):
				finished = True


		print("Data exhausted {finished} ---- medium cursor: " + str(medium_cursor))

		# If all the input is hidden
		# Simply append the rest of the sound file from the medium
		while(medium_cursor < len(medium)):
			new_sf.append(struct.pack(self.__fmt[-1], medium[medium_cursor]))
			medium_cursor += 1

		# Create file to write to
		new_sf_handle = wave.open(self.__mango.getOut(), "w")
		new_sf_handle.setparams(self.__params)
		new_sf_handle.writeframes(b"".join(new_sf))
		new_sf_handle.close()

	def set_lsb(self, value):
		self.__num_lsb = value
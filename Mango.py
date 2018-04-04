
class Mango:
	def __init__(self, data, medium, out):
		self.__data = data
		self.__medium = medium
<<<<<<< HEAD
		self.__out = out
=======
		self.__pixels = 30

		# 44100 is an industry standard sampling rate
		self.__wav_rate = 44100

	def Process(self):
		data = self.__process_audio()
		



	def __process_audio(self):
		format = self.__medium[-3:]

		if format == 'wav' or format == 'flac' or format == 'ogg':
			print("Native file format detected")
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

		print("Reading sound file...")

		# Read in audio file
		data, samplerate = sf.read(self.__medium, always_2d=True)
		return data
>>>>>>> master

	def getData(self):
		return self.__data

	def getMedium(self):
		return self.__medium

	def getOut(self):
		return self.__out

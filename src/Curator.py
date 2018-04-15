from PIL import Image, ImageOps
from pydub import AudioSegment


# Handles files
class Curator:

	def __init__(self):
		pass

	def Organise(self, inputPath, mediumPath, out):
		format = mediumPath[-3:]

		out = "lsb/" + out + ".wav"

		if format == 'wav' or format == 'flac' or format == 'ogg':
			# Native file format
			return inputPath, mediumPath, out
		elif format == 'mp3':

			newPath = mediumPath[:-3] + "wav"

			print("mp3 file detected!\n"
				+ "Converting to "
				+ newPath + "...")

			# Convert into wav
			sound = AudioSegment.from_mp3(mediumPath)
			sound.export(newPath, format="wav")	
		else:
			print(format + " is not a supported mango.")
			exit(0)

		return inputPath, newPath, out

	def isValid(self, filePath):
		format = filePath[-3:]
		flag = False

		if format == 'wav' or format == 'flac' or format == 'ogg':
			flag = True

		return flag
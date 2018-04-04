from PIL import Image, ImageOps
from pydub import AudioSegment


# Handles files
class Curator:

	def __init__(self):
		pass


	def Organise(self, inputPath, mediumPath):
		format = mediumPath[-3:]

		if format == 'wav' or format == 'flac' or format == 'ogg':
			# Native file format
			return inputPath, mediumPath
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
			
		return inputPath, newPath
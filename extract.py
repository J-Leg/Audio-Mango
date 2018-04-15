import argparse
import os
import sys
from src.Mcoder import Mcoder
from src.Curator import Curator
from src.Mango import Mango

def main():
	directory = 'extracted_payloads/'
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="The wav file holding the data. Don't input path to file.")
	parser.add_argument("num_bytes", help="The number of bytes to recover")
	args = parser.parse_args()

	# Initialise Curator
	c = Curator()

	if(not c.isValid(args.input)):
		print("Invalid file format.\n"
			+ "Must be a .wav file.")

	if not os.path.exists(directory):
		print(directory + " doesn't exist.\n"
			+ "Creating " + directory + " directory...")
		os.makedirs(directory)

	# Initialise Mango
	mango = Mango(None, "lsb/" + args.input, directory + args.input[:-4] + '_payload')

	# Initialise Mcoder
	mc = Mcoder(mango)

	# Get up and work
	mc.dejuice(int(args.num_bytes))


if __name__ == "__main__":
	main()
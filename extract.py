import argparse
import os
from Mcoder import Mcoder
from Curator import Curator
from Mango import Mango

def main():
	directory = 'payload_lib/'
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="The wav file holding the data")
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
	mango = Mango(None, args.input, directory + args.input[:-4] + '_payload')

	# Initialise Mcoder
	mc = Mcoder(mango)

	# Get up and work
	mc.dejuice(int(args.num_bytes))


if __name__ == "__main__":
	main()
import argparse
from Mcoder import Mcoder

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="The wav file holding the data")
	parser.add_argument("output", help="Output the restored file")
	args = parser.parse_args()

	# Initialise Curator
	c = Curator()

	if(not c.isValid(args.input)):
		print("Invalid file format.\n"
			+ "Must be a .wav file.")
		exit(0)

	# Initialise Mango
	mango = Mango(None, args.input, args.output)

	# Initialise Mcoder
	mc = Mcoder(mango)

	# Get up and work
	mc.dejuice()


if __name__ == "__main__":
	main()
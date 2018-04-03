import argparse
from Mango import Mango

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("data", help="Data file to be hidden.")
	parser.add_argument("medium", help="The audio file.")
	parser.add_argument("-p", "--pixels", help="Pixels per second. Default value: 30.", type=int)
	parser.add_argument("-s", "--sampling", help="Sampling rate. Default value: 44100.", type=int)
	args = parser.parse_args()

	# Initialise Mango
	mango = Mango(args.data, args.medium)

	# Set user defined parameters if necessary
	if args.pixels:
		mango.set_pixels(args.pixels)

	if args.sampling:
		mango.set_sample(args.sampling)

	# Get down to business
	mango.Process()

if __name__ == "__main__":
	main()
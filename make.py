import argparse
from src.Curator import Curator
from src.Mango import Mango
from src.Mcoder import Mcoder

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="Data file to be hidden.")
	parser.add_argument("medium", help="The audio file.")
	parser.add_argument("output", help="Set the output filename")
	parser.add_argument("-m", "--mode", help="Select mode: lsb or spec", type=str)
	args = parser.parse_args()

	if args.mode == 'spec':
		mango = Mango(args.input, args.medium, "spec/" + args.output + ".wav")
		mc = Mcoder(mango)
		mc.spectro()
	else:
		# Initialise Curator
		c = Curator()

		d_input, medium, output = c.Organise(args.input, args.medium, args.output)

		# Initialise Mango
		mango = Mango(d_input, medium, output)

		# Initialise Mcoder
		# Handles the decoding/encoding process for mango obj type
		mc = Mcoder(mango)

		# Get down and boogy
		mc.juice()


if __name__ == "__main__":
	main()
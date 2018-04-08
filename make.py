import argparse
from src.Curator import Curator
from src.Mango import Mango
from src.Mcoder import Mcoder

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="Data file to be hidden.")
	parser.add_argument("medium", help="The audio file.")
	parser.add_argument("output", help="Set the output file/path.")
	parser.add_argument("-p", "--pixels", help="Pixels per second. Default value: 30.", type=int)
	parser.add_argument("-s", "--sampling", help="Sampling rate. Default value: 44100.", type=int)
	args = parser.parse_args()

	# Initialise Curator
	c = Curator()

	d_input, medium = c.Organise(args.input, args.medium)

	# Initialise Mango
	mango = Mango(d_input, medium, args.output)

	# Initialise Mcoder
	# Handles the decoding/encoding process for mango obj type
	mc = Mcoder(mango)

	# Get down and boogy
	mc.juice()


if __name__ == "__main__":
	main()
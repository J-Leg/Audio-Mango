import argparse
from src.Curator import Curator
from src.Mango import Mango
from src.Mcoder import Mcoder

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="Payload file in payload_lib. Don't input path.")
	parser.add_argument("medium", help="The audio file in slice_lib. Don't input path.")
	parser.add_argument("output", help="Set the output filename")
	parser.add_argument("-m", "--mode", help="Select mode: lsb or spec", type=str)
	args = parser.parse_args()

	if args.mode == 'spec':
		mango = Mango("include/payload_lib/" + args.input, "include/slice_lib/" + args.medium, "spec/" + args.output + ".wav")
		mc = Mcoder(mango)
		mc.spectro()
	elif args.mode == 'lsb':
		# Initialise Curator
		c = Curator()

		d_input, medium, output = c.Organise("include/payload_lib/" + args.input, "include/slice_lib/" + args.medium, args.output)

		# Initialise Mango
		mango = Mango(d_input, medium, output)

		# Initialise Mcoder
		# Handles the decoding/encoding process for mango obj type
		mc = Mcoder(mango)

		# Get down and boogy
		mc.juice()
	else:
		print("No mode selected.")


if __name__ == "__main__":
	main()
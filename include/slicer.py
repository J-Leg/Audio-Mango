from pydub import AudioSegment
import argparse


# Put the sound file you want to slice into lib and use this script to slice

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file that exists in lib. Not path.")
parser.add_argument("lo", help="lowerbound (sec)", type=int)
parser.add_argument("hi", help="upperbound (sec)", type=int)
parser.add_argument("-fi","--fadein", help="fade in offset (sec)", type=int)
parser.add_argument("-fo","--fadeout", help="fade out offset (sec)", type=int)
args = parser.parse_args()

inputPath = "lib/" + args.input
format = args.input[-3:]

if format == "mp3":
	song = AudioSegment.from_mp3(inputPath)
elif format == "wav":
	song = AudioSegment.from_mp3(inputPath)
else:
	print("not supported format")
	exit(0)

lo = args.lo*1000
hi = args.hi*1000

if hi < lo:
	print("Invalid range")
	exit(0)

result = song[lo:hi]

if args.fadein:
	result = result.fade_in(args.fadein * 1000)

if args.fadeout:
	result = result.fade_out(args.fadeout * 1000)

result.export("slice_lib/" + args.input)
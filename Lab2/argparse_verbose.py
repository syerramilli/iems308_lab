# Simple example which returns the given power of the given integer
# with an argument which controls the output verbosity
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Returns the given power of the given integer")
# Define arguments
parser.add_argument("value",help="The integer",type=int)
parser.add_argument("power",help="The power",type=int)
# arguments beginining with -- indicate optional arguments
parser.add_argument("-v","--verbose",default=0,type=int,
	help="increase verbosity")
args = parser.parse_args()

# Print to stdout
out = args.value**args.power
if args.verbose>=1:
	print("{}^{} equals {}".format(args.value,args.power,out))
else:
	print(out)

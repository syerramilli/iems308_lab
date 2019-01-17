# Simple example which returns the square of the given integer
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Returns the square of the given integer")
# Syntax
parser.add_argument("value",help="The integer whose square is needed",type=int)
args = parser.parse_args()

# Print to stdout
print(args.value**2)

import sys

def fizzBuzz(start, finish):
	for i in xrange(start, finish):
		string = ""
		if i % 3 == 0:
			string += "Fizz"
		if i % 5 == 0:
			string += "Buzz"
		if string == "":
			string += str(i)
		print string

def bottlesOfBeer(total):
	ending = "Take one down, pass it around, "
	line = "{0} bottle{1} of beer on the wall, {0} bottle{1} of beer."
	for i in xrange(total, 0, -1):
		s = "s" if i > 1 else ""
		print line.format(i,s)
		if i == 2:
			print ending + "1 bottle of beer on the wall."
		elif i > 2:
			print ending + str(i - 1) + " bottles of beer on the wall."
		else:
			print "No more bottles of beer on the wall!"

inputFile = "input.sa"
if len(sys.argv) > 1:
	inputFile = sys.argv[1]

with open(inputFile, 'r') as f:
	while True:
		c = f.read(1)
		if not c:
			break
		else:
			if c == 'B':
				bottlesOfBeer(99)
			elif c == 'F':
				fizzBuzz(1, 101)
			elif c == 'H':
				print "Hello, world!"

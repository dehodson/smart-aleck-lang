
import sys

def fizzBuzz(start, finish):
	step = 1 if start <= finish else -1
	for i in xrange(start, finish, step):
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
	stack = []
	skipRead = False
	while True:
		if not skipRead:
			c = f.read(1)
		else:
			skipRead = False

		if not c:
			break

		else:
			if c == 'B':
				num = 99
				if(len(stack) > 0):
					num = int(stack.pop())
				bottlesOfBeer(num)

			elif c == 'F':
				end = 101
				start = 1
				if(len(stack) > 1):
					end = int(stack.pop())
					start = int(stack.pop())
				elif(len(stack) > 0):
					end = int(stack.pop())
				fizzBuzz(start, end)

			elif c == 'H':
				print "Hello, world!"

			elif c == 'P':
				print stack.pop()

			elif c == 'Q':
				old = f.tell()
				f.seek(0)
				print f.read()
				f.seek(old)

			elif c == '"':
				stack.append("")
				while True:
					c = f.read(1)
					if not c:
						break
					if c == '"':
						break
					else:
						stack[-1] += c

			elif c in '0123456789':
				stack.append(int(c))
				while True:
					c = f.read(1)
					if not c:
						break
					if c in '0123456789':
						stack[-1] = (stack[-1] * 10) + int(c)
					else:
						skipRead = True
						break


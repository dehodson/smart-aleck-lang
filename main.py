
import sys

hasPrinted = False

def show(string):
	global hasPrinted
	hasPrinted = True
	print string

def bottlesOfBeer(total, what):
	ending = "Take one down, pass it around, "
	line = "{0} bottle{1} of {2} on the wall, {0} bottle{1} of {2}."
	for i in xrange(total, 0, -1):
		s = "s" if i > 1 else ""
		show(line.format(i,s,what))
		if i == 2:
			show(ending + "1 bottle of "+what+" on the wall.")
		elif i > 2:
			show(ending + str(i - 1) + " bottles of "+what+" on the wall.")
		else:
			show("No more bottles of "+what+" on the wall!")

def fibonacciGenerator():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b    

def fibonacci(start, finish):
	for k, v in enumerate(fibonacciGenerator()):
		if k >= start:
			show(v)
		if k >= finish:
			break

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
		show(string)

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
			if c == 'f':
				end = 10
				start = 0
				if(len(stack) > 1):
					end = int(stack.pop())
					start = int(stack.pop())
				elif(len(stack) > 0):
					end = int(stack.pop())
				fibonacci(start, end)

			elif c == 'B':
				what = "beer"
				num = 99
				if(len(stack) > 1):
					what = str(stack.pop())
					num = int(stack.pop())
				elif(len(stack) > 0):
					var = stack.pop()
					if(type(var) == str):
						what = var
					else:
						num = int(var)
				bottlesOfBeer(num, what)

			elif c == 'C':
				show(sys.stdin.read())

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
				show("Hello, world!")

			elif c == 'P':
				if(len(stack) > 0):
					show(str(stack.pop()))

			elif c == 'Q':
				old = f.tell()
				f.seek(0)
				show(f.read())
				f.seek(old)

			elif c == 'R':
				if(len(stack) > 0):
					stack.append(str(stack.pop())[::-1])
				else:
					show(sys.stdin.read()[::-1])

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

if not hasPrinted:
	if(len(stack) > 0):
		show(str(stack[-1]))


import sys

hasPrinted = False
hasRead = False
stdin = ""
pointer = 0

def show(string):
	global hasPrinted
	hasPrinted = True
	print string

def take():
	global stdin
	global hasRead

	if not hasRead:
		stdin = sys.stdin.read()
		hasRead = True

	return stdin

def takeInt():
	global stdin
	global hasRead
	global pointer

	negative = False
	output = 0

	if not hasRead:
		stdin = sys.stdin.read()
		hasRead = True

	char = stdin[pointer]
	while char not in '0123456789' and pointer < (len(stdin) - 1):
		pointer += 1
		char = stdin[pointer]

	if pointer != 0 and stdin[pointer - 1] == "-":
		negative = True

	while pointer < (len(stdin) - 1):
		char = stdin[pointer]
		if char in '0123456789':
			output = output * 10 + int(char)
		else:
			break
		pointer += 1

	if negative:
		output *= -1

	return output

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

def toRoman(num):
	nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
		(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
	roman = ''
	while num > 0:
		for i, r in nums:
			while num >= i:
				roman += r
				num -= i
	return roman

inputFile = "input.sa"
if len(sys.argv) > 1:
	inputFile = sys.argv[1]

with open(inputFile, 'r') as f:
	stack = []
	skipRead = False
	ignoreMode = False
	looping = False
	loopPos = 0

	if '#' in f.read():
		ignoreMode = True

	f.seek(0)

	while True:
		while True:
			if ignoreMode:
				while True:
					c = f.read(1)
					if not c:
						break
					if c == '#':
						ignoreMode = False
						break

			if not skipRead:
				c = f.read(1)
			else:
				skipRead = False

			if not c:
				break

			else:
				if c == 'a':
					stack.append('abcdefghijklmnopqrstuvwxyz')

				elif c == 'f':
					end = 10
					start = 0
					if(len(stack) > 1):
						end = int(stack.pop())
						start = int(stack.pop())
					elif(len(stack) > 0):
						end = int(stack.pop())
					fibonacci(start, end)

				elif c == 'i':
					stack.append(takeInt())

				elif c == 'l':
					if(len(stack) > 0):
						num = int(stack.pop())
						for i in xrange(1, num):
							stack.append(i)

				elif c == 'n':
					if(len(stack) > 1):
						index = int(stack.pop())
						stack.append(stack.pop(len(stack) - index))

				elif c == 'r':
					if(len(stack) > 0):
						stack.append(toRoman(int(stack.pop())))

				elif c == 'x':
					stack.reverse()

				elif c == 'z':
					stack.append('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

				elif c == 'A':
					stack.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

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
					show(take())

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

				elif c == 'L':
					if(len(stack) > 0):
						looping = True
						loopPos = f.tell()

				elif c == 'N':
					if(len(stack) > 1):
						index = int(stack.pop())
						stack.append(stack.pop(len(stack)))

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
						show(take()[::-1])

				elif c == 'S':
					stack.append(take())

				elif c == 'Z':
					stack.append('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

				elif c == '+':
					if(len(stack) > 1):
						a = stack.pop()
						b = stack.pop()
						if(type(a) == str or type(b) == str):
							stack.append(str(a) + str(b))
						else:
							stack.append(int(a) + int(b))
					elif(len(stack) > 0):
						stack.append(take() + str(stack.pop()))

				elif c == '-':
					if(len(stack) > 1):
						a = stack.pop()
						b = stack.pop()
						if(type(a) == str and type(b) == str):
							stack.append(a.translate(None, b))
						else:
							stack.append(int(a)-int(b))
					elif(len(stack) > 0):
						if(type(stack[-1]) == str):
							stack.append(stack.pop().translate(None, take()))

				elif c == '*':
					if(len(stack) > 1):
						a = stack.pop()
						b = stack.pop()
						if((type(a) == str or type(b) == str) and
							(type(a) == int or type(b) == int)):
							if(type(a) == str):
								stack.append(str(a) * int(b))
							else:
								stack.append(str(b) * int(a))
						else:
							stack.append(int(a) * int(b))
					elif(len(stack) > 0):
						if(type(stack[-1]) == int):
							stack.append(take() * stack.pop())

				elif c == '#':
					ignoreMode = True

				elif c == ':':
					if(len(stack) > 0):
						stack.append(stack[-1])
					else:
						stack.append(take())
						stack.append(take())

				elif c == '@':
					stack.append(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")

				elif c == '\'':
					c = f.read(1)
					if not c:
						break
					stack.append(c)

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
		if looping:
			if(len(stack) > 0):
				f.seek(loopPos)
			else:
				break
		else:
			break

if not hasPrinted:
	if(len(stack) > 0):
		show(str(stack[-1]))

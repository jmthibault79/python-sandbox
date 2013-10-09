#####################################################################
# Basic assignment and output

a = 324
b = 24
c = a - b
print 'a - b is', c

d = "OMG"
e = "WTF"
f = "BBQ"
g = "!"
print "String Cat Printing: " + d + e + f + g*3
print "List Printing:", d, e, f, g*3

# Functions

def hypotenuse_squared (a, b):
	return a**2 + b**2

print hypotenuse_squared(3, 4)

#####################################################################
# List and string slicing
# NB: exclusive of second operand

mylist = ['happy', 'happy', 'joy', 'joy']
print mylist[1:3]
print mylist[-1]
print mylist[:1]

print mylist[0][1:4]

def two_inclusive_slices (str, begin1, end1, begin2, end2):
	return str[begin1:end1+1] + ' ' + str[begin2:end2+1]
	
teststr = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
print two_inclusive_slices(teststr, 22, 27, 97, 102)

teststr2 = 'HQhzO4rGuZVX0GVqThtHa4kq6KfN0Drst8lpLVRAcipenserySLFbMw1KJyTfhrnE62yJ16igREwf5R6NJwbXldJB0DeqGfzdRIB6W7j9lKJKEG7pqdJR52HFw88xMfalcipennis0vvBiehXaTVKjxFV3h18mu7QlQiyBiCeOn4ltyskRPo3c.'
print two_inclusive_slices(teststr2, 39, 47, 126, 136)

#####################################################################
# if, while, for, and range

if '1' == 2:
	print "DOES NOT COMPUTE"
else:
	print 'Passed sanity check'
	
looper = 5
while looper > 0:
	print 'Countdown:', looper
	looper = looper - 1
	
for newlooper in range(3):
	print 'Count up:', newlooper
	
for newlooper in range(2,4):
	print 'Count up range(2,4):', newlooper
	
def sum_all_odd_inclusive (a, b):
	acc = 0
	for candidate in range(a, b+1):
		if candidate % 2 == 1:
			acc = acc + candidate
	return acc
	
print sum_all_odd_inclusive(100, 200)
print sum_all_odd_inclusive(101, 199)
print sum_all_odd_inclusive(4631, 9151)

#####################################################################
# files

def countlines (filename):
	linecount = 0
	for line in open(filename, 'r'):
		linecount = linecount + 1
	return linecount
	
print countlines ('noob.py')

file = open('noob.py', 'r')
print str(file.read(10))
print file.readline().strip().split()
file.close()

def save_even_lines (infilename, outfilename):
	import os
	infile = open(os.path.expanduser(infilename), 'r')
	outfile = open(os.path.expanduser(outfilename), 'w')
	printme = False
	for line in infile:
		if printme:
			outfile.write(line)
		printme = not printme
	outfile.close()
	infile.close()
	
#save_even_lines('~/Downloads/sir_robin.txt', '~/Downloads/sir_robin_even.txt')
#save_even_lines('~/Downloads/rosalind_ini5.txt', '~/Downloads/rosalind_ini5_even.txt')
		
#####################################################################
# dictionaries

dict = { 'key': 1, 'KEY': 2 }
print dict

nonkey = 'not a key'
if nonkey not in dict:
	print 'Did not find', nonkey

del dict['key']
print dict

def string_token_counter (s):
	dict = {}
	for token in s.split():
		if token in dict:
			dict[token] = dict[token] + 1
		else:
			dict[token] = 1
	for token in dict:
		print token, dict[token]
		
let_it_be = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
string_token_counter(let_it_be)

#####################################################################
# misc other basic features

a, b = 1, 2
print a, b
a, b = b, a
print a, b

print a, b,
print "continuation"

if a < b:
	print "less"
elif b < a:
	print "more"
else:
	print "same"

# for-else / while-else: executes if the loop completes (doesn't use break)

import random
looper = 10
while looper > 0:
	if random.randint(1, 10) == looper:
		print 'Random number hit:', looper
		break
	looper = looper - 1
else:
	print 'Random number did not hit'
	
#####################################################################
# function parameters

def my_func (param1, param2='default string'):
	print param1, param2
	
my_func ('test')
my_func ('club', 'sandwich')
my_func ('club', param2='med')

# careful!  L gets reused here

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

def funargs(dummy, *varargs, **keyvaluepairs):
	print "Varargs"
	for idx in range(len(varargs)):
		print idx, varargs[idx]
	print "KVPs"
	for key in keyvaluepairs:
		print key, keyvaluepairs[key]
		
funargs (1, 'fish', 'Alabama', named_param='Omega')
		
tuple = ['dog', 'New Jersey']
dict = {"name": "Steve", "demeanor": "unpleasant"}
funargs ('ignored', *tuple, **dict)

#####################################################################
# lists: stack, queue, filter, map, reduce

l = [1, 2, 3]
print l.pop()
l.append(4)
print l

from collections import deque
q = deque(l)
print q.popleft()
print q.popleft()

nums = [1, -2, 7, 5, 2, -11]

def pos(x): return x >= 0
print filter(pos, nums)

def sqr(x): return x * x	
print map(sqr, nums)

def add(x, y): return x + y
print reduce(add, nums)

#####################################################################
# list comprehensions

# wrong
# posnums = [for x in nums if pos]
# sqrnums = [sqr for x in nums]

print [x * x for x in nums if x >= 0]
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

#####################################################################
# sets

numbers = set([1, 2, 3])
letters = set("hello")
print letters
print numbers & letters
print numbers - letters

morenumbers = {x for x in range(3)}
print morenumbers
print numbers ^ morenumbers

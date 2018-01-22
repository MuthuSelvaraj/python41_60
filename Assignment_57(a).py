try:
	import pack6.str
except ImportError as e:
	print "import error",e


a=0
b=1
try:
	a=b%0
except Error as e:
	print e



try:
	val=int(raw_input('enter n'))
	print val
except ValueError as e:
	print "value error",e


try:
	file=open("hello.txt" , "r")
	file.write("hi")
except IOError as e:
	print e


try:
	print s
except NameError as e:
	print e


try:
	prit "hi"
except SyntaxError as e:
	print e


a=input('enter the pound ')
assert (a>0) , "input not in negative"
assert (a<=100) , "pound more than 100 "
kg=a/2.2046
print a,"pound is equal to ",kg,"kilograms"


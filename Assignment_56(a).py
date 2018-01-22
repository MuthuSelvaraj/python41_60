try:
	file=open("hello.txt" , "r")
	file.write("hi")
except IOError as e:
	print e
try:
	val=int(input('enter n'))
	#print val
except ValueError:
	print "error"

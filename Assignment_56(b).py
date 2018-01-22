
try:
	val=int(raw_input('enter n'))
	print val
except ValueError as e:
	print "value error",e

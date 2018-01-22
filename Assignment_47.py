tuple1=(1,2,3,4,5)
list=[6,7,8,9,10]
print "tuple is",tuple1
print "list is",list
def extend(t1,l1):
	t2=tuple(l1)
	print "The extended of list and tuple is ",t1+t2
extend(tuple1,list)
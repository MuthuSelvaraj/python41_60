def tupleop():
	tup1=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
	tup2=('January','February','March','April','May','June','July','Augest','September','October','November','December')
	print "Concat the two tuples tup1 and tup2\n",tup1+tup2

	tuple1=(1,2,3,4,5)
	tuple2=(100,200,300)
	tuple3=(1000,2000)

	print "\n"
	if(cmp(tuple1,tuple2) ==1 and cmp(tuple1,tuple3) ==1 ):
		print "tuple1 is bigger",tuple1
	elif(cmp(tuple2,tuple3) ==1 and cmp(tuple2,tuple1) ==1):
		print "tuple2 is bigger",tuple2
	else:
		print "tuple3 is bigger",tuple3

	list1=list(tuple1)
	list1.pop(3)
	tuple1=tuple(list1)
	print "Delete the 4th elemnt in the tuple  " ,tuple1
	del tuple1
	print "Now completely delete entire tuple1"

	list2=list(tuple2)
	list2.insert(1,150)
	tuple2=tuple(list2)
	print "inserted one element in the tuple  ",tuple2
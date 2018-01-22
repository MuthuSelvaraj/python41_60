def listop():	
	list1=[1,2,3,4,5,6,7,8,9,10]
	list2=[10,20,30,40,50]
	list3=[100,200,300,400,500]
	print "Length of list1 is",len(list1)
	print "Length of list2 is",len(list2)
	print "Length of list3 is",len(list3)
	print "Maximum element in list1 is",max(list1)
	print "Maximum element in list2 is",max(list2)
	print "Maximum element in list3 is",max(list3)

	if( cmp(list1,list2) == 1 and cmp(list1,list2) == 1 ):
		print "List1 is biggest"
	elif( cmp(list2,list1) == 1 and cmp(list2,list3) == 1 ):
		print "List2 is biggest"
	else:
		print "List3 is biggest"

	if( cmp(list1,list2) < 0 and cmp(list1,list2) < 0 ):
		print "List1 is smallest"
	elif( cmp(list2,list1) < 0 and cmp(list2,list3) < 0 ):
		print "List2 is smallest"
	else:
		print "List3 is smallest"


	list1.pop(0)
	list1.pop(len(list1)-1)
	list2.pop(0)
	list2.pop(len(list2)-1)
	list3.pop(0)
	list3.pop(len(list3)-1)
	print "Remove first and last elements in list1",list1
	print "Remove first and last elements in list2",list2
	print "Remove first and last elements in list3",list3





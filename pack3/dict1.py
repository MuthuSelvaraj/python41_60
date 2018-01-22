def dictop():
	dict1 = {'brand':'nokia','color':'blue','model_no':'N73'}
	dict2={'name':'john','age':22,'salary':10000}
	dict3={1:'xxx',2:'yyy',3:'zzz'}
	print dict1
	print dict2
	print dict3

	if(cmp(dict1,dict2) ==1 and cmp(dict1,dict3) ==1 ):
		print "dict1 is bigger",dict1
	elif(cmp(dict2,dict3) ==1 and cmp(dict2,dict1) ==1):
		print "dict2 is bigger",dict2
	else:
		print "dict3 is bigger",dict3
	dict1['cost']=10032	
	dict2['gender']='male'
	print "After add some values in dict1",dict1
	print "After add some values in dict2",dict2
	print "length of dict1 is",len(dict1),"length of dict2 is",len(dict2),"length of dict3 is",len(dict3)
	string=str(dict1)+str(dict2)+str(dict3)
	print "\n"
	print "the all dictionaries are converted to string\n",string
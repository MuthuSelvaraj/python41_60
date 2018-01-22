def dictop():
	dict1 ={'Name':'Ramakrishna','Age':25}
	dict2={'EmpId':1234,'Salary':5000}
	dict3={}
	dict3.update(dict1)
	dict3.update(dict2)
	print "Merging two dict and create on single dict",dict3
	sal=dict3['Salary']
	percent=sal/10
	dict3['Salary']=percent+sal
	print "Increased the salary 10%", dict3
	dict3['Age']=26
	print "Increased the age to 26", dict3
	dict3['Grade']='B1'
	print "Insert the grade ", dict3
	print "Values are",dict3.items()
	print "Keys are", dict3.keys()
	del dict3['Age']
	print "After delete the age the list will be",dict3

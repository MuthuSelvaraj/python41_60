def vow(string):
	list1=[]
	newstring= string.lower()
	list1=list(newstring)
	print list1
	count=0
	temp=1
	for i in range(len(newstring)):
		if(newstring[i]=='a' or newstring[i]=='e' or newstring[i]=='i' or newstring[i]=='o' or newstring[i]=='u' ):
			count=count+1

	print "Total vowels in the given string is",count
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			if(list1[i]==list1[j]):
				temp=temp+1
				list1[j]=' '

		if(list1[i]=='a' or list1[i]=='e' or list1[i]=='i' or list1[i]=='o' or list1[i]=='u'):
		
			print list1[i],"  ",temp
		
		
		temp=1
	#print list1
def binary():
	item_list=[1,2,3,4,5,6,7,8]
	print item_list
	item=input('Enter the element you want to search in the list\n')
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid=(first + last)//2
		if item_list[mid] == item :
			found=True
		else:
			if item<item_list[mid]:
				last=mid - 1
			else:
				first=mid + 1	
	
	
	if (found == True):
		print "present"
	else:
		print "not present"
	return
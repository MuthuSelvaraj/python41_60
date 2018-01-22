def sorting(list1):
	list1.sort()
	print "After sorting",list1
	return
def search(item_list,item):
	item_list.sort()
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
		print "element",item,"is present"
	else:
		print "element",item,"is not present"
def rev(str):
	revstr=str[::-1]
	print "reverse of the given string is",revstr
	
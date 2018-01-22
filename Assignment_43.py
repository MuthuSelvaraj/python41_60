list=[1,2,3,4,5,6,7,8,9,10]
print "List is",list
a=input('Enter the elment you want to search\n')
b=input('Enter the elment you want to search\n')
c=input('Enter the elment you want to search\n')
d=input('Enter the elment you want to search\n')

def search(*elements):
	for e in elements:
		if( e in list):
			print "element ",e,"is present in the list"
		else:
			print "element ",e,"is not present in the list"

search(a,b,c,d)
import Assignment_59(module)
list=[]
n=input("enter how many numbers to sort \n")
print "enter ",n,"numbers"
for i in range(n):
	list.append(input())
print "before sorting",list
Assignment_599.sorting(list)
n1=input('enter the number you want to search in the list\n')
Assignment_599.search(list,n1)
string=raw_input("Enter the string you want to reverse\n")
Assignment_599.rev(string)
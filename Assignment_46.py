a1=input('enter 1st number\n')
b1=input('enter 2nd number\n')
c1=input('enter 3rd number\n')
d1=input('enter 4th number\n')
def findbig(a,b,c,d):
	if(a>b and a>c and a>d):
		print "biggest num is",a
	elif(b>a and b>c and b>d):
		print "biggest num is",b
	elif(c>a and c>b and c>d):
		print "biggest num is",c
	else:
		print "biggest num is",d
findbig(a=a1,b=b1,c=c1,d=d1)
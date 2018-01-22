def fib(n):
	print "fibonacci series for the range of ",n,"is\n"
	print 0
	print 1
	a=0
	b=1
	for i in range(0,n):
		c=a+b
		print c
		a=b
		b=c
	return
n=input('Enter the range\n')
print "\n"
fib(n)
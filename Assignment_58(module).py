import math
def add(a,b):
	print "addition of a ,b, is ",a+b
	return
def sub(a,b):
	print "difference of a ,b, is ",a-b
	return
def mul(a,b):
	print "multiplication of a ,b, is ",a*b
	return
def div(a,b):
	print "division of a ,b, is ",a/b
	return
def fdiv(a,b):
	print "floor division of a ,b, is ",a//b
	return
def mod(a,b):
	print "modulus of a ,b, is ",a%b
	return
def square(a):
	print "square root of the no is",math.sqrt(a)
def prime(a):
	for i in range(2,a):
    		if (a % i ==0):
        		print "The number ",a ,"is not prime"
        		break
	else:
         		print "The number ",a ,"is  prime"
def fib(n):
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
         
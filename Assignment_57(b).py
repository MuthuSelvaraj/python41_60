try:
    pi = 0 
    for k in range(350): 
        pi += (4./(8.*k+1.) - 2./(8.*k+4.) - 1./(8.*k+5.) - 1./(8.*k+6.)) / 16.**k 
    print pi
except Exception as e:
	print "overflow error",e

try:
   list=[]
   print list[1]
except IndexError as e:
	print e

try:
	dict={'1':'muthu','2':'gfd','5':'gfhfgh'}
	print dict['7']
except KeyError as e:
	print e


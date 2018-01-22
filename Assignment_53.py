#file=open("hello.txt","r")
fo = open("hello1.txt", "wb")
print "using write() successfully wrote data to the file"
fo.write( "Python")
fo.close()
fo = open("hello1.txt", "r")
print "using read() print the data below"
print fo.read()
fo.close()
fo = open("hello.txt", "r")
print "using readlines() print the data as a line by line below"
list=fo.readlines()
for i in range(len(list)):
	print list[i].rstrip()
print "using tell()"
print "file object in ",fo.tell()
print "using seek() reset the position of object from 55 to 1"
fo.seek(1)
print "file object in ",fo.tell()
fo.close()
fo = open("hello1.txt", "wb")
fo.write("hello")
fo.flush()
print "using flush method flushes the data to file without clising the file"
fid=fo.fileno()
print "usingt fileno()  == ",fid
ret = fo.isatty()
print "using isatty()  ", ret
fo = open("hello.txt", "r")
for index in range(5):
   line = fo.next()
   print "using next() Line No %d - %s" % (index, line)

# Close opend file
fo.close()


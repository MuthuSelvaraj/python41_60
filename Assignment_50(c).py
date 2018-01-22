file = open("hello.txt", "r")
list=file.readlines()
print "read the file from 5th line onwards\n"
for i in range(4,len(list)):
	print list[i]
file.close()
           
#file=open("hello.txt","r")
print "print the lines from last to first"
for line in reversed(open("hello.txt").readlines()):
    print line.rstrip()
print "\n"
print "print the chararcters from last to first"
for line in reversed(open("hello.txt").read()):
    print line

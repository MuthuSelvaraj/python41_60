file = open('hello.txt', 'r')

while 1:
    c = file.read(1)         
    if not c: break
    print c,"corresponding file object position is",file.tell()
print "after read all character from file the file object will be resetted to starting position"
file.seek(0)
print "now file object in ",file.tell()
print "now again print the data\n",file.read()
file.close()
           
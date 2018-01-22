def fileop():
	fo = open("C:\\Users\\mu391839\\Desktop\\Python\\python41_60\\pack5\\hello.txt", "r")
	str = fo.read();
	print "Read String from file is: ", str
	fo.close()
def encode(str):
	

	string=str.encode('base64','strict')
	print "The Encoded String in your friend's side: ",string
	str1=string.decode('base64','strict')
	if (str==str1):
		print "your friend received the message after decoding: ",str
	return
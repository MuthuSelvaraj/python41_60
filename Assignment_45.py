string=raw_input('Enter the string\n')
def pal(string):
	revstring =string[::-1]
	if ( revstring == string):
		print "the given string is palindrome"
	else:
		print "the given string is not palindrome"
pal(string)
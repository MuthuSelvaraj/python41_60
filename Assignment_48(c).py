print "please give the string in the format of xxx:xxx:xxx: ....... :xxx"
str=raw_input('enter string in the above format\n')
def sub(string,ch):
	print "The list of substring from string is",string.split(':')
sub(str,':')

try:
    print a
except NameError as e:
  print "In this program it is a name error exceptio occured\n",e

try:
    a=0
    b=1
    print b/a
except ArithmeticError as e:
  print "In this program it is a arithmeticerror exception occured\n",e


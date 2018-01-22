count=0
for year in range(1980,2026):
 
	if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    		count=count+1
print "There are ",count , "leap year between 1980 to 2015"	
	
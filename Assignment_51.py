import os

search_path = raw_input("Enter directory path to search : ")
file_type = raw_input("File Type : ")
search_str = raw_input("Enter the search string : ")
list=[]
c=0
a=0
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
if not os.path.exists(search_path):
        search_path ="."

for fname in os.listdir(search_path):

   if fname.endswith(file_type):
	
        fo = open(search_path + fname)

        line = fo.readline()
	
        line_no = 1
			
        while line != '' :
		for word in line.split():
		    if(word==search_str):
			a=a+1
               
                index = line.find(search_str)
                if ( index != -1) :
                   
	            #list.append(fname)	
		    c=1
		    #a=a+1	
               
                line = fo.readline()  
        
                line_no += 1     
        fo.close()
   print "data were ",a, "times present in the file" ,fname
   a=0
   if(c==1):
	list.append(fname)
   
   c=0
print "in the given directory there are ",len(list)," files having the pattern"
def Bubblesort(list):
    print "before sorting",list
    a = True
    num = len(list)-1
    while num > 0 and a:
       a = False
       for i in range(num):
           if list[i]>list[i+1]:
               a = True
               temp = list[i]
               list[i] = list[i+1]
               list[i+1] = temp
       num = num-1
    print "using bubble sort the sorted order of list is",list
    return
		


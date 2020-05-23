#getting kth  min maximum value from list
#pro-tip set contains sorted items 
#convert input list into set
list1 =set(list(map(int,input().split())))
#but oops set doesnt allow indexing so convert back to list
print (list(list1)[1],list(list1)[-2])
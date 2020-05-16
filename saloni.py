from collections import OrderedDict 
list1 =list(map(int,input().split()))
list1.sort()
list1 =list(OrderedDict.fromkeys(list1)) 
print(list1[-2]) 
print(list1[1])
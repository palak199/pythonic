import operator
dicti={}
dicti["ram"]=89
dicti["vgh"]=9
d=dicti
l=dicti.values()

print(max(dicti.items(),key=operator.itemgetter(1))[0])
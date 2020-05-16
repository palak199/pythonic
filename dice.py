import random
import matplotlib.pyplot as plt
bin={
    1:8,
    2:4,
    3:90,
    4:8,
    5:4
}
x=[]
y=[]
val=bin.values()
for each in list(set(val)):
    x.append(each)
    y.append(val.count(each))
    print (each,val.count(each))
plt.plot(x,y)
plt.show()
    
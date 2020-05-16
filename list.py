import random
def get_gates():
    r=random.randint(0,2)
    r1=random.randint(0,2)
    while(r==r1):
        r=random.randint(0,2)
    l=['x','x','x']
    l[r]='c'
    l[r1]='c'
    ind=[0,1,2]
    for each in ind:
        if(each!=r1 and each!=r):
            l[each]='g'
    print(l)
while(1):
    r=random.randint(0,1)
    if(r==0):
        print("tossing")
        break
    else:
        print("tossing")
p1=['a','b','c']
p2=['a','b','c']
c1=random.choice(p1)
c2=random.choice(p2)
if(c1==c2):
    
    print(c1,c2,"success")
else:
    print("failure")
get_gates()

bin={}
for i in range(1,11):
    bin[i]=0
for i in range(1,101):
    r=random.randint(1,10)
    bin[r]=bin[r]+1
print(sum(bin.values()))
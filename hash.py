from itertools import combinations
f=open("a_example (1).in","r")
w=open("res.txt","w")
num,pizza=map(int, f.readline().split())
l=list(map(int,f.readline().split()))
l1=list(combinations(l,3))
s={}
k=[]

for i in l1:
    count=0
    for j in i:
        count+=j
    s[count]=i

for k in s.keys():
    w.write(str(k))
        
 
    
        
        
N=int(input())
l=list(map(int,input().split()[:N]))
l2=[]
for i in range (0,N):
    l2.append(l[i]+l[N-1-i])
    print(l2[i],end=" ")        
    
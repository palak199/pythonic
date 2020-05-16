l=list(map(int,input().split()))
l.sort(reverse=True)
for i in l[1:]:
    if i<l[0]:
        print (i,end=' ')
        break
l.reverse()
for i in l[1:]:
    if i>l[0]:
        print (i,end='')
        break

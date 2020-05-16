for i in range(101):
    f=0
    for j in range(2,i):
        if(j*j==i):
            f=1
            break
    if(f==0):
        print(i)

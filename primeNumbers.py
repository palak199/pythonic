#program to print prime numbers in a given range
for i in range (101):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i)
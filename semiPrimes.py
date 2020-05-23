# A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
# Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).

from itertools import combinations as c
def prime(n):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
            break
    if(f==0):
        return 0 
  
def semiprime(n):
    l=[]
    f=0
    if n>2 and n%2==0:
        l.append(2)
    for i in range(3,n+1):
        if prime(i)==0 and (n%i==0):
            l.append(i)
    ln=list(c(l, 2))
    for i in ln:
        if(i[0]*i[1]==n):
            print(i[0],i[1])
            f=1
            break
    if(f==0):
        return 0

semiprime(9)         

num=int(input())
f=0
l=[]
for i in range(1,num):
    if semiprime(i)!=0:
        for j in range(1,num):
            if semiprime(j)!=0:
                l.append((i,j))
for i in l:
    if(i[0]+i[1]==num):
        f=1
        print("yes")
        break
if(f==0):
        print("no")
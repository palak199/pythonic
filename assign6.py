'''def enc(li,n):
    l=[]
    for i in list(li):
        l.append(chr(ord(i)+1))
    return ''.join(l)
li='ABCDEF'
print(enc(li,5))
def guess(n):
    i=int(input("guess"))
    if(i==n):
        print("yep")
    else:
        guess(n)
guess(3)
def mul(n):
    if(n==-1):
        return -1
    else:
        print(n)
        return(-1*mul(n-1))
    
print(mul(int(input())))
def search(l,loc,item):
    if(loc<0):
        print(loc)
        loc=0
    if(l[loc]==item):
        print("found",loc)
        return
    if(loc==len(l)-1):
        print("nf")
        return 0
    else:
        return search(l,loc+1,item)

l=[1,2,3,4,5,6,7,8,9]
search(l,4,3)
    
print(int(7.96)+int(7.56))'''

def fu(n):
    print(n)
    if(n==0):
        print("over")
    else:
        fu(n/2)

fu(128)
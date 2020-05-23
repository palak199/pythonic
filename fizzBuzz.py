p,q,r=map(int,input().split())
if r%p==0:
    if r%q!=0:
        print("fizz")
if r%q==0:
    if r%p!=0:
        print("buzz")
else:
        print("fb")

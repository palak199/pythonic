

def Divide(n):
    print(n)
    if(n==0):
        print("over")
    else:
        Divide(n/2)

Divide(128)
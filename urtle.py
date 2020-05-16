import turtle
def func(mx,i,n):
    turt=turtle.Turtle()
    turt.setpos(i,i)
    for ind in range(i,n-i):
        turt.goto(i,ind)
    for ind in range(i+1,n-i):
        turt.goto(i,n-1-i)
    for ind in range(n-2-i,i,-1):
        turt.goto(n-1-i,ind)
    for ind in range(n-i-1,i,-1):
        turt.goto(ind,i)
def func1(mx):
    n=len(mx)
    i=0
    while(i<=n-1):
        func(mx,i,n)
        i=i+10
mx=[[0 for i in range(70)] for i in range(70)]

func1(mx)
turtle.getscreen().getcanvas().postscript(file='outputname.ps')
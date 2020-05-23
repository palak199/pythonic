#a person is standing at position p
#he takes 2 steps forward then 4 back
#determine after how many steps he reaches 0 or negative value.
p=int(input())
while(p>0):
    p=p+2
    p=p-4

print("fell at ",p)
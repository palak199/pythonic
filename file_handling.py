with open("f.txt","w") as f:
    f.write("0110")
f.close()
s=0
with open("f.txt","r") as f:
    l=list(f.read())
    
    for i in l:
        s+=int(i)
print (s)
f.close()
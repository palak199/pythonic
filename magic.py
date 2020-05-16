def check():
    num=[1,2,3,4,5,6,7,8,9]
    a00,a01,a10,a11=0,0,0,0
    for i in range(0,8):
        for j in range(0,8):
            for k in range(0,8):
                for l in range(0,8):
                    a00=num[i]
                    a01=num[j]
                    a10=num[k]
                    a11=num[l]
                    l=[a00,a01,a10,a11]
                    
                    print(a00,"\t",a01,"\n",a10,"\t",a11)
                    print("\n")
check()
                   
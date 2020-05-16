import math
N,vm,vc=map(int,input().split())
tc=2*N/vc
tm=math.sqrt(2)*N/vm
if(tc<tm):
  print ("Cab")
else:
  print("Walk")

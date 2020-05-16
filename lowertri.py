n=int(input())
matrix=[[int(input()) for x in range (n)] for y in range (n)]
for i in range(n):
  for j in range (n):
    if(i>j):
      matrix[i][j]=0
print(matrix)
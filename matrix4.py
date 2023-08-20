# important
n=int(input())
res=[list(range(1+n*i,1+n*(i+1)))
     for i in range(n)]
print(res)
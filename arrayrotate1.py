x=[1,2,3,4,5,6,7]
y=int(input())
z=[]
for i in range(0,y):
    x.append(x[i])
del x[0:y]
print(x)

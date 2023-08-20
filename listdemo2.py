mynum=[]
i=0
while i<=5:
    x=int(input("enter"+str(i)+"elements:"))
    mynum.append(x)
    i=i+1
print("the list is")
sum=0
for x in mynum:
    print(x)
    sum+=x
    print("sum is",sum)

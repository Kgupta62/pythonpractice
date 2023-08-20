"""mynum=[]
text=input("enter 5 no:")
for x in text.split():
    mynum.append(int(x))
print("list is:",mynum)
print("sum is:",sum(mynum))"""
text=input("enter 5 integer")
mynum=[int(x)for x in text.split()]
print(mynum)
print("sum is:",sum(mynum))
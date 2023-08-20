from collections import Counter
x=input()
y=input()
x=Counter(x)
y=Counter(y)
result=x&y
print(x)
print(y)
print(result)

if(result==x):
    print("possible")
else:
    print("not possible")




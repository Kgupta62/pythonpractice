x=input("Enter a no.")
z=list(x)
y=0
for i in z:
    y=y+pow(int(i),len(z))
if(y==int(x)):
    print("Yes")
else:
    print("No")
x=int(input())
y=int(input())
z=[]
for i in range(x,y+1):
    no = 0
    for a in range(2,i):
        if i%a==0 :
            no=1
            break
    if no==0 :
        z.append(i)
print(z)



    # loop
    # loop
    # i last no x 1start
    # i%x ==0 y+=y+1
    # y>2 ye ho jayega non prime

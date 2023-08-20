tup=[('for',24),('is',10),('a',28),('geeks',23)]
l=len(tup)
for i in range(0,l):
    for j in range(0,l-i-1):
        temp=tup[j]
        tup[j]=tup[j+1]
        tup[j+1]=temp
print(tup)

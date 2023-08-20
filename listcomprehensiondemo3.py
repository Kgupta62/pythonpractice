'''text=input("type a string")
upperlist=[]
for x in text.split():
    upperlist.append(x.upper())
print(upperlist)'''
text=input("type a string")
upperlist=[x.upper()for x in text.split()]
print(upperlist)


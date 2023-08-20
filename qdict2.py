dict={'a':100,'b':200,'c':300}
list=[]
for i in dict:
    list.append(dict[i])
    final=sum(list)
print(final)
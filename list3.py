list=[1,2,3,4,5]
no=int(input())
list.sort()
for i in range(len(list)-1,len(list)-no-1,-1):
    print(list[i])
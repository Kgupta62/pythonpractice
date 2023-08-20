lis=[1,1,2,3,4,5,3,2,5,6,8,623,4,34,3,543,3,5,2,3]
uniqueList = []
duplicateList = []

for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
       duplicateList.append(i)
       # for i in lis:
       #     if i not in x:
       #         x.append(i)
       # for i in x:
       #     if lis.count(i) > 1:
       #         y.append(i)
print(duplicateList)
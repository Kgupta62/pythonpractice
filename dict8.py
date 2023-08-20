from collections import OrderedDict
input="geeksforgeeks"
k=3
dict=OrderedDict.fromkeys(input,0)
for ch in input:
    dict[ch]+=1
nonRepeat=[key for (key,value) in dict.items() if value==1]
print(nonRepeat)
if len(nonRepeat) <k:
    print("less")
else:
    print(nonRepeat[k-1])

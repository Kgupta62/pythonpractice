from collections import defaultdict
dict={'gfg':[1,2,3],'is':[1,4],'best':[4,2]}
r=defaultdict(list)
for key,val in dict.items():
    for ele in val:
        r[ele].append(key)
print(r)
# print(str(dict(r)))

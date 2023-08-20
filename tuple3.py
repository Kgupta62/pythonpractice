x=(1,2)
y=(3,4)
r=[(a,b) for a in x for b in y]
r=r+[(a,b) for a in y for b in x]
print(r)
# for sorting tuple
# tup.sort(key = lambda x: x[1])
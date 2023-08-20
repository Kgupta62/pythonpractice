tup=(5,20,3,7,6,8)
print("the original tuple is"+str(tup))
k=2
res=[]
tup=list(sorted(tup))
for idx, val in enumerate(tup):
    if idx<k or idx>=len(tup)-k:
        res.append(val)
res=tuple(res)
print("the values:"+str(res))
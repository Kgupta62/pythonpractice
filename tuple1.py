l=[(1,2),(2,3),(6,8),(6,7),(10,14)]
r=[]
for s in l:
    if r and r[-1][0]==s[0]:
        r[-1].extend(s[1:])
    else:
        r.append([e for e in s])
r=list(map(tuple,r))
print(r)
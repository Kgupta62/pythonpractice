t = 'Gfg is best.Gfg also has Classes now.Classes help understand better.'
r = {'Gfg' : 'It', 'Classes' : 'They' }
t = t.split(' ')
res = set()
for i,e in enumerate(t):
    if e in r:
        if e in res:
            t[i] = r[e]
        else:
            res.add(e)
res = ' '.join(t)
print(str(res))
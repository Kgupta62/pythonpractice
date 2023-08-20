dicti = {'gfg': [7, 6, 3],'is': [2, 10, 3],'best': [19, 4]}
y={}
for i in sorted(dicti):
    y[i]=sorted(dicti[i])
print(y)
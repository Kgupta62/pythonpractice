Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
y=[]
for a in Dict:
    q=0
    for i in a:
        if i in arr:
            q+=1
    if (q==len(a)):
        y.append(a)
print(y)
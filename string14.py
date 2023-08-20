s='Geeksforgeeks is best for geeks and CS'
w = ["best", 'CS', 'for']
r = 'gfg'
res = ' '.join([r if i in w else i for i in s.split()])
print(str(res))
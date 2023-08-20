tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict={}
for a,b in tups:
     dict.setdefault(a,[]).append(b)
print(dict)
e = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
r = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}
                               for sub in e]
print(r)
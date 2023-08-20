tup=[(1,2,3),(4,7,8),(9,10,11),(4,7,8),(1,2,3)]
print(tup)
temp=set()
res=[ele for ele in tup if not(tuple(ele)in temp or temp.add(tuple(ele)))]
print(res)
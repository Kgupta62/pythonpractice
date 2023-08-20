def get_numbers(mylist):
    mynumbers=[x for x in mylist if type(x) is int]
    return mynumbers
mylist=[24,23,234,"23","@","$","kubr","ffe","erewf","23234","edfscx"]
print("actuallist",mylist)
print("list with no. only")
mynumbers=get_numbers(mylist)
print(mynumbers)
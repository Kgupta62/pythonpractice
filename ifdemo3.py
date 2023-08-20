a,b,c=input("enter 3 integer").split()
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if a>c:
        print("{0} is greatest".format(a))
    else:
        print("{0} is gretest".format(c))
else:
    if b>c:
        print("{0} is gretest".format(b))
    else:
        print("{0} is gretest".format(c))
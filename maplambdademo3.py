mynum=["jan","feb","march"]
print(list(map(lambda mystring:"even" if len(mystring)%2==0 else mystring[0] ,mynum)))
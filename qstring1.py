def palindrome(a):
    mid=(len(a)-1)//2
    start=0
    last=len(a)-1
    flag=0
    while(start<=mid):
       if(a[start]==a[last]):
          start+=1
       else:
          flag=1
    if(flag==0):
        print("yes")
    else:
        print("no")
def symmetry(string):
    pass

string='amaama'
palindrome(string)
symmetry(string)
'''def removevowels(text):
    mylist=[]
    for x in text:
       if x not in "aieou":
         mylist.append(x)
    return mylist

text=input("type a string")
finallist=removevowels(text)
print(finallist)'''

def removevowels(text):
    mylist=[x for x in text if x not in "aieou"]
    return mylist
text=input("type a string")
finallist=removevowels(text)
print(finallist)
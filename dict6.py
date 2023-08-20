x=input("characters:")
n=int(input("enter a no"))
# create dictionary
original = 'abcdefghijklmnopqrstuvwxyz'
reverse = 'zyxwvutsrqponmlkjihgfedcba'
dic=dict(zip(original,reverse))
prefix=x[0:n-1]
suffix=x[n-1:]
mirror=''
for i in range(0,len(suffix)):
    mirror=mirror+dic[suffix[i]]
print(prefix+mirror)

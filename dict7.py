from collections import Counter
input='python is great and is also great'
input=input.split()
uni=Counter(input)
s=" ".join(uni.keys())
print(s)

# Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

    # If condition is used to store unique string
    # in another list 'k'
    if (s.count(i) >= 1 and (i not in k)):
        k.append(i)
print(' '.join(k))

print(' '.join(dict.fromkeys(s.split())))
print(' '.join(set(s.split())))
s="geeksforgeeks"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
print(str(min(freq,key=freq.get)))
print(str(max(freq,key=freq.get)))
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
x=10
y=linear_search(arr,x)
if y!= -1:
    print(y)
else:
    print("element is  not present")
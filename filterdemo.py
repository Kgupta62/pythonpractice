def check_even(num):
    return num%2==0
mynum=[1,2,3,4,5]
print(list(filter(check_even,mynum)))
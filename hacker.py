# Enter your code here. Read input from STDIN. Print output to STDOUT
a=0
n=int(input())
n1=input()
n2=set(n1.split(" "))
n3=int(input())
for x in range(n3):
    y=input().split(" ")
    if(y[0]=="intersection_update"):
        qa=set(input().split(" "))
        n2.intersection_update(qa)
        print(n2)
        continue
    elif(y[0]=="update"):
        qa1=set(input().split(" "))
        n2.update(qa1)
        print(n2)
        continue
    elif(y[0]=="difference_update"):
        qa2=set(input().split(" "))
        n2.difference_update(qa2)
        print(n2)
        continue
    elif(y[0]=="symmetric_difference_update"):
        qa3=set(input().split(" "))
        n2.symmetric_difference_update(qa3)
        print(n2)
        continue
for x in range(len(n2)):
    a=a+int(x)
print(a)
class A:
    def display(self):
        print("method belongs to A")
# class B(A):
#     pass
class B(A):
    def display(self):
        print("method belongs to A")

b1=B()
b1.display()
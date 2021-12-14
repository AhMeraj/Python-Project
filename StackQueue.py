from abc import ABC
from collections import deque
class arroperation(ABC):
    def __init__(self,a):
        self.a=a
    def display(self):
        print("The final array after operation:",self.a)
class Stack(arroperation):
    def Insertion(self):
        assert len(self.a)<=max,"Stack Overflow."
        item = int(input("Enter your elements:"))
        self.a.append(item)
        self.display()
    def Deletion(self):
        assert a, "Stack Underflow."
        self.a.pop()
        self.display()
class Queue(arroperation):
    def Insertion(self):
        assert len(self.a)<=max,"Stack Overflow."
        item = int(input("Enter your elements:"))
        self.a.append(item)
        self.display()
    def Deletion(self):
        assert a, "Stack Underflow."
        self.a.popleft()
        self.display()
a=deque([])
max=5
k=int(input("1.Stack\t2.Queue\nEnter your way to perform operaiton:"))
arr = [Stack(a), Queue(a)]
C = arr[k - 1]
while('true'):
    l = int(input("1.Insertion\t2.Deletion\t3.Exit\nEnter your choice:"))
    assert l < 3 and l > 0, 'Your operation is finish.'
    if (l == 1):
        C.Insertion()
    elif (l == 2):
        C.Deletion()
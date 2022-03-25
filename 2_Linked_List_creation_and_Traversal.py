class Node:
    def __init__(self,data):
        self.__data= data
        self.next=None

    def get_data(self):
        return self.__data   

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def printll(self):
        node=ll.head
        while(node!=None):
            print(node.get_data())
            node=node.next
  

ll=Linkedlist()

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
ll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None
ll.printll()

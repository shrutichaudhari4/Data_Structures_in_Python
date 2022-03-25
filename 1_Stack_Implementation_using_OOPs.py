# Stack Implementation using OOPS:

class StackImpl:
    def __init__(self,size):
        self.__capacity=size    #self.___capacity, self.__list : private variable
        self.__list=[]          #self.list : public variable

    def isFull(self):
        if(len(self.__list)<self.__capacity):
            return True
        else:
            return False

    def isEmpty(self):
        if(len(self.__list)==0):
            return True
        else:
            return False

    def push(self,value):
        if(self.isFull()):
            self.__list.append(value)
            print(f"{value} is inserted successfully")
        else:
            print("Stack is Full")
            
    def pop(self):
        if(self.isEmpty()):
            print("Stack is Empty")
        else:
            self.__list.pop()

    def get_elements(self):
        return self.__list
    
stack1=StackImpl(5)    #stack1 is an object of class StackImpl
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)

print(stack1.get_elements())
print("After Popping: ")
stack1.pop()
print(stack1.get_elements())

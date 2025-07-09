###########stack implementation using list   1) top?pppek 2)Push 3)pop 4)Is empty or not 5)size
stack=[]
print(type(stack))

class stack_list:
    def __init__(self):
        self.__stack=[]    # __stack for making stack private

    def push (self,data):
        self.__stack.append(data)
        print(f"pushed {data} into stack")

    def size (self):
        return len(self.__stack)

    def is_empty (self):
        return len(self.__stack)==0

    def top(self):
        if self.is_empty():
            print("Stack is empty in top")
            return None
        return self.__stack[-1]

    def pop(self):
        if self.is_empty():
            print("Stack is empty in pop")
            return None
        return self.__stack.pop()

mystack=stack_list()
print(mystack.is_empty())
print(mystack.push(1))
print(mystack.push(2))
print(mystack.push(3))
print(mystack.push(4))
print(mystack.is_empty())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.top())


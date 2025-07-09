#############queue  1)enqueue  2) dequeue 3) is_empty 4) size 5) front #########
class QueueUsingList:
    def __init__(self):
        self.__queue=[] 
    
    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size()==0
    
    def enqueue(self,data):
        self.__queue.append(data)
        return f"We have added {data} to the queue"
    
    def front(self):
        if(self.size()==0):
            print("Queue is empty , cannot show front")
            return None
        return self.__queue[0]
    
    def dequeue(self):
        if(self.size()==0):
            print("Queue is empty , cannot dequeue")
            return None
        
        return self.__queue.pop(0)

Q=QueueUsingList()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
print(Q.size())
print(Q.isEmpty())
print(Q.front())
Q.dequeue()
Q.dequeue()
Q.dequeue()
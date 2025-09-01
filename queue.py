"""
enQueue() Inserts data on the queue
deQueue() pops the first element of the queue
isEmpty() -> checks if the queue is empty
isFull() -> checks if the queue full -- not applicable in python list
peek() -> return the first element of the queue
size() -> returns the SIZE(how many elements) of the queue
"""

class queue:
    def __init__(self):
        self.queue = []
   
    def enqueue(self,element):
        self.queue.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)
    
    def showQueue(self):
        return self.queue
        
myQueue = queue()
myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
myQueue.enqueue("D")
print(myQueue.showQueue())
print("popped element: ",myQueue.dequeue()) #POP
print("Updated Queue: ",myQueue.showQueue()) #SHOW
print("Peek element: ", myQueue.peek()) #PEEk
print("Is Queue empty? ", myQueue.isEmpty()) # ISEMPTY
print("Size of Queue: ", myQueue.size()) #SIZE
        
        
        
        
        
        
        
        
        
        
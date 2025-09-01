"""
STACK

push() -> Inserts data on the top of the stack
pop() -> removes data on the top of the stack
isEmpty() -> checks if the stack is empty
isFull() -> checks if the stack full -- not applicable in python list
peek() -> returns the data at the top of the stack
size() -> returns the SIZE(how many elements) of the stack

"""
class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)
    
    def showStack(self):
        return self.stack
        
myStack = stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.showStack())
print("popped element: ",myStack.pop()) #POP
print("Updated stack: ",myStack.showStack()) #SHOW
print("Peek element: ", myStack.peek()) #PEEk
print("Is stack empty? ", myStack.isEmpty()) # ISEMPTY
print("Size of Stack: ", myStack.size()) #SIZE
print()










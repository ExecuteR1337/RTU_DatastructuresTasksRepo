class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty(): print("Stack is empty")
        else: 
            removed_item = self.stack.pop()
            print(f"Poped: {removed_item}")
        
    def peek(self):
        if self.is_empty(): print("Stack is empty")
        else: print(f"Peek: {self.stack[-1]}")

stack = Stack()
stack.push("Apple")
stack.push("Banana")
stack.push("Apple")
stack.push("Orange")
stack.peek()
stack.pop()
stack.pop()
stack.peek() #By B. Nazarzoda 241ADB013
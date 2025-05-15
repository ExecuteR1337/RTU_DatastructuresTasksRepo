class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty(): print("Queue is empty")
        else:
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")

    def peek(self):
        if self.is_empty(): print("Queue is empty")
        else: print(f"Front: {self.queue[0]}")

queue = Queue()
queue.enqueue("A")
queue.enqueue("C")
queue.enqueue("B")
queue.enqueue("B")
queue.peek()
queue.dequeue()
queue.dequeue()
queue.peek() #By B. Nazarzoda 241ADB013
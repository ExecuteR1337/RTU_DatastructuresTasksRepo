class Array:

    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)
        else:
            print(f"Value not found")

    def search(self, value):
        indexes = []
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                indexes.append(i)
        if indexes:
            print(f"Value {value} found at index(es): {indexes}")
            return indexes
        else:
            print(f"Value {value} not found.")
            return []

    def display(self):
        print(self.arr)

arr = Array()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.insert(10)
arr.display()
arr.search(10)
arr.delete(20)
arr.display()
arr.search(20) #By B. Nazarzoda 241ADB013
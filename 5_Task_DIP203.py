class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next: last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, target):
        current_node = self.head
        if current_node and current_node.data == target:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != target:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None: return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" > ")
            current_node = current_node.next
        print("None")

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

linked_list = LinkedList()
linked_list.insert_at_head('X')
linked_list.insert_at_head('Y')
linked_list.insert_at_tail('Z')
linked_list.display()
linked_list.delete_node('Y')
linked_list.display() #By B. Nazarzoda 241ADB013
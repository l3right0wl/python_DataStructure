# Stack
# Implement Stack ADT using LinkedList

# Declare node class
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Declare stack class
class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
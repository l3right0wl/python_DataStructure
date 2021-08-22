# Queue
# Implement Queue ADT using Array

# Declare queue class
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        item = self.q.pop()
        return item

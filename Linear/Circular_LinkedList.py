# Linked List
# Implement Circular Linked List
# Set start to 0

# Declare node class
# The node has 1 data and 1 pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Declare Circular Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        self.insert(node, self.length())
        return

    def insert(self, node, idx):

        if idx == 1:
            if self.head:
                curn = self.head.next
                cur_i = 1

                while curn.next != self.head:
                    curn = curn.next
                    cur_i += 1

                curn.next = node
                node.next = self.head
                self.head = node
                return
            else:
                self.head = node
                self.head.next = self.head
                return
        else:
            cur_i = 2
            prevn = self.head
            curn = self.head.next

            while curn.next != self.head:
                if cur_i == idx:
                    prevn.next = node
                    node.next = curn
                    return
                prevn = curn
                curn = curn.next
                cur_i += 1

            if cur_i == idx:
                prevn = curn
                curn = curn.next
                prevn.next = node
                node.next = curn
                return
        return

        pass

    def remove(self, idx):
        if idx  == 0:
            if self.head:
                if self.head.next:
                    curn = self.head.next
                    while curn.next != self.head:
                        curn = curn.next
                    curn.next = self.head.next
                    self.head = self.head.next
                    return
                else:
                    self.head = None
                    return
        else:
            prevn = self.head
            curn = self.head.next
            cur_i = 1
            while curn != self.head:
                if cur_i == idx:
                    nextn = curn.next
                    prevn.next = nextn
                    return
                prevn = curn
                curn = curn.next
                cur_i += 1
            return

        pass

    def index(self, idx):
        curn = self.head
        cur_i = 1

        while cur_i != idx:
            curn = curn.next
            cur_i += 1

        return curn

    def length(self):
        return self.count



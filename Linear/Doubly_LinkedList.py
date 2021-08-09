# Linked List
# Implement Doubly Linked List
# Set start to 0

# Declare node class
# The node has 1 data and 2 pointer
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Declare Doubly Linked List Class
class LinkedList:
    # Set start and end
    # cause bidirectional
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
      
    # Add node at last
    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur
            self.tail = cur.next
        self.count += 1

    # Pop node at last
    def pop(self):
        prevn = None

        if self.head:
            cur = self.head
            while cur.next is not None:
                prevn = cur
                cur = cur.next
            # Disconnect previous node
            if cur.next is None:
                prevn.next = None
                self.tail = prevn
        else:
            return None
        self.count -= 1
        return cur.data
    
    # Search
    # Search Data to Front
    def search_front(self, node):
        cur = self.head
        idx = 0

        while cur:
            if cur.data == node.data:
                print("Node[{}] exist index {} in Doubly Linked List".format(node.data, idx+1))
                return idx
            else:
                cur = cur.next
                idx += 1
        return None

    # Search Data to End
    def search_end(self, node):
        cur = self.tail
        idx = 0

        while cur:
            if cur.data == node.data:
                print("Node[{}] exist index {} in Doubly Linked List".format(node.data, self.length()-idx))
                return idx
            else:
                cur = cur.prev
                idx += 1
        return None

    # Print list
    def print_list(self):
        cur = self.head
        strs = ''
        prevn = None
      
        while cur:
            strs += str(cur.data)
            if cur.next and cur.prev == prevn:
                strs += '<->'
            prevn = cur
            cur = cur.next
        print(strs)

    # Length
    def length(self):
        return self.count

    # Insert to desired index
    def insert_idx_node(self, idx, node):
        prevn = None
        cur_i = 1

        if idx == 1:
            if self.head:
                cur = self.head
                cur.prev = node
                node.next = cur
                node.prev = None
                self.head = node
            else:
                self.head = node
        else:
            cur = self.head
            while cur_i < idx:
                if cur:
                    prevn = cur
                    cur = cur.next
                else:
                    return None
                cur_i += 1

            if cur_i == idx:
                node.prev = prevn
                node.next = cur
                prevn.next = node
                if cur:
                    cur.prev = node
            else:
                return None
        self.count += 1
        return

    # remove to desired index
    def remove_idx_node(self, idx):
        prevn = None
        nextn = None
        cur_i = 1
        
        if idx == 1:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
        else:
            cur = self.head
            while cur_i < idx:
                if cur.next:
                    prevn = cur
                    cur = cur.next
                    nextn = cur.next
                else:
                    return
                cur_i += 1

            if cur_i == idx:
                if nextn:
                    nextn.prev = prevn
                prevn.next = nextn
                return
        self.count -= 1
        return

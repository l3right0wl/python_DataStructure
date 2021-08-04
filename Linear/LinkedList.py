# Linked List
# 연결 리스트 구현
# Python의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있다.

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def add(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    def remove(self, val):
        if self.head.data == val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.data == val:
                    self.remove_change_next(val)
                    return
                cur = cur.next
            print(val, "does not exist in linked list")

    def remove_change_next(self, val):
        cur = self.head
        while cur.next is not None:
            if cur.next.data == val:
                nextNode = cur.next.next
                cur.next = nextNode
                break

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.data, '->', end=" ")
            cur = cur.next
        if cur is None:
            print("empty")

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

# 다시
    def search(self, val):
        check = self.head
        for i in range(self.size()):
            if check.data == val:
                print("The data is at the {} index".format((i+1)))
                return None
            check = check.next
        print(val, "does not exist in linked list")
        return None

linked = LinkedList(2)

linked.add(3)
linked.add(4)
linked.add(5)
linked.printlist()

linked.remove(3)
linked.printlist()

linked.search(6)
print(linked.size())
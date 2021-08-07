# Linked List
# Doubly Linked List 구현
# Python의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있지만 직접 구현했다.
# 시작 위치를 1로 잡음

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
      self.head = None
      self.count = 0
      
    # 추가 (마지막 값)
    def add(self, node):
        if self.head:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur
                
        else:
            self.head = node
        self.count += 1
    # 추출 (마지막 값)
    def pop(self):
        cur = self.head
        if self.head:
            while cur.next is not None:
                cur = cur.next
        return cur.data
    
    # 탐색
    def search(self, data):
        idx = 0
        cur = self.head

        while cur:
            if cur.data == data:
                print('{} 번째 위치해있습니다'.format(idx+1))
                return None
            else:
                idx += 1
                cur = cur.next
        return

    # 길이
    def length(self):
        return self.count
      
    # 출력
    def printlist(self):
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
      
      
    # 원하는 위치에 추가
    def insert_idxdata(self, idx, node):
        prevn = None
        nextn = None

        if idx == 1:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
                node.prev = prevn
            else:
                self.head = node
        else:
            cur_i = 1
            cur = self.head
            while cur_i < idx:
                if cur:
                    prevn = cur
                    cur = cur.next
                else:
                    break
                cur_i += 1

            if cur_i == idx:
                node.prev = prevn
                node.next = cur
                prevn.next = node
                if cur:
                    cur.prev = node
            else:
                return
    # 원하는 위치에 삭제
    def remove_idxdata(self, idx):
        pass
  

ll = LinkedList()
ll.add(Node(3))
ll.add(Node(4))
ll.add(Node(5))
ll.add(Node(6))

ll.printlist()
print(ll.length())
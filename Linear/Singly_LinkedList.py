# Linked List
# Singly Linked List 구현
# Python의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있지만 직접 구현했다.
# 시작 위치를 1로 잡음

# Node 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List 클래스 선언
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # 추가 (마지막 값)
    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.count += 1

    # 추출 (마지막 값)
    def pop(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur.data

    # 탐색
    def search(self, node):
        idx = 0
        cur = self.head
        while cur:
            if cur.data == node.data:
                print("{} 번째 위치해있습니다".format(idx+1))
                return None
            else:
                cur = cur.next
                idx += 1
        return None

    # 출력
    def printlist(self):
        strs = ''
        cur = self.head
        while cur:
            strs += str(cur.data)
            if cur.next:
                strs += "->"
            cur = cur.next
        print(strs)

    # 길이
    def length(self):
        return self.count

    # 원하는 위치 추가
    def insert(self, idx, node):
        pre = None
        cur = self.head
        cur_i = 1

        if idx == 1:
            if self.head:
                nextNode = self.head
                self.head = node
                self.head.next = nextNode
            else:
                self.head = node
        else:
            while cur_i < idx:
                if cur:
                    pre = cur
                    cur = cur.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                pre.next = node
                node.next = cur
        self.count += 1
        return None

    # 원하는 위치 삭제
    def delete(self, idx):
        pre = None
        cur = self.head
        cur_i = 1

        if idx == 1:
            self.head = cur.next

        while cur_i < idx:
            if cur:
                pre = cur
                cur = cur.next
            else:
                break
            cur_i += 1

            if cur_i == idx:
                pre.next = cur.next
        self.count -= 1
        return None

class Node(self, data):
    self.prev = None
    self.data = data
    self.next = None
    
class LinkedList(self):
    def __init__(self):
      self.head = None
      
  # 추가 (마지막 값)
    def add(self, node):
        if self.head:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur.next
                
        else:
            self.head = node
  # 추출 (마지막 값)
    def pop(self):
        if self.head:
          cur = self.head
          while cur.next is not None:
            cur = cur.next
            
         return cur.data
      
  # 출력 
   def printlist(self):
      cur = self.head
      strs = ''
      prevn = None
      
      while cur:
          strs += str(cur.data)
          if cur.next and cur.prev == prevn:
              strs += '->'
          prevn = cur
          cur = cur.next
      print(strs)
      
      
  # 원하는 위치에 추가
  def insert_idxdata(self, idx, data)
  
  
  return None
  # 원하는 위치에 삭제 
  def remove_idxdata(self, idx)
  
  pass
  

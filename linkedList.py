class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head

    def get(self, index: int) -> int:
        count = 0
        itr = self.head
        while itr:
            if count == index:
                return itr.val
            itr = itr.next
            count += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        if self.size() == 1:
            self.tail = self.head
        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
        
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size() or not self.head:
            return False
        
        if index == 0: 
            self.head = self.head.next
            if not self.head: 
                self.tail = None
            return True
        
        itr = self.head
        for _ in range(index - 1): 
            if not itr.next:  
                return False
            itr = itr.next
        
      
        itr.next = itr.next.next
        if not itr.next: 
            self.tail = itr
        return True


    def getValues(self):
        List = []
        itr = self.head
        while itr:
            List.append(itr.val)
            itr = itr.next
        return List
        

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
        #deals with out of bounds or an empty list
        if index < 0 or index >= self.size():
            return False
        

        #if removing the head
        if index==0:
            #heads next will always exist or would have been caught by out of bounds
            self.head = self.head.next
            return True
        
        #loop goes until node before desired node
        cursor = self.head
        for i in range(index-1):
            cursor = cursor.next
        #cursor is now at point before desired remove

        #we dont care about the .next.next, all we care about is .(next).next not to be None which it wont be becuase it would have been caught earlier
        cursor.next = cursor.next.next


        #if .next.next does = None then we set the tail to the current cursor aka the one b4 the one we removed
        if not cursor.next:
            self.tail = cursor
        return True



    def getValues(self):
        List = []
        itr = self.head
        while itr:
            List.append(itr.val)
            itr = itr.next
        return List
        

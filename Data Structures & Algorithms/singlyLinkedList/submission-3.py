class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        currNode = self.head.next
        i = 0
        while currNode:
            if i == index:
                return currNode.val
            i += 1
            currNode = currNode.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        firstNode = self.head.next
        newNode.next = firstNode
        self.head.next = newNode
        if not firstNode:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        prevNode = self.head
        currNode = self.head.next
        i = 0
        while currNode:
            if i == index:
                prevNode.next = currNode.next
                if not currNode.next:
                    self.tail = prevNode
                return True
            i += 1
            prevNode = currNode
            currNode = currNode.next
        return False

    def getValues(self) -> list[int]:
        values = []
        currNode = self.head.next
        while currNode:
            values.append(currNode.val)
            currNode = currNode.next
        
        return values
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

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

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        firstNode = self.head.next
        newNode.next = firstNode
        self.head.next = newNode

        if not firstNode:
            self.tail = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        if i == index:
            return self.addAtHead(val)
        prevNode = self.head
        currNode = self.head.next
        newNode = Node(val)
        while currNode:
            if i == index:
                newNode.next = currNode
                prevNode.next = newNode
                return None
            i += 1
            if not currNode.next and i == index:
                return self.addAtTail(val)
            prevNode = currNode 
            currNode = currNode.next
            

    def deleteAtIndex(self, index: int) -> None:
        currNode = self.head.next
        prevNode = self.head
        i = 0
        while currNode:
            if i == index:
                prevNode.next = currNode.next
                if currNode == self.tail:
                    self.tail = prevNode
                return None
            i += 1
            prevNode = currNode
            currNode = currNode.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
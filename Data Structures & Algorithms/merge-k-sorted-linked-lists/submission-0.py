# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeLinked(self, left, right):
        
        dummy = ListNode()
        currNode = dummy
        while left and right:
            if left.val < right.val:
                currNode.next = left
                currNode = left
                left = left.next
            else:
                currNode.next = right
                currNode = right
                right = right.next      
        if left:
            currNode.next = left
        elif right:
            currNode.next = right
        return dummy.next

                
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 0:
            return None
        
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        leftNode = self.mergeSort(left)
        rightNode = self.mergeSort(right)

        return self.mergeLinked(leftNode, rightNode)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        result = self.mergeSort(lists)
        return result

   
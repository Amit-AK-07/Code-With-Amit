class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if head is None:
            new_node.next = new_node
            return new_node

        prev = head
        curr = head.next

        # Case 2: Only one node in the list
        if head.next == head:
            head.next = new_node
            new_node.next = head
            if data < head.data:
                return new_node
            return head

        # Find the last node (prev) to check head/tail insert case
        while prev.next != head:
            prev = prev.next

        # Case 3: Insert before head or after tail
        if data <= head.data or data >= prev.data:
            prev.next = new_node
            new_node.next = head
            if data <= head.data:
                return new_node
            return head

        # Case 4: Insert somewhere in the middle
        prev = head
        curr = head.next
        while curr != head and curr.data < data:
            prev = curr
            curr = curr.next

        prev.next = new_node
        new_node.next = curr
        return head
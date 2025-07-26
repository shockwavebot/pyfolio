
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, first_value: int):
        node = Node(first_value)
        self.head = node
        self.tail = node
        self.size = 1
    
    def append(self, value: int) -> None:
        node = Node(value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def prepend(self, value: int) -> None:
        node = Node(value)
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_after(self, target: int, value: int) -> None:
        current = self.head
        while current.next is not None:
            if current.value == target:
                node = Node(value)
                node.next = current.next
                node.prev = current
                current.next = node
                node.next.prev = node
                self.size += 1
                return
            current = current.next

    def delete(self, target: int) -> None:
        current = self.head
        while current.next is not None:
            if current.value == target:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next



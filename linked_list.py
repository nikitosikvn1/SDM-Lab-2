from typing import Any, List, Optional

# Doubly linked list node class
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.prev = None


# Doubly linked list class
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    # Returns the length of the linked list
    @property
    def length(self) -> int:
        return self.count

    # Adds a new element to the end of the list
    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # Inserts element at index
    def insert(self, data: Any, index: int) -> None:
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")

        new_node = Node(data)

        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.count:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for i in range(index):
                current = current.next
            
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self.count += 1

    # Removes an element by index and returns it
    def delete(self, index: int) -> Any:
        pass

    # Removes all elements in list with value data
    def deleteAll(self, data: Any) -> None:
        pass

    # Returns the element at the specified index
    def get (self, index: int) -> Any:
        pass

    # Returns a copy of the current list
    def clone(self) -> List:
        pass
    
    # Reverses the list
    def reverse(self) -> None:
        pass

    # Looks for the first element with value data from head and returns its index
    def findFirst(self, data: Any) -> int:
        pass

    # Looks for the first element with value data from tail and returns its index
    def findLast(self, data: Any) -> int:
        pass

    # Removes all elements of the list
    def clear(self) -> None:
        pass
    
    # Appends all elements of the given list to the end of the current one
    def extend(self, ex_list: List) -> None:
        pass
    
    # Returns the string representation of the object
    def __str__(self) -> str:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
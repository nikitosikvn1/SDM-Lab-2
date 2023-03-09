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
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        if self.count == 1:
            data = self.head.data
            self.head = None
            self.tail = None
        elif index == 0:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        elif index == self.count - 1:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for i in range(index):
                current = current.next

            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev

        self.count -= 1
        return data

    # Removes all elements in list with value data
    def deleteAll(self, data: Any) -> None:
        current = self.head

        while current:
            if current.data == data:
                if self.count == 1:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.count -= 1
            current = current.next

    # Returns the element at the specified index
    def get (self, index: int) -> Any:
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        current = self.head
        for i in range(index):
            current = current.next

        return current.data

    # Returns a copy of the current list
    def clone(self) -> List:
        new_list = DoublyLinkedList()
        current = self.head

        while current:
            new_list.append(current.data)
            current = current.next

        return new_list
    
    # Reverses the list
    def reverse(self) -> None:
        current = self.head

        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp

        temp = self.head
        self.head = self.tail
        self.tail = temp

    # Looks for the first element with value data from head and returns its index
    def findFirst(self, data: Any) -> int:
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    # Looks for the first element with value data from tail and returns its index
    def findLast(self, data: Any) -> int:
        current = self.tail
        index = self.count - 1

        while current:
            if current.data == data:
                return index
            current = current.prev
            index -= 1
            
        return -1

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
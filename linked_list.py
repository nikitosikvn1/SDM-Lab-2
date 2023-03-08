from typing import Any, Optional

# Doubly linked list node class
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.prev = None
        self.next = None


# Doubly linked list class
class DoublyLinkedList:
    def __init__(self) -> None:
        pass

    # Returns the length of the linked list
    def length(self) -> int:
        pass

    # Adds a new element to the end of the list
    def append(self, data: Any) -> None:
        pass

    # Inserts element at index
    def insert(self, data: Any, index: int) -> None:
        pass

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
    def clone(self) -> DoublyLinkedList:
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
    def extend(self, ex_list: DoublyLinkedList) -> None:
        pass
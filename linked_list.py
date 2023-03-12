from decorators import validate_char_data


# Doubly linked list class
class TypedList:
    def __init__(self) -> None:
        self._list = []

    # Returns the length of the list
    @property
    def length(self) -> int:
        return len(self._list)

    # Adds a new element to the end of the list
    @validate_char_data
    def append(self, data: str) -> None:
        self._list.append(data)

    # Inserts element at index
    @validate_char_data
    def insert(self, data: str, index: int) -> None:
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        self._list.insert(index, data)

    # Removes an element by index and returns it
    def delete(self, index: int) -> str:
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        return self._list.pop(index)

    # Removes all elements in list with value data
    def deleteAll(self, data: str) -> None:
        self._list = [item for item in self._list if item != data]

    # Returns the element at the specified index
    def get(self, index: int) -> str:
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        return self._list[index]

    # Returns a copy of the current list
    def clone(self) -> 'TypedList':
        new_list = TypedList()
        new_list._list = self._list[:]
        
        return new_list
    
    # Reverses the list
    def reverse(self) -> None:
        self._list = self._list[::-1]

    # Looks for the first element with value data from head and returns its index
    def findFirst(self, data: str) -> int:
        for index, item in enumerate(self._list):
            if item == data:
                return index
        return -1

    # Looks for the first element with value data from tail and returns its index
    def findLast(self, data: str) -> int:
        for index in range(len(self._list)-1, -1, -1):
            if self._list[index] == data:
                return index
        return -1

    # Removes all elements of the list
    def clear(self) -> None:
        self._list.clear()
    
    # Appends all elements of the passed list to the end of the current one
    def extend(self, ex_list: 'TypedList') -> None:
        self._list.extend(ex_list._list)
    
    # Returns the string representation of the object
    def __str__(self) -> str:          
        return " -> ".join(self._list)
# Unit tests. CI

## Description
In this lab, 2 types of lists were implemented:
 - **Typed doubly linked list**  
 - **Typed list based on built-in lists**  
Also, tests were written to check the class methods and automatic testing was set up thanks to github actions  

## Variant calculation
```
My variant = 1225 % 4 = 1
```
For the first variant, the first implementation of the list is a **doubly linked list**, the second implementation is a **list based on built-in lists/arrays**  

## Instructions for use
1. First you need to clone the repository on your computer:  
```bash
$ git clone https://github.com/nikitosikvn1/SDM-Lab-2
```
2. To use one of the implementations you can import the DoublyLinkedList/TypedList class and create an instance:
```python
from linked_list import DoublyLinkedList # or TypedList

dll_1 = DoublyLinkedList()
```
3. To run tests:
```bash
$ python -m unittest -v test_linked_list.py
```
You can download the first implementation (Typed Doubly Linked List) in the releases section.

## Reference to the commit the failed CI tests
[Failed commit](https://github.com/nikitosikvn1/SDM-Lab-2/actions/runs/4380709033)

## Conclusion
When writing the first implementation of the list, the unit tests weren't particularly helpful, as I could manually test the newly written method (obviously writing the tests in this case would have taken longer). However, when refactoring for the second implementation of the list, unit tests helped me save time and make sure that the rewritten methods work the same way as in the first implementation.  
However, I am convinced that when creating larger projects, unit tests can be very useful, especially when writing some part of the system takes a long time or when the behavior of the code in various situations is not always predictable for the developer.
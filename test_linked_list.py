import unittest

from linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
    
    def test_length(self):
        self.assertEqual(self.dll.length, 0)

        self.dll.append(1)
        self.assertEqual(self.dll.length, 1)

        self.dll.append(2)
        self.assertEqual(self.dll.length, 2)
    
    def test_append(self):
        self.dll.append(1)
        self.assertEqual(str(self.dll), '1')
        
        self.dll.append(2)
        self.assertEqual(str(self.dll), '1 -> 2')
    
    def test_insert(self):
        self.dll.append(1)
        self.dll.append(3)
        self.dll.insert(2, 1)

        self.assertEqual(str(self.dll), '1 -> 2 -> 3')
    
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.insert(-1, 1)
        with self.assertRaises(IndexError):
            self.dll.insert(10, 1)
    
    def test_delete(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)

        self.assertEqual(self.dll.delete(1), 2)
        self.assertEqual(str(self.dll), '1 -> 3')

        self.assertEqual(self.dll.delete(1), 3)
        self.assertEqual(str(self.dll), '1')

        self.assertEqual(self.dll.delete(0), 1)
        self.assertEqual(str(self.dll), '')
    
    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.delete(-1)
        with self.assertRaises(IndexError):
            self.dll.delete(10)
    
    def test_deleteAll(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(1)

        self.dll.deleteAll(1)
        self.assertEqual(str(self.dll), '2')

        self.dll.deleteAll(2)
        self.assertEqual(str(self.dll), '')
    
    def test_get(self):
        self.dll.append(1)
        self.dll.append(2)

        self.assertEqual(self.dll.get(0), 1)
        self.assertEqual(self.dll.get(1), 2)
    
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.get(-1)
        with self.assertRaises(IndexError):
            self.dll.get(10)
    
    def test_clone(self):
        self.dll.append(1)
        self.dll.append(2)

        clone_dll = self.dll.clone()
        self.assertEqual(str(clone_dll), '1 -> 2')
    
    def test_reverse(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)

        self.dll.reverse()
        self.assertEqual(str(self.dll), '3 -> 2 -> 1')
    
    def test_findFirst(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(1)

        self.assertEqual(self.dll.findFirst(1), 0)
        self.assertEqual(self.dll.findFirst(2), 1)
        self.assertEqual(self.dll.findFirst(3), -1)
    
    def test_findLast(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(1)

        self.assertEqual(self.dll.findLast(1), 2)
        self.assertEqual(self.dll.findLast(2), 1)
        self.assertEqual(self.dll.findLast(3), -1)
    
    def test_clear(self):
        self.dll.append(1)
        self.dll.append(2)

        self.dll.clear()
        self.assertEqual(str(self.dll), '')
    
    def test_extend(self):
        self.dll.append(1)
        self.dll.append(2)

        other_dll = DoublyLinkedList()
        other_dll.append(3)
        other_dll.append(4)

        self.dll.extend(other_dll)
        self.assertEqual(str(self.dll), '1 -> 2 -> 3 -> 4')
    

if __name__ == '__main__':
    unittest.main()
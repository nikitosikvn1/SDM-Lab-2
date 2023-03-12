import unittest

from linked_list import TypedList


class TestTypedList(unittest.TestCase):
    def setUp(self):
        self.dll = TypedList()
    
    def test_length(self):
        self.assertEqual(self.dll.length, 0)

        self.dll.append('a')
        self.assertEqual(self.dll.length, 1)

        self.dll.append('2')
        self.assertEqual(self.dll.length, 2)
    
    def test_append(self):
        self.dll.append('s')
        self.assertEqual(str(self.dll), 's')
        
        self.dll.append('u')
        self.assertEqual(str(self.dll), 's -> u')
    
    def test_insert(self):
        self.dll.append('b')
        self.dll.append('z')
        self.dll.insert('a', 1)

        self.assertEqual(str(self.dll), 'b -> a -> z')
    
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.insert('f', -1)

        with self.assertRaises(IndexError):
            self.dll.insert('7', 10)
        
    def test_validate_char_data_decorator(self):
        with self.assertRaises(TypeError):
            self.dll.insert('foo', 0)

        with self.assertRaises(TypeError):
            self.dll.insert(False, 1)

        with self.assertRaises(TypeError):
            self.dll.append('bar')

        with self.assertRaises(TypeError):
            self.dll.append(127)
    
    def test_delete(self):
        self.dll.append('a')
        self.dll.append('b')
        self.dll.append('c')

        self.assertEqual(self.dll.delete(1), 'b')
        self.assertEqual(str(self.dll), 'a -> c')

        self.assertEqual(self.dll.delete(1), 'c')
        self.assertEqual(str(self.dll), 'a')

        self.assertEqual(self.dll.delete(0), 'a')
        self.assertEqual(str(self.dll), '')
    
    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.delete(-1)

        with self.assertRaises(IndexError):
            self.dll.delete(10)
    
    def test_deleteAll(self):
        self.dll.append('a')
        self.dll.append('b')
        self.dll.append('a')

        self.dll.deleteAll('a')
        self.assertEqual(str(self.dll), 'b')

        self.dll.deleteAll('b')
        self.assertEqual(str(self.dll), '')
    
    def test_get(self):
        self.dll.append('a')
        self.dll.append('b')

        self.assertEqual(self.dll.get(0), 'a')
        self.assertEqual(self.dll.get(1), 'b')
    
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.get(-1)

        with self.assertRaises(IndexError):
            self.dll.get(10)
    
    def test_clone(self):
        self.dll.append('1')
        self.dll.append('2')

        clone_dll = self.dll.clone()
        self.assertEqual(str(clone_dll), '1 -> 2')
    
    def test_reverse(self):
        self.dll.append('1')
        self.dll.append('2')
        self.dll.append('3')

        self.dll.reverse()
        self.assertEqual(str(self.dll), '3 -> 2 -> 1')
    
    def test_findFirst(self):
        self.dll.append('1')
        self.dll.append('2')
        self.dll.append('1')

        self.assertEqual(self.dll.findFirst('1'), 0)
        self.assertEqual(self.dll.findFirst('2'), 1)
        self.assertEqual(self.dll.findFirst('3'), -1)
    
    def test_findLast(self):
        self.dll.append('1')
        self.dll.append('2')
        self.dll.append('1')

        self.assertEqual(self.dll.findLast('1'), 2)
        self.assertEqual(self.dll.findLast('2'), 1)
        self.assertEqual(self.dll.findLast('3'), -1)
    
    def test_clear(self):
        self.dll.append('q')
        self.dll.append('w')

        self.dll.clear()
        self.assertEqual(str(self.dll), '')
    
    def test_extend(self):
        self.dll.append('!')
        self.dll.append('@')

        other_dll = TypedList()
        other_dll.append('#')
        other_dll.append('$')

        self.dll.extend(other_dll)
        self.assertEqual(str(self.dll), '! -> @ -> # -> $')
    

if __name__ == '__main__':
    unittest.main()
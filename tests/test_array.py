import unittest

from src.array import Array 

class TestArray(unittest.TestCase):
    
    def test_append(self):
        arr = Array(8)
        arr.append(5)

        self.assertEqual(arr.size(), 1)
        self.assertEqual(arr.item_at(0), 5)

    def test_insert_index_0(self):
        arr = Array(8)
        arr.append(1)
        arr.append(2)
        arr.insert(3, 0)

        self.assertEqual(arr.size(), 3)
        self.assertEqual(arr.item_at(0), 3)
        self.assertEqual(arr.item_at(1), 1)
        self.assertEqual(arr.item_at(2), 2)

import unittest
from data_structures.arrays.arrays import AshuList

class TestArrays(unittest.TestCase):

    def setUp(self) -> None:
        self.my_list = AshuList(10)

    def test_a_traverse(self):
        self.my_list.data = [23, 87, 71, 57, 42, 12, 13]

        new_list = self.my_list.traverse(0)
        assert new_list == [23, 87, 71, 57, 42, 12, 13]

        new_list = self.my_list.traverse(1)
        assert new_list == [87, 57, 12]

        new_list = self.my_list.traverse(2)
        assert new_list == [71, 12]

    def test_b_arrays_insert(self):
        new_list = self.my_list.insert(0, 23)
        assert new_list == [23, None, None, None, None, None, None, None, None, None]

        new_list = self.my_list.insert(1, 12)
        assert new_list == [23, 12, None, None, None, None, None, None, None, None]

        new_list = self.my_list.insert(2, 42)
        assert new_list == [23, 12, 42, None, None, None, None, None, None, None]

        new_list = self.my_list.insert(2, 57)
        assert new_list == [23, 12, 57, 42, None, None, None, None, None, None]

        new_list = self.my_list.insert(1, 87)
        assert new_list == [23, 87, 12, 57, 42, None, None, None, None, None]

        new_list = self.my_list.insert(2, 71, shift=False)
        assert new_list == [23, 87, 71, 57, 42, 12, None, None, None, None]

        new_list = self.my_list.insert(9, 13)
        assert new_list == [23, 87, 71, 57, 42, 12, 13, None, None, None]

    def test_c_arrays_delete(self):
        self.my_list.data = [23, 87, 71, 57, 42, 12, 13, None, None, None]

        new_list = self.my_list.delete(9)
        assert new_list == [23, 87, 71, 57, 42, 12, 13, None, None]

        new_list = self.my_list.delete(5)
        assert new_list == [23, 87, 71, 57, 42, 13, None, None]

        new_list = self.my_list.delete(3)
        assert new_list == [23, 87, 71, 42, 13, None, None]

        new_list = self.my_list.delete(1)
        assert new_list == [23, 71, 42, 13, None, None]


if __name__ == '__main__':
    unittest.main()
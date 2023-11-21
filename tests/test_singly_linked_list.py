import unittest
from data_structures.linked_lists.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.node = SinglyLinkedList()

    def test_a_traverse(self):
        node = SinglyLinkedList()
        nodes = node.traverse()
        assert nodes == []

        node.append(10)
        nodes = node.traverse()
        assert nodes == [10]

        node.append(20)
        nodes = node.traverse()
        assert nodes == [10, 20]

        node.append(30)
        nodes = node.traverse()
        assert nodes == [10, 20, 30]

    def test_b_count_elements(self):
        node = SinglyLinkedList()
        count = node.count_elements()
        assert count == 0

        node.append(10)
        count = node.count_elements()
        assert count == 1

        node.append(20)
        node.append(30)
        node.append(40)
        node.append(50)
        node.append(60)
        count = node.count_elements()
        assert count == 6

    def test_c_prepend(self):
        node = SinglyLinkedList()
        node.prepend(10)
        node.prepend(20)
        node.prepend(30)
        node.prepend(40)
        nodes = node.traverse()
        assert nodes == [40, 30, 20, 10]

    def test_d_append(self):
        node = SinglyLinkedList()
        node.append(10)
        node.append(20)
        node.append(30)
        node.append(40)
        nodes = node.traverse()
        assert nodes == [10, 20, 30, 40]

    def test_e_insert(self):
        node = SinglyLinkedList()
        node.insert(0, 12)
        node.insert(1, 19)
        node.insert(2, 14)
        node.insert(3, 65)
        node.insert(2, 47)
        node.insert(3, 93)
        nodes = node.traverse()
        assert nodes == [12, 19, 47, 93, 14, 65]

    def test_f_lookup(self):
        node = SinglyLinkedList()
        node.append(10)
        node.append(20)
        node.append(30)
        node.append(40)
        element = node.lookup(1)
        assert element == 20

    def test_g_delete(self):
        node = SinglyLinkedList()
        node.append(10)
        node.append(20)
        node.append(30)
        node.append(40)

        nodes = node.traverse()
        assert nodes == [10, 20, 30, 40]

        node.delete(2)
        nodes = node.traverse()
        assert nodes == [10, 20, 40]


if __name__ == '__main__':
    unittest.main()

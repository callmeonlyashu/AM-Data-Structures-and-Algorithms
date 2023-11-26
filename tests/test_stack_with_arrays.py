import unittest
from data_structures.stack.stack_with_arrays import ArrayStack


class TestStackWithArrays(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = ArrayStack()

    def test_a_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        assert self.stack.pop() == 30
        assert self.stack.pop() == 20
        assert self.stack.count() == 1
        assert self.stack.is_empty() == False
        assert self.stack.is_full() == True
        assert self.stack.peek() == 10


if __name__ == '__main__':
    unittest.main()

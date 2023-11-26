import unittest
from data_structures.queue.queue_with_linked_list import LinkedListQueue


class TestQueueWithLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = LinkedListQueue()

    def test_a_queue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        assert self.queue.dequeue() == 10
        assert self.queue.dequeue() == 20
        assert self.queue.count_elements() == 1
        assert self.queue.is_empty() == False
        assert self.queue.is_full() == True
        assert self.queue.peek() == 30


if __name__ == '__main__':
    unittest.main()

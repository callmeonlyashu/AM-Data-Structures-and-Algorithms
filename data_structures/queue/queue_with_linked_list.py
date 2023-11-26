class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.current_node = None

    def enqueue(self, value):
        """
        Push the value to the queue

        Parameters:
            value (int): value to be inserted in the queue

        Returns:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        """
        Popped up the last value of queue

        Parameters:

        Returns:
            data (int): Returns queue value
        """
        if self.head is None:
            raise Exception("queue is empty")

        current_node = self.head
        self.head = current_node.next

        return current_node.data

    def count_elements(self):
        """
        Returns the count for elements in the
        queue.

        Parameters:

        Returns:
                count (int): Count of queue elements
        """
        count = 0

        if self.head is not None:
            current_node = self.head
            while current_node.next:
                count += 1
                current_node = current_node.next

            return count + 1
        return count

    def peek(self):
        """
        Returns the element at the top of the queue if queue is not empty

        Parameters:

        Returns:
                value (int): queue element
        """
        if self.head is None:
            raise Exception("queue is empty")

        current_node = self.head
        self.head = current_node.next

        return current_node.data

    def is_empty(self):
        """
        Returns true if queue is empty

        Parameters:

        Returns:
                value (boolean): True if queue is empty
        """
        return self.count_elements() == 0

    def is_full(self):
        """
        Returns true if queue is not empty

        Parameters:

        Returns:
                value (boolean): True if queue is not empty
        """
        return self.count_elements() != 0
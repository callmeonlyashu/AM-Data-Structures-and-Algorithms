class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """
        Push the value to the Queue

        Parameters:
            value (int): value to be inserted in the queue

        Returns:
        """
        self.queue.append(value)
        return self.queue

    def dequeue(self):
        """
        Popped up the last value of queue

        Parameters:

        Returns:
            data (int): Returns queue value
        """
        element = self.queue[0]
        del self.queue[0]
        return element

    def count(self):
        """
        Returns the count for elements in the
        queue.

        Parameters:

        Returns:
                count (int): Count of queue elements
        """
        return len(self.queue)

    def peek(self):
        """
        Returns the element at the top of the queue if queue is not empty

        Parameters:

        Returns:
                value (int): queue element
        """
        element = self.queue[0]
        return element

    def is_empty(self):
        """
        Returns true if queue is empty

        Parameters:

        Returns:
                value (boolean): True if queue is empty
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Returns true if queue is not empty

        Parameters:

        Returns:
                value (boolean): True if queue is not empty
        """
        return len(self.queue) != 0
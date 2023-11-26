class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        Push the value to the stack

        Parameters:
            value (int): value to be inserted in the Stack

        Returns:
        """
        self.stack.append(value)
        return self.stack

    def pop(self):
        """
        Popped up the last value of Stack

        Parameters:

        Returns:
            data (int): Returns Stack value
        """
        element = self.stack[-1]
        del self.stack[-1]
        return element

    def count(self):
        """
        Returns the count for elements in the
        Stack.

        Parameters:

        Returns:
                count (int): Count of Stack elements
        """
        return len(self.stack)

    def peek(self):
        """
        Returns the element at the top of the stack if stack is not empty

        Parameters:

        Returns:
                value (int): Stack element
        """
        element = self.stack[-1]
        return element

    def is_empty(self):
        """
        Returns true if stack is empty

        Parameters:

        Returns:
                value (boolean): True if stack is empty
        """
        return len(self.stack) == 0

    def is_full(self):
        """
        Returns true if stack is not empty

        Parameters:

        Returns:
                value (boolean): True if stack is not empty
        """
        return len(self.stack) != 0
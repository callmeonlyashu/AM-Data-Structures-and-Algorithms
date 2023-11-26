class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.current_node = None

    def push(self, value):
        """
        Push the value to the stack

        Parameters:
            value (int): value to be inserted in the Stack

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

    def pop(self):
        """
        Popped up the last value of Stack

        Parameters:

        Returns:
            data (int): Returns Stack value
        """
        if self.head is None:
            raise Exception("Stack is empty")

        current_node = self.head
        prev_node = None
        while current_node.next:
            try:
                if  current_node.next.next == None:
                    prev_node = current_node
            except:
                pass
            current_node = current_node.next
            if prev_node:
                prev_node.next = None

        return current_node.data

    def count_elements(self):
        """
        Returns the count for elements in the
        Stack.

        Parameters:

        Returns:
                count (int): Count of Stack elements
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
        Returns the element at the top of the stack if stack is not empty

        Parameters:

        Returns:
                value (int): Stack element
        """
        if self.head is None:
            raise Exception("Stack is empty")

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        return current_node.data

    def is_empty(self):
        """
        Returns true if stack is empty

        Parameters:

        Returns:
                value (boolean): True if stack is empty
        """
        return self.count_elements() == 0

    def is_full(self):
        """
        Returns true if stack is not empty

        Parameters:

        Returns:
                value (boolean): True if stack is not empty
        """
        return self.count_elements() != 0
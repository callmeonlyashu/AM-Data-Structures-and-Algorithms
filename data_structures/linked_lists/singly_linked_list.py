class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.current_node = None

    def count_elements(self):
        """
        Returns the count for elements in the
        linked list.

        Parameters:

        Returns:
                count (int): Count of linked list elements
        """
        count = 0

        if self.head is not None:
            current_node = self.head
            while current_node.next:
                count += 1
                current_node = current_node.next

            return count + 1
        return count

    def traverse(self):
        """
        Returns the elements in the
        linked list.

        Parameters:

        Returns:
                elements (list): Linked list elements
        """
        elements = []

        if self.head:
            current_node = self.head
            while current_node.next:
                elements.append(current_node.data)
                current_node = current_node.next
            elements.append(current_node.data)
        return elements

    def append(self, value):
        """
        Insert the value at the end of the linked list.

        Parameters:
            value (int): value to be inserted in the linked list

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

    def prepend(self, value):
        """
        Insert the value at the beginning of the linked list.

        Parameters:
            value (int): value to be inserted in the linked list

        Returns:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            self.head = new_node
            self.head.next = current_node

    def insert(self, index, value):
        """
        Insert the value at the index passed in the linked list.

        Parameters:
            index (int): index (starts from 0)
            value (int): value to be inserted in the linked list

        Returns:
        """

        total_elements = self.count_elements()
        if index == 0 or total_elements == 0:
            self.prepend(value)
        elif index == total_elements:
            self.append(value)
        elif index > total_elements:
            raise Exception("Index out of bounds")
        else:
            new_node = Node(value)
            prev_node = self.head
            prev_node_index = 0
            while prev_node.next:
                if prev_node_index == index-1:
                    break
                prev_node = prev_node.next
                prev_node_index += 1

            current_node = prev_node.next
            prev_node.next = new_node
            new_node.next = current_node

    def delete(self, index):
        """
        deletes the value at the index in the linked list.

        Parameters:
            index (int): index (starts from 0)

        Returns:
        """
        total_elements = self.count_elements()

        if self.head is None or index > total_elements:
            raise Exception("Index out of bounds")

        current_node = self.head
        current_node_index = 0

        prev_node = current_node
        while current_node.next:
            if current_node_index == index - 1:
                prev_node = current_node
            if current_node_index == index:
                break
            current_node_index += 1
            current_node = current_node.next

        prev_node.next = current_node.next

    def lookup(self, index):
        """
        Returns the value at the index in the linked list.

        Parameters:
            index (int): index (starts from 0)

        Returns:
            value (int): value at the index
        """
        total_elements = self.count_elements()

        if self.head is None or index > total_elements:
            raise Exception("Index out of bounds")

        current_node = self.head
        current_node_index = 0
        while current_node.next:
            if current_node_index == index:
                break
            current_node_index += 1
            current_node = current_node.next

        return current_node.data
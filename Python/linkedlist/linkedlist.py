from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        # returns the size of the list
        return self._size

    def __getitem__(self, index):
        # a = list[6] - Searching through the linked list
        # a = list.get(6)
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, value):
        # list[5] = 9
        # list.set(5, 9)
        pointer = self._getnode(index)
        if pointer:
            pointer.data = value
        else:
            raise IndexError("list index out of range")

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def append(self, element):
        if self.head:
            # insertion when the list has already elements
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            # first insertion
            self.head = Node(element)

        self._size = self._size + 1

    def index(self, element):
        # returns the index of the element in the list
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == element:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError(f"{element} is not in list")

    def insert(self, index, element):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node = Node(element)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, element):
        if self.head is None:
            raise ValueError(f"{element} is not in list")
        elif self.head.data == element:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
                self._size = self._size - 1
            return True
        raise ValueError(f"{element} is not in list")


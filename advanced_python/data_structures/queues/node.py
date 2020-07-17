class Node:
    """
    This Node class has been created for you.
    It contains the necessary properties for the solution, which are:
    - name
    - phone
    - next
    """

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.__next = None

    def set_next(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type Node or None.")

    def get_next(self):
        return self.__next

    def print_details(self):
        print("{} ({})".format(self.name, self.phone))

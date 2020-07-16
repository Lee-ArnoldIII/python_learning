import unittest
from unittest import TestCase
from node import Node
from linked_lists import LinkedList


class TestLinkedList(TestCase):
    """
    This class tests that your LinkedList class was implemented correctly.
    All you have to do is run this file.

    If any tests fail, then you are not done yet.
    If all tests pass, good job! You can move on to the next challenge.
    """

    def test_node_creation(self):
        name = "Jose"
        matric = "1234"
        year = 2

        node = Node(name, matric, year)

        self.assertEqual(name, node.name)
        self.assertEqual(matric, node.matric)
        self.assertEqual(year, node.year)

    def test_list_creation(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.get_root())

    def test_add_to_list(self):
        name = "Jose"
        matric = "1234"
        year = 2

        node = Node(name, matric, year)

        linked_list = LinkedList()

        linked_list.add_to_list(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_add_many_to_list(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), ("Anna", "3456", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_find_in_list(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), ("Anna", "3456", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find(marker.name), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError):
            linked_list.find("Smith")

if __name__=='__main__':
    unittest.main()
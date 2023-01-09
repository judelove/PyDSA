import unittest
from unittest import TestCase

from linked_lists.linkedlist import Node


class TestNode(TestCase):
    linked_list = None

    @classmethod
    def setUpClass(cls) -> None: cls.linked_list = Node("head")

    def test_append(self):
        self.assertIsNone(self.linked_list.next)
        self.linked_list.append(Node("first child"))
        self.assertIsNotNone(self.linked_list.next)
        self.assertRaises(Exception, self.linked_list.append, "hello")

    def test_next(self):
        self.assertEqual(self.linked_list.next.value, "first child")

    def test_value(self):
        self.assertEqual(self.linked_list.value, "head")

    def test_size(self):
        self.assertTrue(self.linked_list.size == 2)


if __name__ == 'main':
    unittest.main()

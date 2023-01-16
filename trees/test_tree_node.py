from unittest import TestCase

from trees.tree_node import TreeNode


class TestTreeNode(TestCase):
    tree = None

    @classmethod
    def setUpClass(cls) -> None: tree = None

    def test_value(self):
        self.tree = TreeNode("root")
        self.assertEqual("root", self.tree.value)

    def test_value(self):
        self.tree = TreeNode("root")
        self.tree.value = "parent"
        self.assertEqual(self.tree.value, "parent")

    def test_left(self):
        self.tree = TreeNode("root")
        self.tree.left = "left"
        self.assertEqual(self.tree.left.value, "left")

    def test_right(self):
        self.tree = TreeNode("root")
        self.tree.left = "right"
        self.assertEqual(self.tree.left.value, "right")

    def test_contains(self):
        self.tree = TreeNode("root")
        self.tree.left = "right"
        self.assertTrue(self.tree.contains("right"))

    def test_height(self):
        self.tree = TreeNode("root")
        self.tree.left = "right"
        self.assertEqual(self.tree.height, 2)
from unittest import TestCase

from tries.TrieNode import TrieNode


class TestTrieNode(TestCase):
    trie = None

    @classmethod
    def setUpClass(cls) -> None: cls.trie = TrieNode(); cls.trie.add_word("test"); cls.trie.add_word("helm")

    def test_contains_word(self):
        self.assertTrue(self.trie.contains_word("test"))
        self.assertFalse(self.trie.contains_word("tes"))

    def test_size(self):
        self.assertEqual(self.trie.size, 2)
        self.trie.add_word("test")
        self.assertNotEqual(self.trie.size, 3)
        self.trie.add_word("tests")
        self.assertEqual(self.trie.size, 3)

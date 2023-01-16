from unittest import TestCase

from tries.TrieNode import TrieNode


class TestTrieNode(TestCase):

    trie = None

    @classmethod
    def setUpClass(cls) -> None: cls.trie = TrieNode(); cls.trie.add_word("test")

    def test_contains_word(self):
        self.assertTrue(self.trie.contains_word("test"))
        self.assertFalse(self.trie.contains_word("tes"))


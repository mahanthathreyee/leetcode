'''
Problem: Implement Trie (Prefix Tree)
Link: https://leetcode.com/problems/implement-trie-prefix-tree/
Tags: True, Hashtable, String
'''

__end__ = '__end__'


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node[__end__] = True

    def search(self, word: str) -> bool:
        node = self._get_pre_node(word)
        return (node is not None) and (__end__ in node)

    def startsWith(self, prefix: str) -> bool:
        node = self._get_pre_node(prefix)
        return node is not None

    def _get_pre_node(self, prefix: str) -> dict:
        node = self.root

        for c in prefix:
            if c not in node:
                return None
            node = node[c]

        return node

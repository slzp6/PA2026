"""c10_14.py"""
# pylint: disable=too-few-public-methods


class Node:
    """trie node class"""

    def __init__(self):
        self.child = [None] * 26
        self.end = False


def insert(root, key):
    """trie node insert"""
    curr = root
    for i in key:
        idx = ord(i) - ord('a')
        if curr.child[idx] is None:
            node_new = Node()
            curr.child[idx] = node_new
        curr = curr.child[idx]
    curr.end = True


def search(root, key):
    """trie node search"""
    curr = root
    for i in key:
        idx = ord(i) - ord('a')
        if curr.child[idx] is None:
            return False
        curr = curr.child[idx]
    return curr.end


trie = Node()
words_insert = ['bag', 'bar', 'bark']
words_search = ['bag', 'bee', 'bark']

for word in words_insert:
    insert(trie, word)

print(words_insert)
for word in words_search:
    stat = search(trie, word)
    print(f"{word}, {stat}")

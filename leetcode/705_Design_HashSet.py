class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()


    def add(self, key: int) -> None:
        self.hash.add(key)


    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash:
            return True
        return False


class MyHashSetWithoutBuiltIn:

    def __init__(self):
        self.hash = [[] for _ in range(100)]

    def add(self, key: int) -> None:
        l = self.hash[key % 100]
        if key in l:
            return
        self.hash[key % 100].append(key)


    def remove(self, key: int) -> None:
        l = self.hash[key % 100]
        if key in l:
            l.remove(key)

    def contains(self, key: int) -> bool:
        l = self.hash[key % 100]
        if key in l:
            return True
        return False


class MyHashSetLinkedList:

    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key: int):
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket = self.bucket_array[self._hash(key)]
        bucket.insert(key)

    def remove(self, key: int) -> None:
        bucket = self.bucket_array[self._hash(key)]
        bucket.delete(key)

    def contains(self, key: int) -> bool:
        bucket = self.bucket_array[self._hash(key)]
        return bucket.exists(key)


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, val: int):
        node = self.head
        while node.next:
            if node.next.val == val:
                return
            node = node.next
        node.next = Node(val)

    def delete(self, val: int):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur.next = None
                return

            prev = cur
            cur = cur.next

    def exists(self, val: int):
        node = self.head.next
        while node:
            if node.val == val:
                return True
            node = node.next
        return False


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None

    def insert(self, val: int):
        if self.head is None:
            self.head = TreeNode(val)
            return self.head

        node = self.head
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    node = None
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    node = None
            else:
                break


    def search(self, val: int) -> bool:
        node = self.head

        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                return True

        return False


    def delete(self, val: int):
        node = self.head


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket = [BST() for _ in range(self.key_range)]


    def _hash(self, key: int):
        return key % self.key_range


    def add(self, key: int) -> None:
        bst = self.bucket[self._hash(key)]
        bst.insert(key)


    def remove(self, key: int) -> None:
        bst = self.bucket[self._hash(key)]
        bst.delete(key)


    def contains(self, key: int) -> bool:
        bst = self.bucket[self._hash(key)]
        return bst.search(key)
from typing import List
from common.node import TreeNode, inorder_traverse


class BST:
    def insert(self, node: TreeNode, val: int):
        if node is None or node.val == val:
            return

        if val < node.val:
            if node.left:
                self.insert(node.left, val)
            else:
                node.left = TreeNode(val)
        if val > node.val:
            if node.right:
                self.insert(node.right, val)
            else:
                node.right = TreeNode(val)


    def search(self, node: TreeNode, val: int) -> bool:
        if node is None:
            return False

        if node.val == val:
            return True

        left = self.search(node.left, val)
        right = self.search(node.right, val)

        return left or right


    def delete(self, node: TreeNode, val: int):
        if node is None:
            return

        if val < node.val:
            node.left = self.delete(node.left, val)

        if val > node.val:
            node.right = self.delete(node.right, val)

        if val == node.val:
            if node.left and node.right:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right

                node.val = predecessor.val
                predecessor.val = val
                node.left = self.delete(node.left, val)
            elif node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                return None

        return node


def test_bst():
    bst = BST()

    root = TreeNode(5)
    assert inorder_traverse(root) == [5]

    bst.insert(root, 2)
    assert inorder_traverse(root) == [2, 5]

    bst.insert(root, 8)
    assert inorder_traverse(root) == [2, 5, 8]

    bst.insert(root, 1)
    assert inorder_traverse(root) == [1, 2, 5, 8]

    bst.insert(root, 6)
    assert inorder_traverse(root) == [1, 2, 5, 6, 8]

    bst.insert(root, 7)
    assert inorder_traverse(root) == [1, 2, 5, 6, 7, 8]

    bst.insert(root, 12)
    assert inorder_traverse(root) == [1, 2, 5, 6, 7, 8, 12]

    bst.insert(root, 9)
    assert inorder_traverse(root) == [1, 2, 5, 6, 7, 8, 9, 12]

    bst.insert(root, 13)
    assert inorder_traverse(root) == [1, 2, 5, 6, 7, 8, 9, 12, 13]

    assert bst.search(root, 5) == True
    assert bst.search(root, 3) == False

    # if left and right exist
    bst.delete(root, 8)
    assert inorder_traverse(root) == [1, 2, 5, 6, 7, 9, 12, 13]

    # if left and right is None
    bst.delete(root, 1)
    assert inorder_traverse(root) == [2, 5, 6, 7, 9, 12, 13]
    bst.delete(root, 2)
    assert inorder_traverse(root) == [5, 6, 7, 9, 12, 13]

    # if left is None
    bst.delete(root, 7)
    assert bst.search(root, 7) == False
    assert inorder_traverse(root) == [5, 6, 9, 12, 13]

    # if right is None
    bst.insert(root, 2)
    bst.insert(root, 1)
    bst.delete(root, 2)
    assert inorder_traverse(root) == [1, 5, 6, 9, 12, 13]

    # delete root node
    bst.delete(root, 5)
    assert inorder_traverse(root) == [1, 6, 9, 12, 13]

from common.node import TreeNode


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.index = 0
        self.nodes = self._initialize(root)


    def _initialize(self, node):
        res = []

        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)

            if node.right:
                node = node.right
            else:
                node = None

        return res

    def next(self) -> int:
        #print(self.index, self.nodes)
        if self.hasNext():
            index = self.index
            self.index += 1
            return self.nodes[index]

    def hasNext(self) -> bool:
        if self.index < len(self.nodes):
            return True
        return False


class BSTIteratorDFS:
    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1

        self._inorder(root)

    def _inorder(self, node: TreeNode):
        if node is None:
            return
        self._inorder(node.left)
        self.nodes_sorted.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        if self.index + 1 < len(self.nodes_sorted):
            return True
        return False


class BSTIteratorControlledRecursion:
    def __init__(self, root: TreeNode):
        self.stack = []

        self._leftmost_inorder(root)


    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
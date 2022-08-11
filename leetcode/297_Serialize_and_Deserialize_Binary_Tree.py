from collections import deque
from typing import List

from common.node import TreeNode, make_tree_node, compare_tree_node


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        dq = deque([root])

        ret = []
        while dq:
            cur_node = dq.popleft()
            ret.append(cur_node.val if cur_node else None)
            if cur_node is None:
                continue

            dq.append(cur_node.left)
            dq.append(cur_node.right)

        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        root = TreeNode(data[0])
        idx = 1
        dq = deque([root])
        while dq and idx < len(data):
            cur_node = dq.popleft()

            if data[idx] is not None:
                cur_node.left = TreeNode(data[idx])
                dq.append(cur_node.left)

            idx += 1
            if idx < len(data) and data[idx] is not None:
                cur_node.right = TreeNode(data[idx])
                dq.append(cur_node.right)

            idx += 1

        return root


class Codec2:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        nodes = []
        while queue:
            node = queue.popleft()
            if not node:
                nodes.append("null")
                continue

            nodes.append(f"{node.val}")

            queue.append(node.left)
            queue.append(node.right)

        while nodes and nodes[-1] == "null":
            nodes.pop()

        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = [
            TreeNode(int(val)) if val != "null" else None for val in data.split(",")
        ]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if not node:
                continue

            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

        return root


class Codec3:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        nodes = []
        while queue:
            node = queue.popleft()
            if not node:
                nodes.append("#")
                continue

            nodes.append(f"{node.val}")

            queue.append(node.left)
            queue.append(node.right)

        return " ".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None

        datas = data.split()

        index = 1
        root = TreeNode(int(datas[0]))

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if datas[index] != "#":
                node.left = TreeNode(int(datas[index]))
                queue.append(node.left)
            index += 1

            if datas[index] != "#":
                node.right = TreeNode(int(datas[index]))
                queue.append(node.right)
            index += 1

        return root


def check_case(s: Codec, data: list[int | None]):
    root = make_tree_node(data)
    assert compare_tree_node(s.deserialize(s.serialize(root)), root)


def check_cases(s: Codec):
    check_case(s, [])
    check_case(s, [1])
    check_case(s, [1, 2, 3, None, None, 4, 5])


def test_codec():
    check_cases(Codec())


def test_codec2():
    check_cases(Codec2())


def test_codec3():
    check_cases(Codec3())

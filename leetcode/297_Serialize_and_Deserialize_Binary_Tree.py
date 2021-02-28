from collections import deque
from typing import List

from common.node import TreeNode


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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class CodecDFS:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root: TreeNode, string: str) -> str:
            if root is None:
                string += "None,"
            else:
                string += f"{root.val},"
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)

            return string

        return rserialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")

        def rdeserialize(l: List[str]) -> TreeNode:
            if l[0] == "None":
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

            return root

        return rdeserialize(data)

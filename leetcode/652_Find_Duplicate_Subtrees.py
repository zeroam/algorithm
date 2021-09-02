from collections import defaultdict
from typing import Optional, List

from common.node import TreeNode


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        hash_map = defaultdict(lambda: 0)
        result = []

        def postorder(node: Optional[TreeNode]):
            if node is None:
                return "#"

            serial = f"{node.val},{postorder(node.left)},{postorder(node.right)}"
            hash_map[serial] += 1
            if hash_map[serial] == 2:
                result.append(node)

            return serial

        postorder(root)

        return result

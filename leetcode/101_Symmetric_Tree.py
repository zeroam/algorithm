from collections import deque
from typing import List
from common.node import TreeNode, make_tree_node

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        dq = deque([root])

        while dq:
            mirror = []
            for _ in range(len(dq)):
                node = dq.popleft()
                mirror.append(node.val if node else None)

                if node:
                    dq.append(node.left)
                    dq.append(node.right)

            mirror_size = len(mirror)
            for i in range(mirror_size // 2):
                if mirror[i] != mirror[mirror_size - i - 1]:
                    return False

        return True


def check_solution(l: List[int], expect: bool) -> None:
    s = Solution()

    assert s.isSymmetric(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solution([1, 2, 2, 3, 4, 4, 3], True)
    check_solution([1, 2, 2, None, 3, None, 3], False)

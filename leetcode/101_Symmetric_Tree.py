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


class SolutionRecur:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)


class SolutionIter:
    def isSymmetric(self, root: TreeNode) -> bool:
        dq = deque([root, root])

        while dq:
            t1 = dq.popleft()
            t2 = dq.popleft()

            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            dq.append(t1.left)
            dq.append(t2.right)
            dq.append(t1.right)
            dq.append(t2.left)

        return True


def check_solution(l: List[int], expect: bool) -> None:
    s = Solution()
    s_recur = SolutionRecur()
    s_iter = SolutionIter()

    assert s.isSymmetric(make_tree_node(l)) == expect
    assert s_recur.isSymmetric(make_tree_node(l)) == expect
    assert s_iter.isSymmetric(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solution([1, 2, 2, 3, 4, 4, 3], True)
    check_solution([1, 2, 2, None, 3, None, 3], False)

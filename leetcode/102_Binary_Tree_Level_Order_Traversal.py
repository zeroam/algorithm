from typing import List
from collections import deque
from common.node import make_tree_node, TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        dq = deque([[root]])
        output = []

        while dq:
            level = dq.popleft()
            next_level = []
            output_item = []
            for curr in level:
                output_item.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)

                if curr.right:
                    next_level.append(curr.right)

            if next_level:
                dq.append(next_level)

            output.append(output_item)

        return output


def check_solution(case: List[int], expect: List[List[int]]):
    s = Solution()

    assert s.levelOrder(make_tree_node(case)) == expect



if __name__ == "__main__":
    check_solution([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]])
    check_solution([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])

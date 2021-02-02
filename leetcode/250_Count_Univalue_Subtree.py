from typing import List, Optional
from common.node import TreeNode, make_tree_node


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        if root is None:
            return self.count

        def search_subtree(node: TreeNode, parent_node: TreeNode) -> bool:
            if node is None:
                return parent_node.val

            left = search_subtree(node.left, node)
            right = search_subtree(node.right, node)
            if left == right and right == node.val:
                self.count += 1
                return node.val
            else:
                return None

        search_subtree(root, root)
        return self.count


class SolutionDFS1:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):
        # base case - if node has no children this is a univalue subtree
        if node.left is None and node.right is None:
            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtree and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni


class SolutionDFS2:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        # considered a valid subtree
        if node is None:
            return True

        # check if node.left and node.right are univalue subtree of value node.val
        if not all([self.is_valid_part(node.left, node.val), self.is_valid_part(node.right, node.val)]):
            return False

        # if it passwd the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val


def check_solution(l: List[Optional[int]], expect: int) -> None:
    s = Solution()
    s_dfs1 = SolutionDFS1()
    s_dfs2 = SolutionDFS1()

    assert s.countUnivalSubtrees(make_tree_node(l)) == expect
    assert s_dfs1.countUnivalSubtrees(make_tree_node(l)) == expect
    assert s_dfs2.countUnivalSubtrees(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solution([5, 1, 5, 5, 5, None, 5], 4)
    check_solution([], 0)
    check_solution([5, 5, 5, 5, 5, None, 5], 6)

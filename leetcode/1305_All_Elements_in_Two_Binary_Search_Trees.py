from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root: TreeNode, result=[]):
            if root is None:
                return None
            
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
            
        list1, list2 = [], []
        result = []
        inorder(root1, list1)
        inorder(root2, list2)
        
        idx1, idx2 = 0, 0
        while idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] < list2[idx2]:
                result.append(list1[idx1])
                idx1 += 1
            else:
                result.append(list2[idx2])
                idx2 += 1
        
        return result + list1[idx1:] + list2[idx2:]


def insert_node(root: TreeNode, val: int) -> None:
    if root is None:
        return None

    if root.val is None:
        root.val = val
        return

    if val < root.val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insert_node(root.left, val)
    if val > root.val:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            insert_node(root.right, val)


def test_solution(s: Solution, nums1: List[int], nums2: List[int], expect: List[int]) -> None:
    if len(nums1) == 0:
        root1 = None
    else:
        root1 = TreeNode()
        for num in nums1:
            insert_node(root1, num)

    if len(nums2) == 0:
        root2 = None
    else:
        root2 = TreeNode()
        for num in nums2:
            insert_node(root2, num)

    assert s.getAllElements(root1, root2) == expect


if __name__ == "__main__":
    s = Solution()

    nums1 = [2, 1, 4]
    nums2 = [1, 0, 3]
    expect = [0, 1, 1, 2, 3, 4]
    test_solution(s, nums1, nums2, expect)

    nums1 = [0, -10, 10]
    nums2 = [5, 1, 7, 0 ,2]
    expect = [-10, 0, 0, 1, 2, 5, 7, 10]
    test_solution(s, nums1, nums2, expect)

    nums1 = [0, -10, 10]
    nums2 = []
    expect = [-10, 0, 10]
    test_solution(s, nums1, nums2, expect)

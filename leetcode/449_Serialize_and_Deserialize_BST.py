from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        
        dq = deque()
        dq.append(root)
        
        result = []
        while dq:
            cur_node = dq.popleft()
            if cur_node is None:
                continue
                
            result.append(cur_node.val)

            dq.append(cur_node.left)
            dq.append(cur_node.right)
                
        print(result)
        return ",".join(map(str, result))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        
        nums = list(map(int, data.split(",")))
        root = None
        for num in nums:
            root = self._insert_node(num, root)
        return root
    
    def _insert_node(self, val: int, head: TreeNode):
        if head is None:
            return TreeNode(val)
        
        if val < head.val:
            head.left = self._insert_node(val, head.left)
        else:
            head.right = self._insert_node(val, head.right)
                
        return head
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
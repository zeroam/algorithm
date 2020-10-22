# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        def copyNode(origin: 'Node', copy: 'Node'):
            if origin.neighbors == []:
                return
            
            for neighbor in origin.neighbors:
                used = False
                for used_node in used_nodes:
                    if neighbor.val == used_node.val:
                        copy.neighbors.append(used_node)
                        used = True
                        
                if used:
                    continue
                    
                new_node = Node(neighbor.val)
                copy.neighbors.append(new_node)
                used_nodes.append(new_node)
                
                copyNode(neighbor, new_node)
        
        root = Node(node.val)
        used_nodes = [root]
        copyNode(node, root)
        
        return root
    

class SolutionOrigin:
    def __init__(self):
        # Dictonary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # If the node was already visited before.
        # Return the clone from the visited dictionary
        if node in self.visited:
            return self.visited[node]
        
        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as row, hence []
        clone_node = Node(node.val, [])
        
        # The key is origin node and value being the clone node
        self.visited[node] = clone_node
        
        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node
        
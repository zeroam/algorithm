from collections import defaultdict
from typing import List


class SolutionGraph:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graphs = defaultdict(defaultdict)
        
        def backtrack(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            
            ret = -1.0
            if curr_node not in graphs:
                return ret
            
            neighbors = graphs[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for next_node, value in neighbors.items():
                    if next_node in visited:
                        continue
                        
                    ret = backtrack(next_node, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
                        
            visited.remove(curr_node)
            return ret
        
        # Step 1. make graphs
        for (dividend, divider), value in zip(equations, values):
            graphs[dividend][divider] = value
            graphs[divider][dividend] = 1 / value
            
        # Step 2. backtrack
        results = []
        for dividend, divider in queries:
            if dividend not in graphs or divider not in graphs:
                ret = -1.0
            elif dividend == divider:
                ret = 1.0
            else:
                visited = set()
                ret = backtrack(dividend, divider, 1, visited)
            results.append(ret)
                
        return results


if __name__ == "__main__":
    s_g = SolutionGraph()

    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expect = [6.0000, 0.50000, -1.00000, 1.00000, -1.00000]
    assert s_g.calcEquation(equations, values, queries) == expect

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expect = [3.75000, 0.40000, 5.00000, 0.20000]
    assert s_g.calcEquation(equations, values, queries) == expect

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expect = [0.50000, 2.00000, -1.00000, -1.00000]
    assert s_g.calcEquation(equations, values, queries) == expect

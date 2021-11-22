from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List


class Solution(ABC):
    @abstractmethod
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ...


class SolutionGraph(Solution):
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


class SolutionUnion(Solution):
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        gid_weights = {}

        def find(node_id):
            if node_id not in gid_weights:
                gid_weights[node_id] = (node_id, 1)
            group_id, node_weight = gid_weights[node_id]
            # The above statements are equivalent to the following one
            # group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weights[node_id] = (new_group_id, node_weight * group_weight)

            return gid_weights[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together
                # by attaching the dividend group to the one of divisor
                gid_weights[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weights or divisor not in gid_weights:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variable do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results


class SolutionUnionFindReview:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gid_weights = {}

        def find(node_id):
            if node_id not in gid_weights:
                gid_weights[node_id] = (node_id, 1)

            group_id, weight = gid_weights[node_id]
            if node_id != group_id:
                new_group_id, new_weight = find(group_id)
                gid_weights[node_id] = (new_group_id, weight * new_weight)

            return gid_weights[node_id]

        def union(dividend, divisor, value):
            dividend_group, dividend_weight = find(dividend)
            divisor_group, divisor_weight = find(divisor)
            if dividend_group != divisor_group:
                gid_weights[dividend_group] = (divisor_group, divisor_weight * value / dividend_weight)

        # make disjoint set
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        # find ans
        ans = []
        for dividend, divisor in queries:
            if dividend not in gid_weights or divisor not in gid_weights:
                ret = -1
            else:
                dividend_group, dividend_weight = find(dividend)
                divisor_group, divisor_weight = find(divisor)
                if dividend_group != divisor_group:
                    ret = -1
                else:
                    ret = dividend_weight / divisor_weight

            ans.append(ret)

        return ans


def check_cases(s: Solution):
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expect = [6.0000, 0.50000, -1.00000, 1.00000, -1.00000]
    s.calcEquation(equations, values, queries) == expect

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expect = [3.75000, 0.40000, 5.00000, 0.20000]
    s.calcEquation(equations, values, queries) == expect

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expect = [0.50000, 2.00000, -1.00000, -1.00000]
    s.calcEquation(equations, values, queries) == expect


def test_solution_graph():
    check_cases(SolutionGraph())


def test_solution_union():
    check_cases(SolutionUnion())

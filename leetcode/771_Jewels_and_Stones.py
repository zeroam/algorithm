from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set()
        for c in jewels:
            jewel_set.add(c)

        stone_map = defaultdict(lambda: 0)
        for c in stones:
            stone_map[c] += 1

        total = 0
        for c in jewel_set:
            total += stone_map[c]

        return total


def test_solution():
    s = Solution()

    assert s.numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
    assert s.numJewelsInStones(jewels="z", stones="ZZ") == 0

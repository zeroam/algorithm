class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_set = set()

        ans = []
        for v in s:
            if v not in hash_set:
                ans.append(v)
                hash_set.add(v)
            else:
                if v in ans:
                    ans.remove(v)

        if len(ans) == 0:
            return -1
        return s.find(ans[0])


def test_solution():
    solution = Solution()

    assert solution.firstUniqueChar("str") == 0
    assert solution.firstUniqueChar("aabb") == -1
    assert solution.firstUniqueChar("leetcode") == 0
    assert solution.firstUniqueChar("loveleetcode") == 2

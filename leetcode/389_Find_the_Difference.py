from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = dict()
        for c in t:
            t_count.setdefault(c, 0)
            t_count[c] += 1

            if t_count[c] > s_count[c]:
                result = c
                    
        return result
        

class SolutionSort:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1
            
        return sorted_t[i]
        

if __name__ == "__main__":
    solution = Solution()
    solution_sort = SolutionSort()

    s = "abcd"
    t = "abcde"
    assert solution.findTheDifference(s, t) == "e"
    assert solution_sort.findTheDifference(s, t) == "e"

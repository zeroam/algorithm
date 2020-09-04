class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(2, n + 1, 1):
            interval = n / i
            if not interval.is_integer():
                continue
                
            interval = int(interval)
            #print(f"interval: {interval}")
            for j in range(0, n - interval, interval):
                pre = s[j: j + interval]
                compare = s[j + interval: j + interval + interval]
                if pre != compare:
                    break
            else:
                # 모두 비교 했을 때 같으면
                return True
                    
        return False


if __name__ == "__main__":
    s = Solution()

    case = "abab"
    expect = True
    assert s.repeatedSubstringPattern(case) == expect

    case = "aba"
    expect = False
    assert s.repeatedSubstringPattern(case) == expect

    case = "abcabcabcabc"
    expect = True
    assert s.repeatedSubstringPattern(case) == expect

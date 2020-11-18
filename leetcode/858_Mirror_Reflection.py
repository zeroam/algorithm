class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # 최대 공약수 구하기
        def get_gcd(p: int, q: int) -> int:
            gcd = 1
            for i in range(2, min(p, q) + 1):
                while (p % i == 0) and (q % i == 0):
                    p = p // i
                    q = q // i
                    gcd = gcd * i
                    
            return gcd

        gcd = get_gcd(p, q)
        p = (p // gcd) % 2
        q = (q // gcd) % 2
        
        if p == 1 and q == 1:
            return 1
        elif p == 1 and q == 0:
            return 0
        elif p == 0 and q == 1:
            return 2
        else:
            return 0


if __name__ == "__main__":
    s = Solution()

    inputs = [2, 1]
    expect = 2
    assert s.mirrorReflection(*inputs) == expect

    inputs = [2, 0]
    expect = 0
    assert s.mirrorReflection(*inputs) == expect

    inputs = [2, 2]
    expect = 1
    assert s.mirrorReflection(*inputs) == expect

    inputs = [3, 2]
    expect = 0
    assert s.mirrorReflection(*inputs) == expect

    inputs = [6, 4]
    expect = 0
    assert s.mirrorReflection(*inputs) == expect

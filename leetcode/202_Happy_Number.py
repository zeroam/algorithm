class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        hash_set = set()

        total = 0
        while total != 1:
            total = 0
            for c in num:
                total += int(c) ** 2

            if total in hash_set:
                return False
            hash_set.add(total)
            num = str(total)

        return True


class SolutionCycle:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


class SolutionFloydsCycle:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total

        slow_runner = n
        fast_runner = get_next(n)

        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))

        return fast_runner == 1


def check_cases(s: Solution):
    assert s.isHappy(2) == False
    assert s.isHappy(3) == False
    assert s.isHappy(7) == True
    assert s.isHappy(19) == True
    assert s.isHappy(20) == False
    assert s.isHappy(116) == False


def test_solution():
    check_cases(Solution())


def test_solution_cycle():
    check_cases(SolutionCycle())


def test_solution_floyds_cycle():
    check_cases(SolutionFloydsCycle())

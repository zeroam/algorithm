import time
from typing import List
from functools import wraps


def time_elapsed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_dt = time.time()
        ans = func(*args, **kwargs)
        print(f"func: {func.__name__}, time_elapsed: {time.time() - start_dt}, ans: {ans}")
        return ans
    return wrapper


@time_elapsed
def no_memoization(nums: List[int], target: int):
    size = len(nums)

    def calculation(index: int, total: int) -> int:
        if index == size:
            if total == target:
                return 1
            return 0

        add = calculation(index + 1, total + nums[index])
        sub = calculation(index + 1, total - nums[index])

        return add + sub

    return calculation(0, 0)


@time_elapsed
def memoization(nums: List[int], target: int):
    size = len(nums)
    memo = [{} for _ in range(size)]

    def calculation(index: int, total: int) -> int:
        if index == size:
            if total == target:
                return 1
            return 0

        if memo[index].get(total):
            return memo[index][total]

        add = calculation(index + 1, total + nums[index])
        sub = calculation(index + 1, total - nums[index])
        memo[index][total] = add + sub
        print(memo)

        return memo[index][total]

    return calculation(0, 0)


if __name__ == "__main__":
    # no_memoization([13, 2, 4, 1, 1, 2, 3, 4, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 15)
    # memoization([13, 2, 4, 1, 1, 2, 3, 4, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 15)
    memoization([1, 1, 1, 1, 1], 3)

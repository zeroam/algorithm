from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            divide_by_3 = (i % 3 == 0)
            divide_by_5 = (i % 5 == 0)
            
            if divide_by_3 and divide_by_5:
                result.append("FizzBuzz")
            elif divide_by_3:
                result.append("Fizz")
            elif divide_by_5:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        return result


if __name__ == "__main__":
    s = Solution()

    n = 15
    print(s.fizzBuzz(n))

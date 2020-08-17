from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candy = 1
        acc_candy = 0
        turn = 0
        dists = [0] * num_people
        
        while acc_candy < candies:
            
            if candies - acc_candy < candy:
                candy = candies - acc_candy
                
            dists[turn % num_people] += candy
            
            acc_candy += candy
            candy += 1
            turn += 1
                
        return dists


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies(7, 4))

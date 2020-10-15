class SolutionUnsolved:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        max_total = 0
        def traverse_houses(index: int, total: int = 0):
            if index >= n:
                #print(f"total: {total}, index: {index}")
                nonlocal max_total
                if total > max_total:
                    max_total = total
                return
            
            #print(f"index: {index}")
            total = total + nums[index]
            
            traverse_houses(index + 2, total)
            traverse_houses(index + 3, total)
        
        # index 1 포함, n - 1 까지
        traverse_houses(1, 0)
        traverse_houses(2, 0)
        # index 0 포함, n - 2 까지
        n = n - 1
        traverse_houses(0, 0)
        
        return max_total
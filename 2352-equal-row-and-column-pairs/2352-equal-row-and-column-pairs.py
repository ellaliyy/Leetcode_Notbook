class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ans = 0
        
        for i in range(n): #iterate through rows
            for j in range(n): #iterate through columns
                if all(grid[i][k] == grid[k][j] for k in range(n)):
                    ans += 1
            
        return ans

class Solution:
    def climbStairs(self, n: int) -> int:
        
        i1 = 0
        i2 = 1
        
        for index in range(n):
            i = i1+i2
            i1 = i2
            i2 = i
            
        return i
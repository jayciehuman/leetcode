class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(100000):
            if i*i == x or (i*i < x and (i+1)*(i+1) > x):
                return i
        
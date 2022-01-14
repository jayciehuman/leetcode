class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(100000):
            try:
                if i*i == num:
                    return True
            except:
                return False
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        stringlist = []
        for digit in digits:
            stringlist.append(str(digit))
            
        string = ''.join(stringlist)
        num = int(string)
        num = num+1
        
        output = list(str(num))
        
        return output
        
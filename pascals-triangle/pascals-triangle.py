class Solution:
    def factorial(num):
        num = num
        output = 1

        for i in range(1,num+1):
            output = output * i
    
        return output  
        
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        
        for row in range(numRows):
            row_list = []
            for i in range(row+1):
                number = factorial(row) // (factorial(row - i)*factorial(i))
                row_list.append(number)
            output.append(row_list)
                
        return output
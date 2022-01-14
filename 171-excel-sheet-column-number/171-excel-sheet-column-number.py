class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        title = list(map(lambda x : alphabet.index(x) + 1, list(columnTitle)))[::-1]
        if len(title) == 1:
            number = title[0]
            return number
        else:
            number = title[0]
            for i in range(len(title)):
                if i != 0:
                    number += 26 ** i * title[i]
            return number
            
        
    
    

                
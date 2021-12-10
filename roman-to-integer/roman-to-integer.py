class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = ['I','V','X','L','C','D','M']
        Num = [1,5,10,50,100,500,1000]
        s_list = list(s)
        n_list = []
        for s in s_list:
            i = Num[Roman.index(s)]
            n_list.append(i)
        for x in range(0,len(n_list)-1):
            if n_list[x] < n_list[x+1]:
                n_list[x] = -n_list[x]
        return sum(n_list)
        
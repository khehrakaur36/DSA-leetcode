class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        def fun(curr , open , close):
            if len(curr) == 2*n:
                res.append(curr)
                return 

            if open<n:
                fun(curr + "(" , open + 1 , close)

            if close<open:
                fun(curr+ ")" , open , close + 1)
        fun("" ,0 , 0)        
        return res            
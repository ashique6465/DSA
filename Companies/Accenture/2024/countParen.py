def cal_paren(n):
    stack = []
    res = []
    def backtrack(openN,closeN):
        if openN == closeN ==n:
            res.append("".join(stack))
        if openN < n:
            stack.append('(')
            backtrack(openN+1,closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backtrack(openN,closeN+1)
            stack.pop()
    backtrack(0,0)
    return res
   
n = int(input())
print(cal_paren(n))

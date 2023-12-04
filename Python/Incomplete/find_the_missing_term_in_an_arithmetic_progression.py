
def generateParenthesis(n):
    # the result will need n open and n closing parentheses
    # only add open parenthsis is open < n
    # only add a closing parenthesis if closed < open
    # valid IF open -- closed == n

    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0)
    return res

print(generateParenthesis(3))
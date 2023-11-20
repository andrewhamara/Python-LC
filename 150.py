class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            match token:
                case '+':
                    r = stk.pop()
                    l = stk.pop()
                    stk.append(l + r)
                case '-':
                    r = stk.pop()
                    l = stk.pop()
                    stk.append(l - r)
                case '/':
                    r = stk.pop()
                    l = stk.pop()
                    stk.append(int(l / r)) # truncate
                case '*':
                    r = stk.pop()
                    l = stk.pop()
                    stk.append(l * r)
                case _: # integer
                    stk.append(int(token))
        return stk.pop() # final num left

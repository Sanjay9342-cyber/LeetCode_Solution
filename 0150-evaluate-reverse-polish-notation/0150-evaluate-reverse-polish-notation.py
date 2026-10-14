class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operation = {"+","-","*","/"}
        for token in tokens:
            if token in operation:
                b=stack.pop()
                a=stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token =="-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
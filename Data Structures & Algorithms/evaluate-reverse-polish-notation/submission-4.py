class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            match element:
                case "+":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    res = operand2 + operand1 
                    stack.append(res)
                case "-":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    res = operand2 - operand1 
                    stack.append(res)
                case "*":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    res = operand2 * operand1 
                    stack.append(res)
                case "/":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    res = operand2 / operand1 
                    stack.append(res)
                case _:
                    stack.append(element)
            

        return int(stack[0])
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openBracks = {'[', '(', '{'}

        for brack in s:
            if brack in openBracks:
                stack.append(brack)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x == '{' and brack != '}':
                    return False
                if x == '[' and brack != ']':
                    return False
                if x == '(' and brack != ')':
                    return False
        return True if not stack else False
                
            
        
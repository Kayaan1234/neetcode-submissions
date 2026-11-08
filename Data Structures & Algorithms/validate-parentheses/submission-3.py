class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return true
        
        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:

                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if bracket == ")" and temp != "(" or bracket == "}" and temp != "{" or bracket == "]" and temp != "[":
                    return False
        if len(stack) == 0:
            return True
        return False
        
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', ')': '(', '}': '{'}
        stack = []
        
        for bracket in s:
            if stack and bracket in pairs:
                if pairs[bracket] == stack[-1]:
                    stack.pop()
            else:
                stack.append(bracket)
        
        if stack == []:
            return True

        return False
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', ')': '(', '}': '{'}
        stack = []
        
        for bracket in s:
            if bracket in pairs:
                if stack and pairs[bracket] == stack[-1]:
                    stack.pop()
            else:
                stack.append(bracket)
        
        if stack == []:
            return True

        return False
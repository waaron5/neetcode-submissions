class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        open = ['[', '(', '{']
        pairs = {']': '[', ')': '(', '}': '{'}
        stack = []
        
        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            elif pairs[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if stack == []:
            return True

        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == '(':
                stack.append('(')
            elif symbol == '[':
                stack.append('[')
            elif symbol == '{':
                stack.append('{')
            elif symbol == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif symbol == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
            elif symbol == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            if len(stack) == 0:
                return True
        return False
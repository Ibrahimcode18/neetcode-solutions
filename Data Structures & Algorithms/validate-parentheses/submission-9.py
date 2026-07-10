class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = [')', '}', ']']
        hash_map = {')': '(', '}' : '{', ']': '['}
        for i in range(len(s)):
            if s[i] in hash_map and len(stack) != 0:
                if stack[-1] == hash_map[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        return True

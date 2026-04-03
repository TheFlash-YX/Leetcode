class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        map={'(':')','{':'}','[':']'}
        stack=[]

        for char in s:
            if char in map:
                stack.append(map[char])
            elif not stack or stack.pop()!=char:
                return False

        if stack:
            return False

        return True



Solution().isValid("([])")
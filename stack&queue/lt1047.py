class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)==0:
            return None
        stack=[]

        for char in s:
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)


        return ''.join(stack)
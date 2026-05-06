from collections import deque
class Solution:
    # 时间复杂度O（N）
    # 空间复杂度O（N）
    # 内置方法
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    # 双端队列
    def reverseWords(self, s: str) -> str:
        left=0
        right=len(s)-1

        while left<=right and s[left]==" ":
            left+=1
        while left<=right and s[right]==" ":
            right-=1

        que=deque()
        word=[]

        while left<=right:
            if s[left]==" " and word:
                que.appendleft("".join(word))
                word=[]
            elif s[left]!=" ":
                word.append(s[left])
            left+=1

        que.appendleft("".join(word))

        return " ".join(que)


Solution().reverseWords1("the sky is blue")

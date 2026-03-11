def reverseWords1(self, s: str) -> str:
    s=s[::-1]               #翻转字符串
                            # 将字符串拆分为单词，并反转每个单词
     # split()函数能够自动忽略多余的空白字符，列表形式
    s=' '.join(word[::-1] for word in s.split())

    return s

def reverseWords2(self, s: str) -> str:
    words=s.split()

    left,right=0,len(s)-1
    while left<right:
        words[left],words[right]=words[right],words[left]
        left+=1
        right-=1

    return ' '.join(words)

def reverseWords3(self, s: str) -> str:
    def single_reverse(self,s:str,start:int,end:int):
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1

    result=""
    fast=0

    s=list(s)
    s.reverse()
    while fast<len(s):
        if s[fast]!=' '!=0:
            if len(result)!=0:
                result+=' '
            while s[fast]!='' and fast<len(s):
                result+=s[fast]
                fast+=1
        else:
            fast+=1

    slow=0
    fast=0
    result=list(result)
    while fast <= len(result):
        if fast == len(result) or result[fast] == " ":
            self.single_reverse(result, slow, fast - 1)
            slow = fast + 1
            fast += 1
        else:
            fast += 1

    return "".join(result)




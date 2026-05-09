class Solution:
    # 用栈模拟递归
    def decodeString(self, s: str) -> str:
        st = []
        res=""
        k=0

        for c in s:
            if c.isalpha():
                res+=c
            elif c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                st.append((res,k))
                res=""
                k=0
            else:
                pre_res,pre_k=st.pop()
                res=pre_res+res*pre_k

        return res

Solution().decodeString("3[a]2[bc]")
class Solution:
    def calculate(self,nums:list[int])->int:
        stack=[]
        num=0
        pre_op="+"

        for i,ch in enumerate(nums):
            if ch.isdigit():
                num=num*10+int(ch)
            if (not ch.isdigit() and ch !=" ") or i==len(nums)-1:
                if pre_op=="+":
                    stack.append(num)
                elif pre_op=="-":
                    stack.append(-num)
                elif pre_op=="*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                pre_op=ch
                num=0
        return sum(stack)
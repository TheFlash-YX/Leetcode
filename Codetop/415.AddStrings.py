class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        flag = 0
        ans = []
        while i >= 0 or j >= 0 or flag > 0:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            cur_sum = digit1 + digit2 + flag
            flag = cur_sum // 10
            cur_digit = cur_sum % 10

            ans.append(str(cur_digit))
            i -= 1
            j -= 1

        return "".join(ans[::-1])

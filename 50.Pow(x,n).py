class Solution:

    # 递归
    def myPow1(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1.0

        return self.myPow(x, n // 2) ** 2 * (x if n % 2 else 1.0)

    # 非递归，位运算
    def myPow2(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            n = -n
            x = 1 / x

        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return ans

Solution().myPow2(2.0,10)
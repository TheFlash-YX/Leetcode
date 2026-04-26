class Solution:
    # 回溯+剪枝
    def getPermutation(self, n: int, k: int) -> str:
        self.result = []
        used = [False] * (n + 1)
        # 准备阶乘数组
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        self.backtrack(n, k, [], used, fact)

        return "".join(map(str, self.result))

    def backtrack(self, n, cur_k, path, used, fact):
        if len(path) == n:
            self.result = path[:]
            return

        branch_size = fact[n - len(path) - 1]

        for i in range(1, n + 1):
            if used[i]:
                continue
            if cur_k > branch_size:
                cur_k -= branch_size
            else:
                used[i] = True
                path.append(i)
                self.backtrack(n, cur_k, path, used, fact)


Solution().getPermutation(3,1)
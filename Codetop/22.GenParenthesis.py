class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.result = []
        self.backtrack(n, [], 0, 0)
        return self.result

    def backtrack(self, n, path, left_cnt, right_cnt):
        if len(path) == 2 * n:
            self.result.append("".join(path[:]))
            return

        if left_cnt < n:
            path.append("(")
            self.backtrack(n, path, left_cnt + 1, right_cnt)
            path.pop()
        if left_cnt > right_cnt:
            path.append(")")
            self.backtrack(n, path, left_cnt, right_cnt + 1)
            path.pop()


class Solution:
    def letterCombinations(self, digits: str) ->list[str]:
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.result = []
        self.backtrack(digits, 0, [])
        return self.result

    def backtrack(self, digits, index, path):
        if index == len(digits):
            self.result.append("".join(path[:]))
            return

        cur_letters = self.map[int(digits[index])]
        for char in cur_letters:
            path.append(char)
            self.backtrack(digits, index + 1, path)
            path.pop()

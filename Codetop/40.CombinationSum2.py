class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [])
        return self.result
    # 枚举选哪个
    def backtrack1(self, candidates, target, index, path):
        if target == 0:
            self.result.append(path[:])
            return

        for i in range(index, len(candidates)):
            if target < candidates[i]:
                break
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path)
            path.pop()
    # 选或不选
    def backtrack(self, candidates, target, index, path):
        if target<0:
            return
        if index==len(candidates) or candidates[index]>target:
            return

        # 选
        path.append(candidates[index])
        self.backtrack(candidates,target-candidates[index],path)
        path.pop()


        # 不选
        next_idx=index+1
        while next_idx<len(candidates) and candidates[next_idx]==candidates[index]:
            next_idx+=1
        self.backtrack(candidates,target,next_idx,path)


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.result=[]
        candidates.sort()
        self.backtrack(candidates,target,index=0,path=[])
        return self.result

    # 选或不选
    def backtrack1(self,candidates,target,index,path):
        if target==0:
            self.result.append(path[:])
            return
        if index==len(candidates) or candidates[index]>target:
            return

        # 不选

        self.backtrack(candidates,target,index+1,path)


        # 选
        path.append(candidates[index])
        self.backtrack(candidates,target-candidates[index],index,path)
        path.pop()


    # 选哪个
    def backtrack2(self, candidates, target, index, path):
        if target == 0:
            self.result.append(path[:])
            return

        for i in range(index, len(candidates)):
            if target < candidates[i]:
                break

            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, path)
            path.pop()


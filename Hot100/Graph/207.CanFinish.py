from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        inDegress,adjList=self.buildGraph(numCourses,prerequisites)

        return self.topologicalSort(numCourses,inDegress,adjList)
    # 辅助函数：负责建图
    def buildGraph(self, numCourses: int, prerequisites: list[list[int]]):
        inDegrees=[0]*numCourses
        adjList={}
        for i in range(numCourses):
            adjList[i]=[]
            
        for course,preCourse in prerequisites:
            inDegrees[course]+=1
            adjList[preCourse].append(course)

        return inDegrees,adjList


    # 辅助函数：负责拓扑排序
    def topologicalSort(self, numCourses: int, inDegrees: list[int], adjList: dict) -> bool:
        queue=deque()
        taken_count=0
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)

        while queue:
            course=queue.popleft()
            taken_count += 1
            for nextCourse in adjList[course]:
                inDegrees[nextCourse]-=1
                if inDegrees[nextCourse]==0:
                    queue.append(nextCourse)

        return taken_count==numCourses

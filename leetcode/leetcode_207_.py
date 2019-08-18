'''
LeetCode 207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    # 그래프 생성
    for pair in prerequisites:
        x, y = pair
        graph[x].append(y)
    # 각각 노드 방문
    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False
    return True

def dfs(graph, visited ,i):
    # 만약 i번째 노드가 방문된 것으로 마킹되어있으면, 사이클이 발견됨
    if visited[i] == -1:
        return False
    # 만약 이미 방문된 경우 다시 방문하지 않음
    if visited[i] == 1:
        return True
    # 방문된 것으로 마킹
    visited[i] = -1
    # 모든 이웃을 방문함
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False
    # a모든 이웃을 방문 후, 방문 완료로 표시
    visited[i] = 1
    return True
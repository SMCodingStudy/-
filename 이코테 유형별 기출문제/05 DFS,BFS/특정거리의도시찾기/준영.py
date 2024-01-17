from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리정보 K, 출발도시의 번호 X 입력
N, M, K, X = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
print(graph)

# print(graph)
# [[1, 2], [1, 3], [2, 3], [2, 4]]

# 특정 도시 X에서 K만큼 떨어진 도시의 정보를 출력해야한다
# 따라서 X에서 다른 도시들까지의 거리를 구하는 DFS 깊이탐색알고리즘을 사용해본다

# 내 착오였다. 이 문제의 경우 BFS를 사용해야했다

# 거리
distance = [0] * (N)
visited = [False] * (N)


def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
# def DFS(출발도시, 끝도시):


# 출발도시 X를 기점으로 bfs 알고리즘 실시
bfs(X)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

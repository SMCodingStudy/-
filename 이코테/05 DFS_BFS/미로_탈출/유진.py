import sys
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue: # 큐가 빌 때까지 반복
        x, y = queue.popleft()

        # 현재위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지형 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물있는 곳 무시
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 공간일 시
            if graph[nx][ny] == 1:
                # 갈 수 있는 공간이면 값+1
                graph[nx][ny] = graph[x][y] + 1
                # 큐에 이동할 곳 넣어두기
                queue.append((nx, ny))
    # 그래프의 마지막 값 리턴
    return graph[n - 1][m - 1]

print(bfs(0, 0))

# 몰라서 봤음
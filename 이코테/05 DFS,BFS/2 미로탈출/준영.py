# BFS 정리
# 큐를 사용하는데 그 중에서도 deque를 사용한다. deque는 성능 면에 있어 queue보다 우수한 면을 보이기 때문이다.
# 좌표 문제의 경우, 특히 상하좌우 문제의 경우 dx, dy에 저장을 해놓고 푸는 방법을 알게되었다.
# DFS의 경우 스택과 재귀를 사용하는데 BFS는 큐를 사용하고 큐에서 넣고 뺌을 꼭 명심하자!
# 안되면 외우기라도 하기 리스트 -> while queue / x, y = queue.popleft() / nx = x + dx[i] 등등...

from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어날 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽일 경우
            if graph[nx][ny] == 0:
                continue
            # 아직 방문하지 않은 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]


print(bfs(0, 0))

# 입력예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10

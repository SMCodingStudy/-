# 11:44

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 북동남서

n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[y][x] = True


answer = 1
while True:
    for i in range(4):
        ld = (d + 3) % 4  # 왼쪽 방향 계산
        # 왼쪽 방향의 좌표 계산
        ly = y + directions[ld][0]
        lx = x + directions[ld][1]
        d = ld

        # 왼쪽이 방문하지 않은 공간이고 바다가 아닌 경우, 이동하고 True로 변경합니다.
        if graph[ly][lx] == 0 and not visited[ly][lx]:
            answer += 1
            y, x = ly, lx
            visited[y][x] = True
            break
    # 네 방향 모두 바다이거나, 방문한 공간인 경우, 후진
    else:
        # 후진 방향 계산
        bd = (d + 2) % 4
        # 후진 방향의 좌표 계산
        by = y + directions[bd][0]
        bx = x + directions[bd][1]
        # 후진 방향이 바다인 경우, 작동을 멈춤
        if graph[by][bx] == 1:
            break
        else:
            y = by
            x = bx

print(answer)

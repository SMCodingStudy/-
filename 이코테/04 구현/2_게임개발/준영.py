import sys

# N x M 크기의 맵 생성
# 4   4
N, M = map(int, sys.stdin.readline().split())

# 게임 캐릭터의 위치좌표와 바라보는 방향
# 1 1 0
x, y, d = list(map(int, sys.stdin.readline().split()))
visited = [[False] * M for _ in range(N)]
visited[x][y] = True

arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 북동남서

count = 1

# 현재 바라보고 있는 방향을 기준으로 왼쪽으로 90도 ex) 북 -> 서 -> 남 -> 동
while True:
    for i in range(4):
        # 다음으로 바라볼 왼쪽 방향 설정
        next_d = (d + 3) % 4
        # 다음으로 바라볼 방향의 좌표 찾기
        next_x = x + directions[next_d][0]
        next_y = y + directions[next_d][1]
        # print(next_x, next_y)
        d = next_d

        # 만약 왼쪽이 방문하지 않았거나, 바다가 아닌 경우, 이동하고 True로 변경
        if arr[next_x][next_y] == 0 and not visited[next_x][next_y]:
            count += 1
            x, y = next_x, next_y
            visited[x][y] = True
            break
    # 네 방향이 모두 바다이거나, 방문한 공간인 경우, 후진
    else:
        # 후진 방향 계산
        bd = (d + 2) % 4
        bx = x + directions[bd][0]
        by = y + directions[bd][1]

        # 후진 방향이 바다인 경우, 작동을 멈춤
        if arr[bx][by] == 1:
            break
        else:
            x = bx
            y = by

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

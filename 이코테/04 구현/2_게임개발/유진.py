import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 북, 동, 남, 서
game_map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

# 맵 입력받기
for i in range(n):
    game_map.append(list(map(int, sys.stdin.readline().split())))

count = 1
turn_time = 0

# 게임시작
while True:
    # 1. 왼쪽 방향으로 회전
    d -= 1
    if d < 0 :
        d = 3
    
    # 2. 한칸 전진
    nx = x + direction[d][0]
    ny = y + direction[d][1]

    # 갈수있을 때
    if visited[x][y] == 0 and game_map[x][y] == 0:
        visited[x][y] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 바다 or 이미 간곳일 시
    else :
        turn_time += 1

    #모든면이 바다 or 간곳이라 회전을 끝냈을 때 후진
    if turn_time == 4:
        nx = x - direction[d][0]
        ny = y - direction[d][1]

        if game_map[x][y] == 0:
            x = nx
            y = ny
        
        #뒤에 바다
        else:
            break
        turn_time = 0

print(count)

# 간곳 배열 따로 안만들고 기존의 맵을 활용할 수도 있을 것 같은데.. 도저히 안돼서 포기
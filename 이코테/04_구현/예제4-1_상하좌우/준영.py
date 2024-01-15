import sys

# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# N x N 배열
N = int(sys.stdin.readline())

# 예를 들어 N개의 명령 수행을 따로 하라는 말이 없었으므로 arr라는 list에 명령들을 담음
arr = list(map(str, sys.stdin.readline().split()))

# 초기 좌표
now = [1, 1]

# arr에 담긴 명령어들을 조건문에 따라 좌표를 더하고 뺌
for i in arr:
    # 왼쪽으로 한 칸 이동
    if i == "L":
        # 왼쪽 끝이 아니라면, 즉 (2,y) 이상인 경우
        if now[1] > 1:
            # y의 좌표를 -1
            now[1] -= 1
    # 오른쪽으로 한 칸 이동
    elif i == "R":
        # 오른쪽 끝이 아니라면
        if now[1] < N:
            now[1] += 1
    # 위로 한 칸 이동
    elif i == "U":
        # 맨 위가 아니라면
        if now[0] > 1:
            now[0] -= 1
    # 아래로 한 칸 이동
    elif i == "D":
        if now[1] < N:
            now[0] += 1
print(now[0], now[1])

# 문제를 읽고 보통의 문제들처럼 N번의 실행 횟수가 지정되어있지않아 헷갈렸다
# 인터넷에서 해설을 보고 나니 이해가 되었다
# 횟수가 지정되지않은 경우 list에 명령들을 담으면 되었다는것이다

# 5
# R R R U D D

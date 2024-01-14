import sys

N, K = map(int, sys.stdin.readline().split())

# 총 연산 횟수
count = 0

while True:
    if N == 1:
        break
    # 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
    if N % K == 0:
        N //= K
    else:
        N -= 1
    # 몇 회 연산했는지 count
    count += 1

print(count)

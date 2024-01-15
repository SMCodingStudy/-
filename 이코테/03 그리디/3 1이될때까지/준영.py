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

# 거의 다 해결했으나 문제에 있어 이해가 가지않았음
# 따라서 해설과 코드를 보았으나 또한 이해가 되지않았다
# 조금 더 생각해보고 코드의 2번과정을 while문 안에서 위로 올렸고
# 1번과정을 밑으로 내렸더니 해결되었다.

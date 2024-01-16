import sys

# N, M 입력
N, M = map(int, sys.stdin.readline().split())

# 2차원 배열 만들기
# 한 번에 입력받아서 넣기
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 2차원 배열 확인
# print(arr)

# 선택된 N행 확인
# print(arr[N-1])

# N행 중 가장 작은 수 출력
print(min(arr[N-1]))

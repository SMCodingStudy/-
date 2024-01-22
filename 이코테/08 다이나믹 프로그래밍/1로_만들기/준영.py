X = int(input())

# 1~X까지 각각의 최단 거리를 기록하기 위해 크기가 30000인 배열을 만들고 0으로 초기화한다

arr = [0] * 30001

for i in range(2, X + 1):
    # 이전요소까지의 바로 아래 단계까지 가는 거리를 더해주기 위해 1을 더함
    arr[i] = arr[i-1] + 1

    # 2로 나누어질때
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
    # 3으로 나누어질때
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    # 5로 나누어질때
    if i % 5 == 0:
        arr[i] = min(arr[i], arr[i//5] + 1)

print(arr[X])

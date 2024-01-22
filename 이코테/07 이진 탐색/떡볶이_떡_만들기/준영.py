N, M = map(int, input().split())
dduck = list(map(int, input().split()))

dduck.sort()

mid = max(dduck) // 2
# print(mid)

for i in range(0, len(dduck)):
    sum = 0
    res = dduck[i] - mid
    sum += res
    # print("sum:", sum)
    if sum == M:
        print(dduck[i])
        break

# 정답 코드 (이진 탐색)
start = 0
end = max(dduck)

# 절단 위치
result = 0

while (start <= end):
    # 총 잘리는 떡의 길이
    total = 0
    mid = (start + end) // 2

    for i in dduck:
        # 절단기 길이보다 떡 길이가 길면 절단 가능
        if i > mid:
            total += i - mid

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

x = int(input())
d = [0] * 30001

# 보텀업 방식
for i in range(2, x + 1):
    # 1을 빼주는 경우
    # i - 1보다 하나의 연산(-1)을 더해줘야 하므로 +1
    d[i] = d[i - 1] + 1

    # 2로 나눌경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 3으로 나눌경우
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 5로 나눌경우
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
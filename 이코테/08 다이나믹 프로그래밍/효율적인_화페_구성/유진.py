import sys
input = sys.stdin.readline

n, m = 2, 15#map(int, input().split())
money = [2, 3]
#for _ in range(n):
#    money.append(int(input()))

d = [10001] * (m + 1)
# 1로 만들기 + 거스름돈 문제 같은데
# d를 10001개로 설정하는게 맞나? -> 1원이 있을 때? -> 화폐 단위별 개수를 저장하는 거라서 101개가 맞지 않을까
# d[1] = m일 듯.
# 점화식은?
# di = min(d[i - 1], d[m//i])
# 단단히 틀림. 
# 왜 i - k 인가...
d[0] = 0
for i in range(n):
    for j in range(money[i], m + 1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 0:
    print(-1)
else:
    print(d[m])
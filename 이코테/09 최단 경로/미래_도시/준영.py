import sys
input = sys.stdin.readline

# 무한대 설정
INF = int(1e9)

# 회사의 개수 N, 경로의 개수 M
N, M = map(int, input().split())

company = [[INF] * (N+1) for _ in range(N+1)]
# print(company)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            company[i][j] = 0

for i in range(M):
    x, y = map(int, input().split())
    company[x][y] = 1
    company[y][x] = 1

# X와 K가 공백으로 구분되어 차례대로 주어진다 (1 <= K <= 100)
X, K = map(int, input().split())

for i in range(N):
    for j in range(N):
        print(company[i][j], end=' ')
    print()

# 여기까지 2차원 리스트에서 자기 자신까지의 거리는 0, 인접한 회사끼리는 1, 두 칸 이상 떨어진 회사는 INF로 초기화

# 다음 과정은 두 칸 떨어진 회사까지의 거리를 테이블에 적용시켜야함

for k in range(1, N + 1):
    for a in range(1,  N + 1):
        for b in range(1, N + 1):
            company[a][b] = min(company[a][b], company[a][k] + company[k][b])

# 결과 출력
distance = company[1][k] + company[k][X]

if distance >= INF:
    print("-1")
else:
    print(distance)

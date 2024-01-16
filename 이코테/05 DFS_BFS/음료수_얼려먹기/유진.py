import sys

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def count_ice (x, y):
    if x < 0 or y < 0 or x > m or y > n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        count_ice(x + 1, y)
        count_ice(x, y + 1)
        count_ice(x - 1, y)
        count_ice(x, y - 1)
        return True
    return False

ice = 0
for i in range(n):
    for j in range(m):
        if count_ice(n, m) == True:
            ice += 1
print(ice)

# DFS
# 몰라서 보고함
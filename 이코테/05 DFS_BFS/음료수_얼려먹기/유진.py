import sys

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

ice = 0
for i in range(n):
    for j in range(m):
        if dfs(n, m) == True:
            ice += 1
print(ice)

# DFS
# 몰라서 보고함
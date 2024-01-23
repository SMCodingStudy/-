def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

# 간선들 리스트
edges = []
# 최종 비용
result = 0

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 #가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost # 오름차순 정렬해서 마지막 값이 가장 크기 때문

print(result - last)
# 마을을 두개로 하려고 길을 하나 끊는건가?
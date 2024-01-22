import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 간선들의 정보 입력받기
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 다익스트라
def dijkstra(start):
    q = [] # 우선순위 큐

    heapq.heappush(q, (0, start))
    # 시작지점 거리 0
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리했다면,
        if distance[now] < dist:
            continue

        # 지금 위치에서 비용계산을 하면
        for i in graph[now]:
            cost = dist + i[1]

            # 다른 노드를 거치는게 더 적게 걸린다면, 
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
dijkstra(c) # 다익스트라 함수 실행

# C와 연결된 도시 갯수 세기
count = 0

# 전보가 가는 시간 측정
# -> 총 걸리는 시간 = 가장 오래 걸리는 시간을 측정해야하는데 최댓값을 뽑아야 하나?
time = 0
for i in distance:
    if i != INF:
        count += 1
        time = max(time, i)

print(count - 1, time) # 시작노드 제외해야 해서 -1 해줘야 하는데 안함
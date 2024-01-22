import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드의 연결되어 있는 노드에 대한 정보들 - 인덱스 0 은 비워짐
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 - 인덱스 0 은 비워짐
distance = [INF] * (n + 1)

# 모든 간선들의 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드까지 c의 비용이 든다
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    # 시작 노드로 가는 비용 0
    heapq.heappush(q, (0, start))
    # 근데 큐에 넣는 것 만으로도 distance에 저장이 되나?
    distance[start] = 0

    while q: # q가 비어있지 않다면,
        # 최단 거리가 짧은 노드 꺼내기
        # 거리, 지금 노드
        dist, now = heapq.heappop(q)

        # 이미 처리된 적 있는가?
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # 지금까지 거리 + 다음 노드까지 거리

            # 현재 노드를 거쳐서, 다른 노드까지 이동하는 거리가 더 짧을 때
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
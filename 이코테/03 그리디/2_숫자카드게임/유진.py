import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
result = 0

for i in range(n):
    arr.append(min(list(map(int, sys.stdin.readline().split())))) 
    # result = max(result, min(list(map(int, sys.stdin.readline().split())))) -> 배열선언해서 하는 것 보다 빠르고 효율적일까? => 아무래도 그러긴할 듯
print(max(arr))

N = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)
print(arr[(N-1) // 2])

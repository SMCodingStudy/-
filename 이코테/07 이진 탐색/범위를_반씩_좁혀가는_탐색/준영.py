N, target = list(map(str, input().split()))

arr = list(map(str, input().split()))

for i in range(len(arr)):
    if arr[i] == target:
        print(i+1)

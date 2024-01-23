def binary_search(arr, start, end):

    if start > end:
        return None
    mid = (start + end) // 2
    while start <= end:
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return binary_search(arr, start, mid - 1)
        else:
            return binary_search(arr, mid + 1, end)


N = int(input())

arr = list(map(int, input().split()))

index = binary_search(arr, 0, N-1)

if index == None:
    print(-1)
else:
    print(index)

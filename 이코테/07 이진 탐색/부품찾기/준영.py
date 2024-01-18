def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 왼쪽에 확인하는 경우
        if arr[mid] > target:
            end = mid - 1
        # 오른쪽을 확인하는 경우
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return None


# 부품 N개
N = int(input())
arr1 = list(map(int, input().split()))

# 이진 탐색은 정렬된 list에서만 사용가능하기 때문에 sort
arr1.sort()

# 손님 요청 M개
M = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    result = binary_search(arr1, i, 0, N-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=" ")

from bisect import bisect_left, bisect_right

# 내가 처음 풀었던 풀이
N, x = map(int, input().split())

arr = list(map(int, input().split()))

# 배열에 x가 없는 경우 -1 출력

# 이진 탐색을 이용하여 arr에서 x와 같은 수까지 start와 end를 늘려가다가 더 이상 같이 않을 때 멈추고 start와 end의 길이를 구함

start = 0
end = len(arr) - 1


while start <= end:
    # mid = (start + end) // 2
    # print(mid)

    # start < x
    if arr[start] < x:
        start += 1
        # print("start, end:", start, end)
        # if arr[start] == x:
        #     break
    # x < end
    if arr[end] > x:
        end -= 1
        # print("start, end:", start, end)
        # if arr[end] == x:
        #     break
    if arr[end] == x and arr[start] == x:
        break

print(end - start + 1)
print()

##################################################################################
# 이진 탐색을 이용한 풀이
print("이진 탐색을 이용한 풀이")


def binary_search(arr, x, find_first):
    n = len(arr)
    start = 0
    end = n-1
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            result = mid
            if find_first:
                # x가 처음 등장하는 위치를 찾습니다.
                end = mid - 1
            else:
                # x가 마지막으로 등장하는 위치를 찾습니다.
                start = mid + 1
    return result


N, x = map(int, input().split())

arr = list(map(int, input().split()))

# 이진 탐색으로 첫 번째와 마지막 위치를 찾기
first_position = binary_search(arr, x, True)
last_position = binary_search(arr, x, False)

# 결과 출력
if first_position == -1 or last_position == -1:
    print(-1)
else:
    print(last_position - first_position + 1)

print()

##################################################################################
# bisect를 활용한 풀이


def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index


N, x = map(int, input().split())

arr = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(arr, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)

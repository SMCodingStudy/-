# 절단기의 길이를 이진탐색해서, 떡썰어보고, 결론 도출
# 이진 탐색 함수를 어떻게 구성해야 할까
# 절단기의 길이는 0 ~ 떡의 최대 길이
# 절반의 길이부터 설정해보고, 떡을 잘라서 m이 나오면 정답
def find(rice_cake, m, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0

        # 설정한 절단기 값으로 떡을 잘라서 모두 합한 값 도출
        for i in rice_cake:
            if i > mid :
                sum += i - mid
            else:
                continue

        # 절단기 길이가 맞는지 확인
        if sum == m:
            result = mid
            return result
        elif sum < m:
            end = mid - 1
        else:
            result = mid # "최대한 덜 잘랐을 때"!!!!!!!!
            start = mid + 1
    return None

n, m = 4, 1 #map(int, input().split())
rice_cake = [1, 2, 3, 4] #list(map(int, input().split()))

print(find(rice_cake, m, 0, max(rice_cake)))
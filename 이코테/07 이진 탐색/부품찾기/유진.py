def find(n_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return mid # return True도 맞지 않나
        elif n_list[mid] > target: 
            end = mid - 1
        else:
            start = mid + 1
    return None

n = 5 #int(input())
n_list = [8, 3, 7, 9, 2] #list(map(int, input().split()))
n_list.sort()
m = 3 #int(input())
m_list = [5, 7, 9] #list(map(int, input().split()))


for i in m_list:
    if find(n_list, i, 0, n - 1) != None:
        print("yes", end=" ")
    else: 
        print("no", end=" ")
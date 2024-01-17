# 전체 스테이지 수 N

# 사용자들이 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하는 solution 함수를 작성해라

def solution(N, stages):
    answer = []
    failure = {}

    분모 = len(stages)
    for i in range(1, N+1):
        분자 = stages.count(i)
        print(분자)
        if 분자 == 0:
            failure[i] = 0
        else:
            failure[i] = 분자 / 분모
            분모 -= 분자
    answer = sorted(failure, key=lambda x: failure[x], reverse=True)
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))

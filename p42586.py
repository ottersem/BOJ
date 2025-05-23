import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    deploy_day = days[0]
    count = 1

    for day in days[1:]:
        if day <= deploy_day:
            count += 1  # 앞 작업과 함께 배포됨
        else:
            answer.append(count)
            deploy_day = day  # 다음 배포 기준 갱신
            count = 1

    answer.append(count)  # 마지막 배포 묶음 추가
    return answer

progresses = [93, 30, 55]	
speeds = [1, 30, 5]	

solution(progresses=progresses, speeds=speeds)
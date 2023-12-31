# 기능 개발

# 예제1 progresses = [93, 30, 55], speeds = [1, 30, 5], result = [2, 1]
# 예제2 progresses = [95, 90, 99, 99, 80, 99], speeds = [1, 1, 1, 1, 1, 1],	result = [1, 3, 2]

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 출력 1 설명
# 첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
# 두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
# 세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

# 출력 2 설명
# 모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 
# 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.
# 따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.

def solution(progresses, speeds):
    result = []
    
    # speeds 리스트가 빈배열이 될때까지 (모든 배포가 완료될때 까지)
    while speeds:
        # 모든 작업의 개발 속도를 현재 진도에 더해줌, 작업의 인덱스와 속도를 순회
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed
        
        # 배포된 기능 갯수를 초기화함
        count = 0
        
        # 첫 번째 작업이 100이상 될때까지
        while progresses and progresses[0] >= 100:
            # 작업이 완료되면 첫 번째 작업을 삭제, 속도 또한 제거
            del progresses[0], speeds[0]
            count += 1
        
        if count > 0:
            result.append(count)
        
    return result 
        
    
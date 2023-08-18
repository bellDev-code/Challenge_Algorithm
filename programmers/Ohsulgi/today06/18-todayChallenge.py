# [PGS] 특이한 정렬/18/오슬기

def solution(numlist, n):
    distance = {}
    for i in numlist:
        if i not in distance:
            distance[i] = 0
        distance[i] = abs(n-i)

    distance = sorted(distance.items(), key=lambda x: x[1])

    arr = [distance[0][0]]
    cnt = 0
    for i in range(1, len(distance)):
        if distance[i][1] > cnt:
            arr.append(distance[i][0])
            cnt = distance[i][1]
        elif distance[i][1] == cnt:
            if distance[i][0] > arr[-1]:
                arr.insert(-1, distance[i][0])
            elif distance[i][0] < arr[-1]:
                arr.append(distance[i][0])

    return arr
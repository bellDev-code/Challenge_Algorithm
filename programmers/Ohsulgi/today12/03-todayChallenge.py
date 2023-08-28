'''
[PGS] 기사단원의 무기/03/오슬기

number까지의 모든 약수의 개수를 구할때 1부터 number까지 for문을 돌리면 시간복잡도가 O(n**2)이 된다
하지만 i의 배수는 항상 i를 약수를 갖는다는 점을 이용하면 시간을 많이 줄일 수 있다

'''

def solution(number, limit, power):
    arr = [0 for _ in range(number+1)]

    for i in range(1, number+1):
        for j in range(i, len(arr), i):
            arr[j] += 1

    arr = arr[1:]
    answer = 0
    for k in arr:
        if k > limit:
            answer += power
        else:
            answer += k
    return answer
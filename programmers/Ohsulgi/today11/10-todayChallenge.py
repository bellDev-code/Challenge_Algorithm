'''
[PGS] 소수 찾기/10/오슬기

n이 소수인지 판별하려면 2부터 n-1까지 나누어 떨어지지 않으면 된다
하지만 n이 여러개라면 시간복잡도가 O(n^2)이므로
2부터 루트n 까지 확인해도 동일한 결과가 나온다는 점을 이용해 시간을 줄일 수 있다

'''

def solution(n):
    def check(num):
        for i in range(2, int(num**(1/2)+1)):
            if num % i == 0:
                return False
        return True

    arr = [i for i in range(2, 1000000) if i <= n and check(i) == True]
    return len(arr)


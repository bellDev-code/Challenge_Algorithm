# [PGS] 연속된 수의 합/07/오슬기

def solution(num, total):
    answer = []
    if total != 0:
        if total > 0:
            for i in range(-2 * total, total * 2):
                result = (i * num) + int((num * (num-1)) / 2)

                if result == total:
                    for  j in range(i,i+num):
                        answer.append(j)
        else:
            for i in range(2 * total, -2 * total):
                result = (i * num) + int((num * (num-1)) / 2)

                if result == total:
                    for  j in range(i,i+num):
                        answer.append(j)
    else:
        answer.append(0)
        if len(answer) == num:
                print(answer)
        else:
            for i in range(1, num+1):
                answer.append(i)
                answer.append(-1 * i)
                if len(answer) == num:
                    break
    answer.sort()
    return answer
# 공백으로 구분하기 2

# my_string = " i    love  you"
# result = ["i", "love", "you"]
# join 함수의 예시: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
# 마지막으로 split 하여 배열로 변환한다.
def solution(my_string):
    return "".join(my_string).split()
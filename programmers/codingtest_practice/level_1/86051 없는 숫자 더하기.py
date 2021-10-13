def solution(numbers):
    answer = 45
    for i in range(len(numbers)):
        answer = answer - numbers[i]
    return answer
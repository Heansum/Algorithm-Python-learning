arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]


def solution(arr1, arr2):
    answer = []
    # [[1, 2],[2, 3]]
    # [[3, 4],[5, 6]]
    # [[4, 6],[7, 9]]
    # arr1[0][0] + arr2[0][0]  # -> 1 + 3
    # arr1[0][1] + arr2[0][1]  # -> 2 + 4
    # print(len(arr1))
    for i in range(len(arr1)):
        tmp_list = []
        for j in range(len(arr1[i])):
            # print(arr1[i][j])
            tmp = arr1[i][j] + arr2[i][j]
            tmp_list.append(tmp)
        answer.append(tmp_list)
    return answer


solution(arr1, arr2)

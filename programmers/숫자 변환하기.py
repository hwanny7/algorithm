def solution(x, y, n):
    answer = [1000000] * (y + 1)
    answer[x] = 0

    for i in range(x, y):
        if answer[i] == 1000000:
            continue

        first, second, third = i + n, i * 2, i * 3

        if first <= y:
            answer[first] = min(answer[first], answer[i] + 1)
        if second <= y:
            answer[second] = min(answer[second], answer[i] + 1)
        if third <= y:
            answer[third] = min(answer[third], answer[i] + 1)

    return answer[-1] if not answer[-1] == 1000000 else -1
# def find(B):
#     if B == 1:
#         return A
#     if B % 2:       #홀수일 경우
#         return find((B - 1) // 2) ** 2 * A
#     else:           #짝수일 경우
#         return find(B // 2) ** 2
#
#
# A, B, C = map(int, input().split())
# print(find(B) % C)

def find(B):
    if B == 1:
        return A % C
    else:
        if B % 2:       #홀수일 경우
            return (find((B - 1) // 2) ** 2 * A) % C
        else:           #짝수일 경우
            return (find(B // 2) ** 2) % C


A, B, C = map(int, input().split())
print(find(B))

# 마지막에 나머지 연산을 하는거나 계속해서 나머지 연산을 해오는거나 결과는 동일하다

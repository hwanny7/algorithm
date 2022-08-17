'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''




def dfs(v, end):
    visited = [0] * V       # 방문 여부 확인
    stack = [0] * V
    top = -1
    visited[v-1] = 1

    while True:
        for w in adjlist[v-1]:      #1번 노드가 0번 인덱스에서부터 시작되니까
            if visited[w-1] == 0:
                visited[w-1] = 1

                top += 1
                stack[top] = v      # v를 w로 바꾸기 전에 stack에 저장해두기

                if w == end:

                    return 1
                v = w               #다음 while 문에서도 자동으로 실행되도록 v를 w로 초기화 시킨다.
                break
        else:       # w가 방문한 경우일 경우 break을 하기 위해서 for else 형식으로 작성
            if top != -1:
                v = stack[top]
                top -= 1        # top에 위치한 노드가 pop 돼서 없어진 것으로 간주하기 위해서 -1을 해준다
            else:
                return 0        #더이상 갈 수 있는 노드가 없어서 마지막 노드까지 돌아가서 top이 -1 이 됐을 때 break



for t in range(1, int(input())+1):
    V, E = map(int, input().split())   # V는 노드 개수

    adjlist = [[] for _ in range(V)]

    for _ in range(E):      #간선 개수만큼 받기
        a, b = map(int, input().split())
        adjlist[a-1].append(b)
        # adjlist[b-1].append(a)
    print(adjlist)
    start, end = map(int, input().split())
    print(f'#{t}', dfs(start, end))



# deque랑 enque랑 그림 그려보면서 해보기
# 최대힙으로 실습, 최소힙은 최대힙을 전부 반대로 진행하면 된다.
# 최대힙 또는 최소힙은 완전이진트리를 이뤄야함

''' 2, 5, 7, 3, 4, 6 의 순서로 넣을 경우'''
def enq(n):
    global last
    last += 1       #마지막 정점 추가
    heap[last] = n  #마지막 정점에 key값(인덱스) 추가

    c = last
    p = c // 2      # 완전 이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 부모가 있고(조건식에 먼저 적어야 인덱스 오류가 나지 않는다), 부모 < 자식 인 경우 자리 교환 (조건이 만족하는 경우 계속 진행)
        heap[p], heap[c] = heap[c], heap[p]
        c = p       #부모였던 노드를 자식으로 만들고 다시 이 노드의 부모를 구한다.
        p = c // 2


heap = [0] * 100
last = 0            #아직까지 한개도 들어오지 않은 상태

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)

#힙에서 삭제
'''루트 노드의 원소 삭제 > 마지막 노드 삭제(last -= 1) > 
루트에 옮긴 값을 자식노드와 자리 바꾸기 
(최대힙이면 자식이 클 경우 교환, 최소힙이면 자식이 작을 경우 교환)'''

def deq():
    global last
    temp = heap[1]      # 루트 삭제 전 저장

    # 삭제할 노드의 키를 루트에 복사
    heap[1] = heap[last]
    last -= 1           # 마지막 노드 삭제
    p = 1
    c = p * 2           # 왼쪽 자식
    while c <= last:    # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:     # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                                      # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c               # 자식을 새로운 부모로 바꾼다
            c = p * 2
        else:
            break               # 부모가 더 큰 경우 비교 중단

    return temp

while last:
    print(deq())

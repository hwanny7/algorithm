def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:       #두개가 교차하기 전까지
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s - 1)
        qsort(s + 1, r)

A = [7, 2, 5, 3, 4, 5]
N = len(A)
qsort(0, N - 1)
print(A)


#================================================

def quick_hoare(lo, hi):

    if lo >= hi: return

    #partition
    i, j = lo, hi
    p = arr[lo]         #피봇: arr[lo]
    while i <= j:
        while i <= hi and p >= arr[i]:      # i <= hi 는 경계 체크
            i += 1
        while p < arr[j]:                   #항상 pivot 전에 멈출 것이기 때문에 경계 체크가 필요없음
            j -= 1

        if i < j:                           #서로 만나지 않았을 때만 교환
            arr[i], arr[j] = arr[j], arr[i]

    #while 문이 끝났을 때 P / 작은값들 / 큰값들로 어느정도 정렬되게 된다.
    #PIVOT을 I에 두면 큰값에 피봇보다 큰값에 들어가기 때문에 J에 둬야 한다.

    arr[lo], arr[j] = arr[j], arr[lo]
    # 분할 위치는 pivot 이 있는 j 인덱스
    quick_hoare(lo, j - 1)
    quick_hoare(j + 1, hi)

arr = [69, 30, 10, 2, 16, 8, 32, 21, 21, 32]
quick_hoare(0, len(arr) - 1)
print(arr)



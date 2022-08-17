def binarysearch(a, N, key):
    start = 0
    end = N-1     #(0부터 7)
    while start <= end:      # start == end 일때도 검색을 해야해기 때문에 / 만약 start == end인 상황에서 원하는 키값보다 값이 큰 경우 end가 start보다 작아지기 때문에 break
        middle = (start+end) // 2      #몫을 구해서 소수점일 경우 올림
        if a[middle] == key : #검색 성공
            return True     #또는 인덱스 return
        elif a[middle] > key:    #키 값이 작은 경우
            end = middle - 1
        else:
            start = middle + 1    #키값이 더 큰 경우
    return False  #검색 실패 (if 에서 true가 안 나왔을 경우 실패)
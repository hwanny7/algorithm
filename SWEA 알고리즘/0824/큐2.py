q = []

q.append(10)
q.append(20)
q.append(30)

print(q.pop(0))     # 이 방법을 쓰면 속도가 많이 느리다.
print(q.pop(0))     # deque 외장함수를 쓰면 속도 문제는 해결이 된다.
print(q.pop(0))
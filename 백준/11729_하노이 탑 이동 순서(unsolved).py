def H():
    O = one.pop(0)
    if O == 0:
        return
    if three[-1] < 0:
        three.append(O)
        H()
    else:

top = -1
one = list(range(0, int(input()) + 1))
two = [0]
three = [0]

print(one.pop())